# -*- coding: UTF-8 -*-
#TCASystemUtilities, Shut down and restart the PC with Windows classic sound, an Open system Options.
#Autor: Peter Reina<peterrc87@gmail.com><Tecnoconocimiento Accesible  2020>
# This file is covered by the GNU General Public License.

from scriptHandler import script
import api, keyboardHandler, globalPluginHandler, tones, ui, globalVars, addonHandler,winUser, gui
import subprocess, os, sys, threading
import webbrowser, wx
from time import sleep

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from TCA_SU import t_fun as tsu
from TCA_SU import t_menu as tm 
sys.path.remove(os.path.dirname(os.path.abspath(__file__)))

addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):	
	def __init__(self):
		if globalVars.appArgs.secure:
			return
		super(GlobalPlugin, self).__init__()		

		self._MainWindows = None

		#Barra de herramientas.
		tm.create_menu(self)

	def terminate(self):
		try:
			if not self._MainWindows:
				self._MainWindows.Destroy()
		except (AttributeError, RuntimeError):
			pass

	@script(description=_('Apagar el sistema'), category='TCA-SystemUtilities', gesture='kb:nvda+shift+a')
	def script_TCAShut(self,gesture):		
		tsu.T_h(self,1)
	
	@script(description=_('Reinicio del sistema'), category='TCA-SystemUtilities', gesture='kb:nvda+shift+r')
	def script_TCAShutR(self,gesture):
		
		tsu.T_h(self, 2)
	
	@script(description=_('Anular apagado'), category='TCA-SystemUtilities', gesture='kb:nvda+0')
	def script_TCAShutA(self,gesture):
		tsu.T_h(self, 3)
	
	@script(description= _('Abrir opciones de sonido'), category='TCA-SystemUtilities')
	def script_TCAsndOp(self,gesture):
		subprocess.Popen('mmsys.cpl', shell=True)
	
	@script(description=_('Abrir carpeta Roaming'), category='TCA-SystemUtilities', gesture='kb:nvda+9')
	def script_TCARoa(self,gesture):
		os.startfile(os.path.join(os.environ['userprofile'], 'appdata', 'Roaming'))
	
	@script(description=_('Abrir Asistente transferir archivos por Bluetooth'), category='TCA-SystemUtilities', gesture='kb:nvda+shift+9')
	def script_TCAblue(self,gesture):
		subprocess.Popen('fsquirt')
			 
	@script(description=_('Saber la arquitectura del sistema'), category='TCA-SystemUtilities')
	def script_TCAar(self,gesture):
		try:
			os.environ['PROGRAMFILES(X86)']
			version_sys=64
		except:
			version_sys=32
		ui.message(_('Su sistema operativo es de: {} Bits').format(version_sys))
		
	@script(description=_('Abrir el asistente para guardar la contraseña del sistema'), category='TCA-SystemUtilities')
	def script_TCArcon(self,gesture):
		ui.message(_('Abriendo restablecer   contraseñas de Windows'))
		subprocess.Popen('RunDll32.exe keymgr.dll,PRShowSaveWizardExW')
	
	@script(description=_('Copiar al portapapeles la ruta'), category='TCA-SystemUtilities')
	def script_TCAclip(self,gesture):
		tsu.t_obj(self)
		if self.v_obj is not False:
			api.copyToClip('"{}"'.format(self.v_obj))
			ui.message(_('Ruta copiada '))
		else:
			ui.message(_("No se pudo copiar la ruta"))
	@script(description= _('Abrir el administrador de discos'), category='TCA-SystemUtilities')
	def script_TCAdisk(self,gesture):
		subprocess.Popen('diskmgmt.msc', shell=True)
	
	@script(description=_('Abrir la tienda oficial de complementos'), category='TCA-SystemUtilities', gesture='kb:nvda+x')
	def script_TCAtien(self,gesture):
		webbrowser.open_new_tab('https://addons.nvda-project.org/index.es.html')
	
	@script(description=_('Abrir monitor de recursos'), category='TCA-SystemUtilities')
	def script_TCAmon(self, gesture):
		subprocess.Popen('resmon')
	
	@script(description=_('Copiar al portapapeles la lista de carpetas y archivos'), category='TCA-SystemUtilities', gesture='kb:nvda+shift+l')
	def script_TCAList(self, gesture):
		tsu.T_h(self, 5)
	
	@script(description=_('Saber la versión de Windows'), category='TCA-SystemUtilities')
	def script_TCAver(self, gesture):
		subprocess.Popen('winver')
	
	@script(description=_('Abrir el administrador de dispositivoss'), category='TCA-SystemUtilities')
	def script_TCAdispo(self,gesture):
		subprocess.Popen('devmgmt.msc', shell=True)
	
	@script(description=_('Abrir Opciones de carpeta'), category='TCA-SystemUtilities', gesture='kb:nvda+shift+0')
	def script_TCAcar(self,gesture):
		subprocess.Popen('control folders')
		tones.beep(350,100)
	
	@script(description=_('Hacer análisis del sistema Con SFC  '), category='TCA-SystemUtilities')
	def script_TCAsfc(self, gesture):
		tsu.T_h(self, 6)
			
	@script(description=_('Copiar información de todo el sistema al portapapeles'), category='TCA-SystemUtilities')
	def script_TCAcopy_sys(self, gesture):
		tsu.T_h(self, 4)
		ui.message(_('información del sistema copiada al portapapeles'))
	
	@script(description=_('Abrir mapa de caracteres'), category='TCA-SystemUtilities')
	def script_TCAchar(self, gesture):
		subprocess.Popen('charmap')
	
	@script(description=_('Abrir Asistente guardar contraseñas de usuarios'), category='TCA-SystemUtilities', gesture='kb:nvda+shift+8')
	def script_TCAa_usu(self, gesture):
		subprocess.Popen('credwiz')
		
	@script(description=_('Abrir opciones de voz'), category='TCA-SystemUtilities')
	def script_TCAopvox(self, gesture):
		subprocess.Popen(os.path.join(os.environ['systemroot'], 'system32', 'Speech', 'SpeechUX', 'sapi.cpl'), shell=True)
	
	@script(description=_('Copiar al portapapeles la información sobre las tarjetas de sonido'), category='TCA-SystemUtilities')
	def script_TCAcopitar(self, gesture):
		tsu.T_h(self, 7)
	
	@script(description=_('Ocultar carpetas'), category='TCA-SystemUtilities')
	def script_TCAocu(self, gesture):
		tsu.T_h(self, 8)
			
	@script(description=_('Mostrar carpetas ocultas'), category='TCA-SystemUtilities')
	def script_TCAmos(self, gesture):
		tsu.T_h(self, 9)
	
	@script(description=_('Limpiar disco'), category='TCA-SystemUtilities')
	def script_TCAclean(self, gesture):
		tsu.T_h(self, 10)
		
	@script(description=_('Reiniciar Explorador'), category='TCA-SystemUtilities')
	def script_TCAr_explo(self, gesture):
		tsu.T_h(self, 11)
	
	@script(description=_('Abrir Optimizar las unidades'), category='TCA-SystemUtilities')
	def script_TCAoptim(self, gesture):
		tsu.T_h(self, 12)
	
	@script(description=_('Hibernar el sistema'), category='TCA-SystemUtilities')
	def script_TCAhiber(self, gesture):
		tsu.T_h(self, 13)

	
	@script(description=_('Volumen'), category='TCA-SystemUtilities')
	def script_TCAvolu(self, gesture):
		fg = api.getForegroundObject()
		obj = fg.children[5].children[2].children[0].children[7]
		ui.message("el nombre es: {}".format(obj.name))
		
		api.moveMouseToNVDAObject(obj)
		keyboardHandler.KeyboardInputGesture.fromName("space").send()

		os.chdir(tsu.a_path)
		focus = api.getFocusObject()
		focus = focus.parent
		a = '''Red
Acceso a Internet'''
		if focus.name ==a:
			recButton = focus.parent.next.firstChild
			api.moveMouseToNVDAObject(recButton)
			winUser.mouse_event(winUser.MOUSEEVENTF_LEFTDOWN,0,0,None,None)
			winUser.mouse_event(winUser.MOUSEEVENTF_LEFTUP,0,0,None,None)
			#winsound.PlaySound("C:\Windows\Media\Windows Pop-up Blocked.wav", winsound.SND_FILENAME)

	
	@script(description=_('Reparar sistema con Dism'), category='TCA-SystemUtilities')
	def script_TCAa_dism(self, gesture):
		tsu.T_h(self, 14)

	
	@script(description=_('Reiniciar el sistema y entrar en Modo seguro con funciones de red'), category='TCA-SystemUtilities')
	def script_TCA_sh_b(self, gesture):	
		tsu.T_h(self, 15)
	
	@script(description=_('Deshabilitar el Modo seguro y reiniciar el sistema'), category='TCA-SystemUtilities')
	def script_TCA_sh_nor(self, gesture):	
		tsu.T_h(self, 16)
	
	@script(description=_('Abrir Mezclador de volumen'), category='TCA-SystemUtilities')
	def script_TCAa_mvol(self, gesture):
		subprocess.Popen('sndvol.exe', shell = True)

	
	@script(description=_('Suspender el sistema'), category='TCA-SystemUtilities')
	def script_TCA_susp(self, gesture):	
		tsu.T_h(self, 17)
	
	@script(description=_('Abrir Restablecer éste PC'), category='TCA-SystemUtilities')
	def script_TCA_resPC(self, gesture):
		tsu.T_h(self, 18)

	
	@script(description=_('Copiar al portapepeles la lista de archivos en cuarentena'), category='TCA-SystemUtilities')
	def script_TCA_qclip(self, gesture):
		tsu.T_h(self, 19)

	
	@script(description=_('Análisis rápido'), category='TCA-SystemUtilities')
	def script_TCA_scan_r(self, gesture):
		tsu.T_h(self, 20)

	
	@script(description=_('Análisis completo'), category='TCA-SystemUtilities')
	def script_TCA_scan_f(self, gesture):
		tsu.T_h(self, 21)

	
	@script(description=_('Análisis del sector de arranque'), category='TCA-SystemUtilities')
	def script_TCA_scan_sc_boot(self, gesture):
		tsu.T_h(self, 22)


	@script(description=_('Activar escanéo de archivos comprimidos'), category='TCA-SystemUtilities')
	def script_TCA_sc_f(self, gesture):
		tsu.T_h(self, 23)

	@script(description=_('Desactivar escanéo de archivos comprimidos'), category='TCA-SystemUtilities')
	def script_TCA_scn_nf(self, gesture):
		tsu.T_h(self, 24)
	
	@script(description=_('Desactivar la Webcam'), category='TCA-SystemUtilities')
	def script_TCA_webcam_d(self, gesture):
		tsu.T_h(self, 25)

	
	@script(description=_('Activar la Webcam'), category='TCA-SystemUtilities')
	def script_TCA_webcam_ac(self, gesture):
		tsu.T_h(self, 26)
	
	@script(description=_('Reiniciar el sistema y entrar en la BIOS-UEFI'), category='TCA-SystemUtilities')
	def script_TCA_bios(self, gesture):
		tsu.T_h(self, 27)
	
	@script(description=_('Limpiar caché DNS'), category='TCA-SystemUtilities')
	def script_TCA_cache(self, gesture):
		tsu.T_h(self, 28)

	
	@script(description=_('Desactivar el espacio reservado'), category='TCA-SystemUtilities')
	def script_TCA_des_space(self, gesture):
		tsu.T_h(self, 29)

	
	@script(description=_('Activar el espacio reservado'), category='TCA-SystemUtilities')
	def script_TCA_ac_space(self, gesture):
		tsu.T_h(self, 30)
	
	@script(description=_('AbrircConsola CMD en la ruta actual'), category='TCA-SystemUtilities')
	def script_TCA_cmd(self, gesture):
		tsu.T_h(self, 31)
	
	@script(description=_('AbrircConsola CMD Administrador'), category='TCA-SystemUtilities')
	def script_TCA_cmd_ad(self, gesture):
		tsu.T_h(self, 32)
	
	@script(description=_('Limpiar configuración guardada para ejecutarse en pantallas seguras'), category='TCA-SystemUtilities')
	def script_TCA_scclean(self,gesture):
		tsu.T_h(self, 33)
	
	@script(description=_('Borrar el portapapeles y su historial'), category='TCA-SystemUtilities')
	def script_TCA_clean_clip(self,gesture):
		tsu.T_h(self, 34)