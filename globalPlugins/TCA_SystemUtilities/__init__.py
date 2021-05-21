# -*- coding: UTF-8 -*-
#TCASystemUtilities, Shut down and restart the PC with Windows classic sound, an Open system Options.
#Autor: Peter Reina<peterrc87@gmail.com><Tecnoconocimiento Accesible  2020>
# This file is covered by the GNU General Public License.
from scriptHandler import script
import api
import keyboardHandler
import globalPluginHandler
import subprocess, os, sys 
import webbrowser
import tones
import ui
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from TCA_SU import t_fun as tsu

class GlobalPlugin(globalPluginHandler.GlobalPlugin):	
	@script(description='Apagar el sistema', category='TCA-SystemUtilities', gesture='kb:nvda+shift+a')
	def script_TCAShut(self,gesture):		
		tsu.T_h(self,1)
	
	@script(description='Reinicio del sistema', category='TCA-SystemUtilities', gesture='kb:nvda+shift+r')
	def script_TCAShutR(self,gesture):
		
		tsu.T_h(self, 2)
	
	@script(description='Anular apagado', category='TCA-SystemUtilities', gesture='kb:nvda+0')
	def script_TCAShutA(self,gesture):
		tsu.T_h(self, 3)
		
	@script(description='Abrir Explorador Windows', category='TCA-SystemUtilities', gesture='kb:nvda+e')
	def script_OpenEx(self,gesture):
		os.system('explorer')
	
	@script(description='Abrir opciones de sonido', category='TCA-SystemUtilities', gesture='kb:nvda+shift+3')
	def script_TCARexplo(self,gesture):
		subprocess.Popen('mmsys.cpl', shell=True)
	
	@script(description='Abrir carpeta Roaming', category='TCA-SystemUtilities', gesture='kb:nvda+9')
	def script_TCARoa(self,gesture):
		os.startfile(os.path.join(os.environ['userprofile'], 'appdata', 'Roaming'))
	
	@script(description='Abrir Asistente transferir archivos por Bluetooth  ', category='TCA-SystemUtilities', gesture='kb:nvda+shift+9')
	def script_TCAopti(self,gesture):
		subprocess.Popen('fsquirt')
			 
	@script(description='Saber la arquitectura del sistema', category='TCA-SystemUtilities')
	def script_TCAar(self,gesture):
		try:
			os.environ['PROGRAMFILES(X86)']
			version_sys=64
		except:
			version_sys=32
		ui.message('Su sistema operativo es de: {} Bits'.format(version_sys))
		
	@script(description='Abrir el asistente para guardar la contraseña del sistema', category='TCA-SystemUtilities')
	def script_TCArcon(self,gesture):
		ui.message('Abriendo restablecer   contraseñas de Windows')
		subprocess.Popen('RunDll32.exe keymgr.dll,PRShowSaveWizardExW')
	
	@script(description='Copiar al portapapeles la ruta', category='TCA-SystemUtilities')
	def script_TCAclip(self,gesture):
		f = api.getForegroundObject()
		try:
			obj = f.children[1].children[2].children[0].children[0].children[0]
		except:
			obj = f.children[1].children[0].children[2].children[0].children[0].children[0]
		c_obj=obj.name
		a=c_obj.replace('Dirección: ', '')
		api.copyToClip('"{}"'.format(a))
		ui.message('Ruta copiada ')
		
	@script(description='Abrir el administrador de discos', category='TCA-SystemUtilities')
	def script_TCAdisk(self,gesture):
		subprocess.Popen('diskmgmt.msc', shell=True)
	
	@script(description='Abrir la tienda oficial de complementos', category='TCA-SystemUtilities', gesture='kb:nvda+x')
	def script_TCAtien(self,gesture):
		webbrowser.open_new_tab('https://addons.nvda-project.org/index.es.html')
	
	@script(description='Abrir monitor de recursos', category='TCA-SystemUtilities')
	def script_TCAmon(self, gesture):
		subprocess.Popen('resmon')
	
	@script(description='Copiar al portapapeles la lista de carpetas y archivos', category='TCA-SystemUtilities', gesture='kb:nvda+shift+l')
	def script_TCAList(self, gesture):
		tsu.T_h(self, 5)
	
	@script(description='Saber la versión de Windows', category='TCA-SystemUtilities')
	def script_TCAver(self, gesture):
		subprocess.Popen('winver')
	
	@script(description='Abrir el administrador de dispositivoss', category='TCA-SystemUtilities')
	def script_TCAdispo(self,gesture):
		subprocess.Popen('devmgmt.msc', shell=True)
	
	@script(description='Abrir Opciones de carpeta', category='TCA-SystemUtilities', gesture='kb:nvda+shift+0')
	def script_TCAcar(self,gesture):
		subprocess.Popen('control folders')
		tones.beep(350,100)
	
	@script(description='Hacer análisis del sistema Con SFC  ', category='TCA-SystemUtilities', gesture='kb:nvda+shift+4')
	def script_TCAsfc(self, gesture):
		tsu.T_h(self, 6)
			
	@script(description='Copiar información de todo el sistema al portapapeles', category='TCA-SystemUtilities', gesture='kb:nvda+shift+6')
	def script_TCAcopy_sys(self, gesture):
		tsu.T_h(self, 4)
		ui.message('información del sistema copiada al portapapeles')
	
	@script(description='Abrir mapa de caracteres', category='TCA-SystemUtilities', gesture='kb:nvda+shift+7')
	def script_TCAchar(self, gesture):
		subprocess.Popen('charmap')
	
	@script(description='Abrir Asistente guardar contraseñas de usuarios', category='TCA-SystemUtilities', gesture='kb:nvda+shift+8')
	def script_TCAa_usu(self, gesture):
		subprocess.Popen('credwiz')

	@script(description='Abrir Optimizar las unidades', category='TCA-SystemUtilities', gesture='kb:nvda+shift+1')
	def script_TCAoptim(self, gesture):
		try:
			os.environ['PROGRAMFILES(X86)']
			with tsu.disable_file_system_redirection():
				subprocess.Popen('dfrgui')	
		except:
			subprocess.Popen('dfrgui')
	
	@script(description='Abrir opciones de voz', category='TCA-SystemUtilities', gesture='kb:nvda+shift+2')
	def script_TCAopvox(self, gesture):
		subprocess.Popen(os.path.join(os.environ['systemroot'], 'system32', 'Speech', 'SpeechUX', 'sapi.cpl'), shell=True)
	
	@script(description='Copiar al portapapeles la información sobre las tarjetas de sonido', category='TCA-SystemUtilities', gesture='kb:nvda+shift+5')
	def script_TCAcopitar(self, gesture):
		tsu.T_h(self, 7)
		
	
	@script(description='Ocultar carpetas', category='TCA-SystemUtilities', gesture='kb:nvda+shift+f4')
	def script_TCAocu(self, gesture):
		tsu.T_h(self, 8)
		
		
	
	@script(description='Mostrar carpetas ocultas', category='TCA-SystemUtilities', gesture='kb:nvda+shift+f5')
	def script_TCAmos(self, gesture):
		tsu.T_h(self, 9)
	
	@script(description='Limpiar disco', category='TCA-SystemUtilities', gesture='kb:nvda+shift+f6')
	def script_TCAclean(self, gesture):
		tsu.T_h(self, 10)
		