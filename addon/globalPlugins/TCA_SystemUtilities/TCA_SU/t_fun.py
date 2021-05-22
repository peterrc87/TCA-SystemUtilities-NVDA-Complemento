#!/usr/bin/python
# -*- coding: utf-8 -*-
#TCASystemUtilities, Shut down and restart the PC with Windows classic sound, an Open system Options.
#Autor: Peter Reina<peterrc87@gmail.com><Tecnoconocimiento Accesible  2020>
# This file is covered by the GNU General Public License.

import os, subprocess, threading
import ctypes 
from threading import Thread
import wx
import winsound
import ui, api, 	keyboardHandler, globalVars, addonHandler
a_path = os.getcwd()
addonHandler.initTranslation()


class disable_file_system_redirection:

	_disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
	_revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection

	def __enter__(self):
		self.old_value = ctypes.c_long()
		self.success = self._disable(ctypes.byref(self.old_value))

	def __exit__(self, type, value, traceback):
		if self.success:
			self._revert(self.old_value)

def ejecutar(modo, aplicacion, parametros, directorio, ventana):
	p = ctypes.windll.shell32.ShellExecuteW(
		None,
		modo,
		aplicacion,
		parametros,
		directorio,
		ventana)
	return p
#Clase para hilos.
class T_h(Thread):
	def __init__(self, frame, op):
		super(T_h, self).__init__()
		self.frame = frame
		self.op = op
		self.daemon = True
		self.start()
	def run(self):
		def TCAShut():		
			ui.message('Apagando el Pc.')
			winsound.PlaySound('C:\Windows\Media\Windows Shutdown.wav',winsound.SND_FILENAME)
			si = subprocess.STARTUPINFO()
			si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
			subprocess.run('shutdown.exe -s -t 3', shell=True, startupinfo=si)
		def TCAShutR():
			ui.message('Reiniciando el PC.')
			winsound.PlaySound('C:\Windows\Media\Windows Shutdown.wav',winsound.SND_FILENAME)
			si = subprocess.STARTUPINFO()
			si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
			subprocess.run('shutdown.exe -r -t 3', shell=True)
	
		def TCAShutA():
			ui.message('anulando el apagado o reinicio del pc.')
			subprocess.run('shutdown.exe -a', shell=True)

		def TCAcopy_sys():
			subprocess.Popen('Systeminfo | clip', shell=True)
		def TCAList():
			f = api.getForegroundObject()
			try:
				obj = f.children[1].children[2].children[0].children[0].children[0]
			except:
				obj = f.children[1].children[0].children[2].children[0].children[0].children[0]

			c_obj=obj.name
			a=c_obj.replace('Dirección: ', '')
			os.chdir('{}'.format(a))
			subprocess.Popen('dir /b|clip', shell=True)
			os.chdir(a_path)
			ui.message('Copiada la lista al portapapeles')
		def TCAsfc():
			try:
				os.environ['PROGRAMFILES(X86)']
				with disable_file_system_redirection():
					ejecutar('runas', 'cmd.exe', '/c' + 'sfc' + '/scannow' + '&pause', None, 10)				
			except:
				ejecutar('runas', 'cmd.exe', '/c' + 'sfc' + '/scannow' + '&pause', None, 10)								
											
			
		def TCAcopitar():
			lt=['powershell', 'Get-WmiObject Win32_SoundDevice |clip']
			subprocess.run(lt, shell=True)
			ui.message('Copiada la info del sonido al portapapeles')
		
		def ocu():
			f = api.getForegroundObject()
			try:
				obj = f.children[1].children[2].children[0].children[0].children[0]
			except:
				obj = f.children[1].children[0].children[2].children[0].children[0].children[0]
			c_obj=obj.name
			a=c_obj.replace('Dirección: ', '')
			d=os.path.dirname(a)
			b=os.path.basename(a)
			os.chdir(d)
			#keyboardHandler.KeyboardInputGesture.fromName("alt+leftarrow").send()

			try:
				os.environ['PROGRAMFILES(X86)']
				with disable_file_system_redirection():

					#subprocess.run('attrib /d /s +h {}'.format(b), shell=True)
					ejecutar(None,'cmd.exe', '/c' + 'attrib /d /s +h {}'.format(b), None, 10)	
				keyboardHandler.KeyboardInputGesture.fromName("alt+f4").send()
				os.startfile(d)
				winsound.Beep(900,300)
				os.chdir(a_path)
			except:
				ejecutar(None,'cmd.exe', '/c' + 'attrib /d /s +h'.format(b), None, 10)		
				#keyboardHandler.KeyboardInputGesture.fromName("alt+leftarrow").send()
				
				keyboardHandler.KeyboardInputGesture.fromName("alt+f4").send()
				os.startfile(d)
				#subprocess.run('attrib -h {}'.format(b), shell=True)
				winsound.Beep(900,300)
				os.chdir(a_path)

		
		def mos():
			f = api.getForegroundObject()
			try:
				obj = f.children[1].children[2].children[0].children[0].children[0]
			except:
				obj = f.children[1].children[0].children[2].children[0].children[0].children[0]
			c_obj=obj.name
			a=c_obj.replace('Dirección: ', '')
			#d=os.path.dirname(a)
			#b=os.path.basename(a)
			os.chdir(a)
			try:
				os.environ['PROGRAMFILES(X86)']
				with disable_file_system_redirection():  
					subprocess.Popen('attrib /d -h', shell=True)
					#ejecutar(None,'cmd.exe','/c' + 'attrib /d /s -h', None, 10)		
					os.chdir(a_path)
					winsound.Beep(300,300)
			except:
				#ejecutar('runas','cmd.exe','/c' + 'attrib /d -h', None, 10)		
				subprocess.Popen("attrib /d -h", shell = True)
				os.chdir(a_path)
				winsound.Beep(300,300)


		
		def clean():
			if os.path.isfile(os.path.join(globalVars.appArgs.configPath,"tsu.ini")):
				pass
			else:
				dlg=wx.RichMessageDialog(None,"Si es la primera vez que ejecuta ésta acción.\n es necesario crear un perfil de limpieza, solo debe hacerlo una vez.\n puede pulsar en Crear perfil también si desea mmofificar uno existente, o puede marcar  la casilla para no volver a mostrar éste mensaje.", style=wx.CANCEL) 
				dlg.SetOKLabel("Crear perfil")
				dlg.ShowCheckBox("No volver  a mostrar este mensaje")		
				rp = dlg.ShowModal()
				if dlg.IsCheckBoxChecked():
					with open(os.path.join(globalVars.appArgs.configPath,"tsu.ini"), "w") as tsu_i:
						tsu_i.write("sageset: True")
				else:
					pass
				
				if rp == wx.ID_OK:
					try:
						os.environ['PROGRAMFILES(X86)']
						with disable_file_system_redirection(): 
							#try:
							ejecutar('runas','cmd.exe','/c' + 'CLEANMGR /sageset:1', None, 10)	
					
					except:
						ejecutar('runas','cmd.exe', '/c' + 'CLEANMGR /sageset:1', None, 10)		
				else:
					dlg.Destroy()
			
			try:
				os.environ['PROGRAMFILES(X86)']
				with disable_file_system_redirection():  
					ejecutar('runas','cmd.exe', '/c' + 'CLEANMGR /sagerun:1', None, 10)	
					
			except:
				ejecutar('runas','cmd.exe', '/c' + 'CLEANMGR /sagerun:1', None, 10)				

			

		if self.op == 4:
			wx.CallAfter(TCAcopy_sys)
		elif self.op == 1:
			wx.CallAfter(TCAShut)
		elif self.op == 2:
			wx.CallAfter(TCAShutR)
		elif self.op == 3:
			wx.CallAfter(TCAShutA)
		elif self.op == 5:
			wx.CallAfter(TCAList)
		elif self.op == 6:
			wx.CallAfter(TCAsfc)
		elif self.op == 7:
			wx.CallAfter(TCAcopitar)
		elif self.op == 8:
			wx.CallAfter(ocu)
		elif self.op == 9:
			wx.CallAfter(mos)
		elif self.op == 10:
			wx.CallAfter(clean)

