#!/usr/bin/python
# -*- coding: utf-8 -*-
#TCASystemUtilities, Shut down and restart the PC with Windows classic sound, an Open system Options.
#Autor: Peter Reina<peterrc87@gmail.com><Tecnoconocimiento Accesible  2020>
# This file is covered by the GNU General Public License.

import os, subprocess
import ctypes 
from threading import Thread
import wx
import winsound
import ui, api

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