#!/usr/bin/python
# -*- coding: utf-8 -*-
#TCASystemUtilities, Shut down and restart the PC with Windows classic sound, an Open system Options.
#Autor: Peter Reina<peterrc87@gmail.com><Tecnoconocimiento Accesible  2020>
# This file is covered by the GNU General Public License.

import ui, api, keyboardHandler, globalVars, addonHandler, shellapi, tones
from time import sleep
import os, ctypes, sys, platform  
import wx
#if sys.version.startswith("3.11"):
	#from ._311 import win32clipboard as cb
if sys.version.startswith("3.13"):
	from ._313 import win32clipboard as cb

addonHandler.initTranslation()

	
'''Función para obtener la ruta del ssistema( Win32), es cortesía de:
Héctor Benítez Corredera<xebolax@gmail.com>'''
def GetPath(self):
	count_attempts = 0	
	clipboard_opened = False

	try:
		sleep(0.7)
		keyboardHandler.KeyboardInputGesture.fromName("Control+c").send()
		sleep(0.5)

		max_attempts = 5
		while count_attempts < max_attempts:
			sleep(0.3 * (count_attempts + 1))  # Espera progresiva
			clipboard_opened = False
			
			try:
				cb.OpenClipboard(0)
				clipboard_opened = True
				
				if cb.IsClipboardFormatAvailable(cb.CF_HDROP):
					clipboard_file_path = cb.GetClipboardData(cb.CF_HDROP)
					cb.CloseClipboard()
					clipboard_opened = False
					
					if not clipboard_file_path or len(clipboard_file_path) != 1:
						raise ValueError("Selección inválida")
					
					path = clipboard_file_path[0]
					if not os.path.exists(path):
						raise FileNotFoundError("Ruta no existe")
					
					return path
				else:
					# No hay datos de archivo en el portapapeles
					cb.CloseClipboard()
					clipboard_opened = False
					
			except Exception as e:
				if clipboard_opened:
					try:
						cb.CloseClipboard()
					except:
						pass  # Ignorar errores al cerrar
				
				if count_attempts == max_attempts - 1:
					ui.message(_("Error: {}. Por favor seleccione el elemento nuevamente").format(str(e)))
		
			count_attempts += 1
			sleep(0.5)
		
		ui.message(_("No se tomó el foco, mueva la flecha o seleccione algún elemento"))
		return False

	except Exception as e:
		if clipboard_opened:
			try:
				cb.CloseClipboard()
			except:
				pass  # Ignorar errores al cerrar
		ui.message(_("Error inesperado: {}").format(str(e)))
		return False			
		
#función para crear el path.
def z_path(self):
	p = GetPath(self) 
	
	if ctypes.windll.user32.OpenClipboard(None):
		ctypes.windll.user32.EmptyClipboard()
		ctypes.windll.user32.CloseClipboard()
	if p == False:
		self.v_path = False
		return self.v_path
	else: 
		self.v_path = os.path.dirname(os.path.abspath(p))
		return self.v_path

#Función para la ruta con  el obj.
def t_obj(self):
	f = api.getForegroundObject()
	if int(platform.release()) > 8:
		try:
			obj = f.children[1].children[2].children[0].children[0].children[0]
		except:
			try:
				obj = f.children[0].children[0].children[4].children[0].children[0].children[0] #  Esta es para la ruta
			except:
				try:
					obj = f.children[0].children[2].children[0].children[0].children[0] 
				except:
					try:
						obj = f.children[1].children[0].children[4].children[0].children[0].children[0]
					except:
						try:
							obj = f.children[4].children[0].children[4].children[0].children[0].children[0]
						except:
							#win10
							try:
								obj = f.children[1].children[2].children[0].children[0].children[0]
							except:
								try:
									obj = f.children[3].children[0].children[4].children[0].children[0].children[0]	
								except:
									pass
	elif int(platform.release()) <= 8:
		try:
			obj = f.children[1].children[0].children[2].children[0].children[0].children[0]
		except:
			pass
	
	try:
		c_obj = obj.name
	except:
		c_obj = None
	
	if c_obj is not None: 
		self.v_obj = r"{}".format( c_obj.replace(_('Dirección: '), ''))

		if int(platform.release()) > 8 and os.path.dirname(self.v_obj) == '':
			self.v_obj =r"{}".format( c_obj.replace(_('Dirección: '), '').replace(_('Vídeos'), _('Videos')))

			if os.path.isdir(os.path.join(os.environ['userprofile'], "OneDrive", self.v_obj)):
				self.v_obj = os.path.join(os.environ['userprofile'], "OneDrive", self.v_obj)
			elif os.path.isdir(os.path.join(os.environ['userprofile'], self.v_obj)):
				self.v_obj = os.path.join(os.environ['userprofile'], self.v_obj)
			return self.v_obj		
		else:
			return self.v_obj		
	else:
		self.v_obj = False


#Función que comprobará cual de los 2 métodos para obtener el path del sistema es válido.
def fs_path(self):
	obj = explorer_active()
	target_path = get_explorer_path(self, obj)
	if target_path is not None:
		# Si es un archivo, obtener el directorio padre
		if os.path.isfile(target_path):
			#target_path = os.path.dirname(target_path)
			pass
	else:
		target_path = ''
	if os.path.exists(target_path):
		self.path = target_path 
	# Intentar el método del objeto
	elif t_obj(self) and os.path.exists(self.v_obj):
		self.path = self.v_obj
	else:
		# Usar método del portapapeles
		if z_path(self) and os.path.exists(self.v_path):
			self.path = self.v_path
		else:
			self.path = False
	return self.path


#función que comprueba si está activa una ventana del explorador.
def explorer_active():
	obj = api.getForegroundObject()
	if not obj or not obj.appModule or obj.appModule.appName != 'explorer':
		ui.message(_('Active una ventana del explorador antes de ejecutar esta acción'))
		return False
	else:
		return obj

#Función para obtener la ruta del elemento con foco en el explorador usando COM
def get_explorer_path(self, obj):
	from comtypes.client import CreateObject as COMCreate
	
	if not hasattr(self, '_shell'):
		self._shell = COMCreate('shell.application')
	
	target_path = None
	for window in self._shell.Windows():
		if window.hwnd == obj.windowHandle:
			try:
				target_path = str(window.Document.FocusedItem.path)
				break
			except:
				continue
	
	if not target_path:
		return None
	
	if not os.path.exists(target_path):
		return None
	
	return target_path