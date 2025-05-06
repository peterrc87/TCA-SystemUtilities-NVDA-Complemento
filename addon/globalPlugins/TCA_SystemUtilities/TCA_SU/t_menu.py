﻿# -*- coding: UTF-8 -*-
#TCASystemUtilities, Shut down and restart the PC with Windows classic sound, an Open system Options.
#Autor: Peter Reina<peterrc87@gmail.com><Tecnoconocimiento Accesible  2020>
# This file is covered by the GNU General Public License.
import gui,addonHandler
import wx
addonHandler.initTranslation()

def create_menu(self):
	# Definimos el menu general de wx y el de NVDA.
	self.menuGeneral = wx.Menu()
	self.tools_menu = gui.mainFrame.sysTrayIcon.toolsMenu

	# Submenú Apagado del sistema
	self.menuApagar = wx.Menu()
	t_sh_s = self.menuApagar.Append(-1, _("Apagar"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAShut, t_sh_s)
	t_sh_bios = self.menuApagar.Append(-1, _("Entrar a la BIOS-UEFI"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_bios, t_sh_bios)
	t_sh_h = self.menuApagar.Append(-1, _("Hibernar"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAhiber, t_sh_h)
	t_sh_r = self.menuApagar.Append(-1, _("Reiniciar"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAShutR, t_sh_r)
	t_sh_b = self.menuApagar.Append(-1, _("Reiniciar y entrar en Modo seguro con funciones de red"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_sh_b, t_sh_b)
	t_sh_n = self.menuApagar.Append(-1, _("Reiniciar en Modo normal"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_sh_nor, t_sh_n)
	t_sh_susp = self.menuApagar.Append(-1, _("Suspender"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_susp, t_sh_susp)
	self.subApagado = self.menuGeneral.AppendSubMenu(self.menuApagar, _("Apagado del sistema"))

	# Submenú Explorador y Procesos
	self.menuExplorador = wx.Menu()
	t_clean_clip = self.menuExplorador.Append(-1, _('Borrar el portapapeles'))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_clean_clip, t_clean_clip)
	t_close =self.menuExplorador.Append(-1, _("Cerrar todas las aplicaciones")) 
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_close_all, t_close)

	t_des_explo = self.menuExplorador.Append(-1, _("Desbloquear explorador de Windows"))  
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_des_explo, t_des_explo)
	t_process = self.menuExplorador.Append(-1, _('Matar procesos'))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_close_app2, t_process) 

	t_monitor = self.menuExplorador.Append(-1, _("Monitor de recursos"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAmon, t_monitor)
	
	t_rExplo = self.menuExplorador.Append(-1, _("Reiniciar Explorador"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAr_explo, t_rExplo)
	self.subExplorador = self.menuGeneral.AppendSubMenu(self.menuExplorador, _("Explorador y Procesos"))

	# Submenú Reparación y optimización
	self.menuReparacion = wx.Menu()
	t_ac_spa = self.menuReparacion.Append(-1, _("Activar almacenamiento reservado"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_ac_space, t_ac_spa)
	t_des_spa = self.menuReparacion.Append(-1, _("Desactivar almacenamiento reservado"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_des_space, t_des_spa)
	#version 1.0
	t_hight_pw = self.menuReparacion.Append(-1, _('Activar el plan alto rendimiento'))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU,self.script_TCA_hihgt_pw, t_hight_pw)
	t_balanced_pw = self.menuReparacion.Append(-1, _('Activar el plan equilibrado'))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU,self.script_TCA_balanced_pw, t_balanced_pw)
	
	t_sfc = self.menuReparacion.Append(-1, _("Análisis del sistema Con SFC    "))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAsfc, t_sfc)
	t_cache = self.menuReparacion.Append(-1, _("Limpiar caché DNS"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_cache, t_cache)
	t_clean_sc = self.menuReparacion.Append(-1, _('Limpiar configuración guardada en pantallas seguras'))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_scclean, t_clean_sc)
	t_clDisk = self.menuReparacion.Append(-1, _("Limpiar disco"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAclean, t_clDisk)
	t_opti = self.menuReparacion.Append(-1, _("Optimizar las unidades"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAoptim, t_opti)
	t_resPC = self.menuReparacion.Append(-1, _("Restablecer PC"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_resPC, t_resPC)
	t_dism = self.menuReparacion.Append(-1, _("Reparar sistema con Dism"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAa_dism, t_dism)
	self.subReparacion = self.menuGeneral.AppendSubMenu(self.menuReparacion, _("Reparación y optimización"))
	# Submenú Seguridad de Windows
	self.menuSeguridad = wx.Menu()
	t_uac_on =self.menuSeguridad.Append(-1, _('Activar el control de cuentas de usuario (uac)'))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAuac_on, t_uac_on)
	
	t_ab = self.menuSeguridad.Append(-1, _("Analizar arranque del sistema"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_scan_sc_boot, t_ab)
	t_af = self.menuSeguridad.Append(-1, _("Análisis completo"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_scan_f, t_af)
	t_ar = self.menuSeguridad.Append(-1, _("análisis rápido"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_scan_r, t_ar)
	t_ac = self.menuSeguridad.Append(-1, _("Escanear archivos comprimidos"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_sc_f, t_ac)
	t_dc = self.menuSeguridad.Append(-1, _("No escanear archivos comprimidos"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_scn_nf, t_dc)
	t_uac_off =self.menuSeguridad.Append(-1, _('Desactivar el control de cuentas de usuario (uac)'))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAuac_off, t_uac_off)

	t_lq = self.menuSeguridad.Append(-1, _("Listado de archivos en cuarentena al portapapeles"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_qclip, t_lq)
	self.subSeguridad = self.menuGeneral.AppendSubMenu(self.menuSeguridad, _("Seguridad de Windows"))
	
	# Submenú Voz y multimedia
	self.menuMultimedia = wx.Menu()
	t_wcam_ac = self.menuMultimedia.Append(-1, _("Activar Webcam"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_webcam_ac, t_wcam_ac)
	t_wcam_d = self.menuMultimedia.Append(-1, _("Desactivar Webcam"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_webcam_d, t_wcam_d)
	t_mvol = self.menuMultimedia.Append(-1, _("Mezclador de volumen"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAa_mvol, t_mvol)
	t_soundOps = self.menuMultimedia.Append(-1, _("Opciones de sonido"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAsndOp, t_soundOps)
	t_vo =self.menuMultimedia.Append(-1, _("Opciones de voz"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAopvox, t_vo)
	self.subMultimedia = self.menuGeneral.AppendSubMenu(self.menuMultimedia, _("Voz y multimedia"))
	# Submenú Utilidades del sistema
	self.menuUtilidades = wx.Menu()
	t_passUsu = self.menuUtilidades.Append(-1, _("Asistente guardar contraseñas de usuarios"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAa_usu, t_passUsu)
	t_blueTooth = self.menuUtilidades.Append(-1, _("Asistente transferir archivos por Bluetooth"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAblue, t_blueTooth)
	t_roa = self.menuUtilidades.Append(-1, _("Carpeta Roaming"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCARoa, t_roa)
	t_adDisk = self.menuUtilidades. Append(-1, _("administrador de discos"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAdisk, t_adDisk)
	t_adDev = self.menuUtilidades.Append(-1, _("administrador de dispositivos"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAdispo, t_adDev)
	t_savePass = self.menuUtilidades.Append(-1, _("asistente para guardar la contraseña del sistema"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCArcon, t_savePass)
	t_char = self.menuUtilidades.Append(-1, _("mapa de caracteres"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAchar, t_char)
	t_foldOps = self.menuUtilidades.Append(-1, _("Opciones de carpeta"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAcar, t_foldOps)
	t_wVer = self.menuUtilidades.Append(-1, _("Saber la versión de Windows"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAver, t_wVer)
	self.subUtilidades = self.menuGeneral.AppendSubMenu(self.menuUtilidades, _("Utilidades del sistema"))
	self.menuPrincipal = self.tools_menu.AppendSubMenu(self.menuGeneral, "&TCA_SystemUtilities")
	return self.tools_menu, self.menuPrincipal
