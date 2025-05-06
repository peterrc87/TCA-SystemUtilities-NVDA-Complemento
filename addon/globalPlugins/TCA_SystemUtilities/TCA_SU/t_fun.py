#!/usr/bin/python
# -*- coding: utf-8 -*-
#TCASystemUtilities, Shut down and restart the PC with Windows classic sound, an Open system Options.
#Autor: Peter Reina<peterrc87@gmail.com><Tecnoconocimiento Accesible  2020>
# This file is covered by the GNU General Public License.

import ui, api, keyboardHandler, globalVars, addonHandler, shellapi, tones
from time import sleep
import os, subprocess, platform, ctypes, winsound, sys  
from threading import Thread
import wx
from comtypes.client import CreateObject as COMCreate
from .path_func import z_path, t_obj, fs_path
a_path = os.getcwd()
w_pt = os.path.join(os.environ['programfiles'].replace('Program Files (x86)', 'Program Files'), 'Windows Defender')

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
			
#Decoradora para redirección.
def rdt(fn):
	def d_rdt():
		try:
			os.environ['PROGRAMFILES(X86)']
			with disable_file_system_redirection():
				fn()
				os.chdir(a_path)
				tones.beep(950,50)
		except:
			fn()
			os.chdir(a_path)
			tones.beep(950,50)
	return d_rdt

