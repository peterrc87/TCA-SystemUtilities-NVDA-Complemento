#!/usr/bin/python
# -*- coding: utf-8 -*-
#TCASystemUtilities, Shut down and restart the PC with Windows classic sound, an Open system Options.
#Autor: Peter Reina<peterrc87@gmail.com><Tecnoconocimiento Accesible  2020>
# This file is covered by the GNU General Public License.

import os, subprocess
import ctypes 
from threading import Thread

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
	def __init__(self, frame):
		super(T_h, self).__init__()
		self.frame = frame
		self.daemon = True
		self.start()
	def run(self):
		subprocess.Popen('Systeminfo | clip', shell=True)
		