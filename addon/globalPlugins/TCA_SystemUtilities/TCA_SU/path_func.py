#!/usr/bin/python
# -*- coding: utf-8 -*-
#TCASystemUtilities, Shut down and restart the PC with Windows classic sound, an Open system Options.
#Autor: Peter Reina<peterrc87@gmail.com><Tecnoconocimiento Accesible  2020>
# This file is covered by the GNU General Public License.

import ui, api, keyboardHandler, globalVars, addonHandler, shellapi, tones
from time import sleep
import os, ctypes, sys, platform  
import wx
from .win32 import win32clipboard as cb

addonHandler.initTranslation()

	
'''Función para obtener la ruta del ssistema( Win32), es cortesía de:
Héctor Benítez Corredera<xebolax@gmail.com>'''

def GetPath(self):
	sleep(0.5)
	keyboardHandler.KeyboardInputGesture.fromName("Control+c").send()
	try:
		cb.OpenClipboard()
	except:
		cb.CloseClipboard()
		cb.OpenClipboard()
	if cb.IsClipboardFormatAvailable(cb.CF_HDROP):
		clipboard_file_path = cb.GetClipboardData(cb.CF_HDROP)
		cb.CloseClipboard()
		numList = len(clipboard_file_path)
		if numList == 0: # Si no hay nada informamos
			ui.message(_("No se pudo tomar el foco, seleccione algún elemento"))
			return False
		else: 
			if numList == 1: 
				return clipboard_file_path[0]
			else: 
				ui.message(_("Ha seleccionado %s ficheros. Seleccione solo un fichero.") % numList)
				return False
	else: 
		ui.message(_("No se tomó el foco, mueva la flecha o seleccione algún elemento"))
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
		return self.v_obj


#Función que comprobará cual de los 2 métodos para obtener el path del sistema es válido.
def fs_path(self):
	t_obj(self)
	
	if self.v_obj is not False and os.path.dirname('{}'.format(self.v_obj)) != '':
		self.path = '{}'.format(self.v_obj)
	else:
		z_path(self)
		if self.v_path is not False:
			self.path = '{}'.format(self.v_path)
		else:
			self.path = False
	return self.path