#Clase para hilos.
class T_h(Thread):
	def __init__(self, frame, op):
		super(T_h, self).__init__()
		self.frame = frame
		self.op = op
		self.daemon = True
		self.start()
	
	def run(self):
		@rdt
		def TCAShut():		
			ui.message(_('Apagando el Pc.'))
			winsound.PlaySound('C:\Windows\Media\Windows Shutdown.wav',winsound.SND_FILENAME)
			shellapi.ShellExecute(None, 'runas', 'cmd.exe', '/c' + 'shutdown -s -t 3', None, 10)
			
		@rdt
		def TCAShutR():
			ui.message(_('Reiniciando el PC.'))
			winsound.PlaySound('C:\Windows\Media\Windows Shutdown.wav',winsound.SND_FILENAME)
			shellapi.ShellExecute(None, 'runas', 'cmd.exe', '/c' + 'shutdown -r -t 3', None, 10)
	
		def TCAShutA():
			ui.message(_('anulando el apagado o reinicio del pc.'))
			shellapi.ShellExecute(None, 'runas', 'cmd.exe', '/c' + 'shutdown -a', None, 10)


		def TCAcopy_sys():
			subprocess.Popen('Systeminfo | clip', shell=True)
			
		def TCAList():
			#t_obj(self)
			fs_path(self)
			if self.path  is not False:
				os.chdir(self.path    )
				subprocess.Popen('dir /b|clip', shell=True)
				os.chdir(a_path)
				ui.message(_('Copiada la lista al portapapeles'))
			else:
				ui.message(_('No se pudo copiar la lista al portapapeles'))
		
		@rdt
		def TCAsfc():
			shellapi.ShellExecute(None, 'runas', 'cmd.exe', '/c' + 'sfc' + '/scannow' + '&pause', None, 10)																
			
		def TCAcopitar():
			lt=['powershell', 'Get-WmiObject Win32_SoundDevice |clip']
			subprocess.run(lt, shell=True)
			ui.message(_('Copiada la info del sonido al portapapeles'))
			
		@rdt
		def ocu():
			fs_path(self)
			if self.path  is not False:

				d=os.path.dirname(self.path)
				b=os.path.basename(self.v_path)
				os.chdir(d)
				shellapi.ShellExecute(None, None, 'cmd.exe', '/c' + r'attrib +s +h "{}"'.format(b), None, 0)	
				sleep(0.5)
				keyboardHandler.KeyboardInputGesture.fromName("alt+f4").send()
				os.startfile(d)
				tones.beep(900,50)
				os.chdir(a_path)
			else:
				ui.message(_('No fue posible ocultar los elementos'))

		@rdt
		def mos():
			fs_path(self)
			if self.path  is not False:

				os.chdir(self.v_path)
				shellapi.ShellExecute(None, None, 'cmd.exe','/c' + r'attrib /d -s -h', None, 0)
				sleep(0.5)
				os.chdir(a_path)
			else:
				ui.message(_('no se pudieron mostrar los archivos'))
			
		def clean():
			if os.path.isfile(os.path.join(globalVars.appArgs.configPath,"tsu.ini")):
				pass
			else:
				dlg=wx.RichMessageDialog(None, _("Si es la primera vez que ejecuta ésta acción.\n es necesario crear un perfil de limpieza, solo debe hacerlo una vez.\n puede pulsar en Crear perfil también si desea modificar uno existente, o puede marcar  la casilla para no volver a mostrar éste mensaje."), style=wx.CANCEL) 
				dlg.SetOKLabel(_("Crear perfil"))
				dlg.ShowCheckBox(_("No volver  a mostrar este mensaje"))		
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
							shellapi.ShellExecute(None, 'runas','cmd.exe','/c' + 'CLEANMGR /sageset:1', None, None)	
							
					except:
						shellapi.ShellExecute(None, 'runas','cmd.exe','/c' + 'CLEANMGR /sageset:1', None, None)		
				else:
					dlg.Destroy()
			
			try:
				os.environ['PROGRAMFILES(X86)']
				with disable_file_system_redirection():  
					shellapi.ShellExecute(None, 'runas','cmd.exe','/c' + 'CLEANMGR /sagerun:1', None, None)	
					
			except:
				shellapi.ShellExecute(None, 'runas','cmd.exe','/c' + 'CLEANMGR /sagerun:1', None, None)	
				
		@rdt
		def r_explo():
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + 'taskkill /f /im explorer.exe' + '& start explorer', None, 10)	
			
		@rdt
		def optim():
			shellapi.ShellExecute(None, 'runas', 'cmd.exe', '/c' + 'dfrgui', None, 0)	

		def iver():
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + 'shutdown /h', None, 10)		
		
		@rdt
		def a_dism():
			shellapi.ShellExecute(None, 'runas', 'cmd.exe', '/c' + 'DISM /online /cleanup-image /RestoreHealth' + '&pause', None, 10)
	
		@rdt
		def sh_b():
			dlg = wx.MessageDialog(None, _("Está a punto de reiniciar el sistema, y activar el modo Seguro con funciones de red.\n En éste modo los sistemas Windows anteriores al 10, puede que no tengan sonidos, por ende, el lector de pantalla no tendrá soporte de voz.\n Deberá deshabilitar este modo desde las configuraciones del sistema msconfig, o haciendo uso de TCA SystemUtilities en el apartado: apagado del sistema.\n ¿Está seguro que desea continuar?"),_("Atención activación del Modo seguro!"), wx.YES_NO|wx.ICON_QUESTION) 
			rp = dlg.ShowModal()
			if rp == wx.ID_YES:
				shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'bcdedit /set {default} safeboot network',None, 10)
				shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'bcdedit /set {default} safebootalternateshell yes', None, 10)

				ui.message(_("Modo seguro activado, se va a reiniciar el Pc"))
				winsound.PlaySound('C:\Windows\Media\Windows Shutdown.wav',winsound.SND_FILENAME)
				shellapi.ShellExecute(None, 'runas', 'cmd.exe', '/c' + 'shutdown -r -t 3', None, 10)
			else:
				dlg.Destroy()

		@rdt
		def sh_nor():
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'bcdedit /deletevalue {default} safeboot',None, 10)
			ui.message(_("Modo normal, reiniciando el Pc"))
			winsound.PlaySound('C:\Windows\Media\Windows Shutdown.wav',winsound.SND_FILENAME)
			shellapi.ShellExecute(None, 'runas', 'cmd.exe', '/c' + 'shutdown -r -t 3', None, 10)
		
		def susp():
			ui.message(_("Suspendiendo el sistema"))
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' +'Rundll32.exe powrprof.dll, SetSuspendState', None, 10)				

		@rdt
		def resPC():
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' +'powershell start ms-settings:recovery', None, 10)								

		@rdt
		def qclip():
			
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'"{}\MpCmdRun.exe" -Restore -ListAll'.format(w_pt) + '|clip', None, 10)																
		
		
		@rdt
		def scan_r():
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'"{}\MpCmdRun.exe" -scan -scantype 1'.format(w_pt), None, 10)																																

		@rdt
		def scan_f():
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'"{}\MpCmdRun.exe" -scan -scantype 2'.format(w_pt), None, 10)																																																				
		@rdt
		def sc_boot():
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'"{}\MpCmdRun.exe" -scan -bootsectorscan'.format(w_pt), None, 10)
		
		@rdt
		def sc_f():
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'powershell Set-MpPreference -DisableArchiveScanning 0', None, 10)
			sleep(1)
			ui.message(_('Se activó el escanéo de archivos comprimidos'))
		
		@rdt
		def sc_nf():
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'powershell Set-MpPreference -DisableArchiveScanning 1', None, 10)
			sleep(1)
			ui.message(_('Se desactivó el escanéo de archivos comprimidos'))
		
		def webcam_d():
			
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'powershell Disable-PnpDevice -InstanceId (Get-PnpDevice -FriendlyName *webcam*  -Status OK).InstanceId', None, 10)
			sleep(0.1)
			keyboardHandler.KeyboardInputGesture.fromName("enter").send()
			sleep(2)
			ui.message(_('Se desactivó la Webcam'))
				
		
		def webcam_ac():
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'powershell Enable-PnpDevice -InstanceId (Get-PnpDevice -FriendlyName *webcam* -Status Error).InstanceId', None, 10)
			sleep(0.1)
			keyboardHandler.KeyboardInputGesture.fromName("enter").send()
			sleep(2)
			ui.message(_('Se activó la Webcam'))


		def bios():
			dlg = wx.MessageDialog(None, _("Está a punto de activar entrar a la BIOS-UEFI\n El PC se va a reiniciar en unos segundos. \n Recuerda que en la BIOS-UEFI no podrás utilizar un lector de pantalla, tendrás que pedir ayuda visual.\n ¿está seguro que desea continuar?"), _("¿Atención Se intentará activar la entrada a la BIOS-UEFI!"), wx.YES_NO|wx.ICON_QUESTION) 
			rp = dlg.ShowModal()
			if rp == wx.ID_YES:
				shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + 'shutdown /r /fw', None, 10)				
			else:
				dlg.Destroy()
		

		def cache():
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + 'ipconfig / flushDNS', None, 10)
			sleep(0.5)
			ui.message(_("Se limpió la Caché DNS "))

		
		@rdt
		def des_space():
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + 'DISM.exe /Online /Set-ReservedStorageState /State:Disabled', None, 10)
			sleep(0.5)
			ui.message(_("Se desactivó el espacio reservado"))

		@rdt
		def ac_space():
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + 'DISM.exe /Online /Set-ReservedStorageState /State:Enabled', None, 10)
			sleep(0.5)
			ui.message(_("Se activó el espacio reservado"))
		
		@rdt
		def cmd():
			obj = api.getForegroundObject()
			if not obj or not obj.appModule or obj.appModule.appName != 'explorer':
				ui.message(_('Active una ventana del explorador antes de abrir CMD'))
				return

			try:
				if not hasattr(self, '_shell'):
					self._shell = COMCreate('shell.application')
				for window in self._shell.Windows():
					if window.hwnd == obj.windowHandle:
						target_path = str(window.Document.FocusedItem.path)
						break
				else:
					target_path = None

				if not target_path:
					windows = self.get_selected_files_explorer_ps()
					if windows and str(obj.windowHandle) in windows:
						target_path = windows[str(obj.windowHandle)]

				if not target_path:
					desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
					target_path = desktop_path + '\\' + api.getDesktopObject().objectWithFocus().name

				if not os.path.exists(target_path):
					ui.message(_('La ruta seleccionada no existe'))
					return

				if os.path.isdir(target_path):
					target_path = os.path.dirname(target_path)
				else:
					target_path = os.path.dirname(os.path.abspath(target_path))    

				shellapi.ShellExecute(
					None,
					'open',
					'cmd.exe',
					None,
					os.path.abspath(target_path),
					1
				)
			except Exception as e:
				ui.message(_('Error al abrir CMD: {}').format(str(e)))

		@rdt
		def cmd_ad():
			fs_path(self)
			if self.path is not False:
				try:
					os.chdir('{}'.format(self.path))
				except:
					ui.message(_('No se pudo obtener la ruta para el CMD'))
					return
				else: #anidado al try.
					shellapi.ShellExecute(None, 'runas', 'cmd.exe','{}:'.format(os.path.abspath(self.path)), None, 10)
			else:
				ui.message("no se pudo ejecutar el cmd")
		
		def delete_config():
			os.chdir("C:/Program Files (x86)/NVDA/systemConfig")
			pt_ac = os.getcwd()
			paths_sc = (pt_ac,os.path.join(pt_ac, 'addons'), os.path.join(pt_ac, 'profiles'))
			if len(os.listdir('addons')) > 0:
				dlg = wx.MessageDialog(None, _('Este proceso eliminará todos los complementos y configuraciones que están en pantallas seguras.\n Es necesario que se reinicie el explorador de Windows, se deben cerrar todas las ventanas del explorador.\n Si tiene activado el uac (Control de cuentas de usuario), es probable que deba darle varias veces permisos para continuar.\n ¿Está seguro que desea continuar?'), _('Atención borrando addons y configuraciones de pantallas seguras'), wx.YES_NO|wx.ICON_QUESTION)
				rp = dlg.ShowModal()
				if rp == wx.ID_YES:
					for path in paths_sc:
						os.chdir(path)
				
						for folder in os.listdir():
							if os.path.isdir(folder):
								if folder == 'addons':
									continue
								elif folder == 'profiles':
									continue
								elif folder == 'speechDicts':
									continue
					
								shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'rd /s /q "{}\{}"'.format(path, folder), None, 0)
							
							elif os.path.isfile(folder):
								shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'del /f /a /q "{}\{}"'.format(path,folder), None, 0)
				
					os.chdir(a_path)
					tones.beep(950,50)
					sleep(1)
					ui.message(_("Se limpió la configuración en pantallas seguras  "))
					r_explo()	
				else:
					dlg.Destroy()
			else:
				ui.message(_("No existen configuraciones guardadas en pantallas seguras"))

		@rdt
		def clean_clip():
			try:
				shellapi.ShellExecute(None, 'runas','cmd.exe','/c' +r'powershell Restart-Service -Name "cbdhsvc*" -force', None, 0)				
			except:
				ui.message(_('no hay nada en el historial del portapapeles'))
			try:
				shellapi.ShellExecute(None, 'runas','cmd.exe','/c' + 'echo off | clip', None, 0)				
			except:
				ui.message(_('No fue posible eliminar el portapapeles'))
			
			ui.message(_('Se limpió correctamente el portapapeles'))

		def z_path2():
			z_path(self)
			
		@rdt
		def des_explo():
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + 'taskkill.exe /f /fi "status eq Not Responding"', None, 10)		

		@rdt
		def close_all():
			u_path = os.environ['userprofile']
			u_name = u_path.split('\\')
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + 'taskkill /fi "USERNAME eq {}" /f'.format(u_name[-1]), None, 10)				

		def roaming():		
			path = os.path.join(os.environ['userprofile'], 'appdata', 'Roaming')
			shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + 'start %windir%\explorer.exe {}'.format(path), None, 10)								
		
		@rdt
		def uac_off():
			try:
				shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'powershell reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System /v ConsentPromptBehaviorAdmin /t REG_DWORD /d 0 /f', None, 10)
				shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'powershell reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f', None, 10)
			except Exception as e:
				ui.message(_('No fue posible desactivar el control de cuentas de usuario\n Error: {}').format(e))
			else:
				dlg = wx.MessageDialog(None, _('Se ha desactivado el control de cuentas de usuario (uac).\n Es necesario reiniciar el sistema para que surtan los cambios. \n ¿Desea hacerlo ahora?'),_('Atención !Reinicio necesario'), wx.YES_NO|wx.ICON_QUESTION) 
				rp = dlg.ShowModal()
				if rp == wx.ID_YES:
					winsound.PlaySound('C:\Windows\Media\Windows Shutdown.wav',winsound.SND_FILENAME)
					shellapi.ShellExecute(None, 'runas', 'cmd.exe', '/c' + 'shutdown -r -t 3', None, 10)
				else:
					dlg.Destroy()
						
		@rdt
		def uac_on():
			try:
				shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'powershell reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System /v ConsentPromptBehaviorAdmin /t REG_DWORD /d 2 /f', None, 10)
				shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + r'powershell reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f', None, 10)
			except Exception as e:
				ui.message(_('No fue posible activar el control de cuentas de usuario\n Error: {}').format(e))
			else:
				dlg = wx.MessageDialog(None, _('Se ha activado el control de cuentas de usuario (uac).\n Es necesario reiniciar el sistema para que surtan los cambios. \n ¿Desea hacerlo ahora?'),_('Atención !Reinicio necesario'), wx.YES_NO|wx.ICON_QUESTION) 
				rp = dlg.ShowModal()
				if rp == wx.ID_YES:
					winsound.PlaySound('C:\Windows\Media\Windows Shutdown.wav',winsound.SND_FILENAME)
					shellapi.ShellExecute(None, 'runas', 'cmd.exe', '/c' + 'shutdown -r -t 3', None, 10)
				else:
					dlg.Destroy()
				
		@rdt
		def close_app():
			dlg = wx.TextEntryDialog(None, _('Escriba aquí el nombre de la aplicación'), _('Ingrese el nombre:'))
			dlg.SetWindowStyle(dlg.GetWindowStyle() | wx.STAY_ON_TOP)
			rp = dlg.ShowModal()
			if rp == wx.ID_OK:
				app_name  = dlg.GetValue()					
				if app_name != '':
					try:
						shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + 'taskkill /f /im {}*'.format(app_name), None, 10)		
					except Exception as e:
						ui.message(_('No fue posible termninar el proceso {}\n Ocurrió el error: {}').format(app_name, e))
						sleep(2)
					else:
						ui.message(_('Se terminaron todos los procesos de: {} de forma correcta').format(app_name))
						sleep(2)
				else:
					ui.message(_('Debe escribir el nombre de una aplicación'))
					sleep(2)

				dlg.Destroy()
			else:
				dlg.Destroy()
		
		#versión 0.10
		@rdt
		def hight_pw():
			try:
				shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + 'powercfg -s SCHEME_MIN', None, 10)				
			except Exception as e:
				ui.message(_('No fue posible activar el plan alto rendimiento. Ocurrió el error: {}'.format(e)))
				sleep(3)
			else:
				ui.message(_('Plan alto rendimiento activado'))
				sleep(3)
		
		@rdt
		def balanced_pw():
			try:
				shellapi.ShellExecute(None, 'runas','cmd.exe', '/c' + 'powercfg -s SCHEME_BALANCED', None, 10)				
			except Exception as e:
				ui.message(_('No fue posible activar el plan Equilibrado. Ocurrió el error: {}'.format(e)))
				sleep(3)
			else:
				ui.message(_('Plan Equilibradoactivado'))
				sleep(3)


		
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
		elif self.op == 11:
			wx.CallAfter(r_explo)
		elif self.op == 12:
			wx.CallAfter(optim)
		elif self.op == 13:
			wx.CallAfter(iver)
		elif self.op == 14:
			wx.CallAfter(a_dism)
		elif self.op == 15:
			wx.CallAfter(sh_b)
		elif self.op == 16:
			wx.CallAfter(sh_nor)
		elif self.op == 17:
			wx.CallAfter(susp)
		elif self.op == 18:
			wx.CallAfter(resPC)
		elif self.op == 19:
			wx.CallAfter(qclip)
		elif self.op == 20:
			wx.CallAfter(scan_r)
		elif self.op == 21:
			wx.CallAfter(scan_f)
		elif self.op == 22:
			wx.CallAfter(sc_boot)
		elif self.op == 23:
			wx.CallAfter(sc_f)
		elif self.op == 24:
			wx.CallAfter(sc_nf)
		elif self.op == 25:
			wx.CallAfter(webcam_d)
		elif self.op == 26:
			wx.CallAfter(webcam_ac)
		elif self.op == 27:
			wx.CallAfter(bios)
		elif self.op == 28:
			wx.CallAfter(cache)
		elif self.op == 29:
			wx.CallAfter(des_space)
		elif self.op == 30:
			wx.CallAfter(ac_space)
		elif self.op == 31:
			wx.CallAfter(cmd)
		elif self.op == 32:
			wx.CallAfter(cmd_ad)
		elif self.op == 33:
			wx.CallAfter(delete_config)
		elif self.op == 34:
			wx.CallAfter(clean_clip)
		
		elif self.op == 36:
			wx.CallAfter(des_explo)
		elif self.op == 37:
			wx.CallAfter(close_all)
		elif self.op == 38:
			wx.CallAfter(roaming)
		elif self.op == 39:
			wx.CallAfter(uac_off)
		elif self.op == 40:
			wx.CallAfter(uac_on)
		elif self.op == 41:
			wx.CallAfter(close_app)
		elif self.op == 42:
			wx.CallAfter(hight_pw)
		elif self.op == 43:
			wx.CallAfter(balanced_pw)