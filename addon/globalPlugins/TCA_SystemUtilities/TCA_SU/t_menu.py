# -*- coding: UTF-8 -*-
#TCASystemUtilities, Shut down and restart the PC with Windows classic sound, an Open system Options.
#Autor: Peter Reina<peterrc87@gmail.com><Tecnoconocimiento Accesible  2020>
# This file is covered by the GNU General Public License.
import gui,addonHandler
import wx
addonHandler.initTranslation()
def create_menu(self):
	#Barra de herramientas.
	self.menu = wx.Menu()	
	a_sys = wx.Menu()
	e_sys = wx.Menu()
	u_sys = wx.Menu()
	r_sys = wx.Menu()
	s_sys = wx.Menu()
	ws_sys = wx.Menu()
	t_menu = gui.mainFrame.sysTrayIcon.toolsMenu
	#Menú Apagado del sisstema.
	t_sh_s = a_sys.Append(-1, _("Apagar"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAShut, t_sh_s)
	t_sh_bios = a_sys.Append(-1, _("Entrar a la BIOS-UEFI"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_bios, t_sh_bios)

	t_sh_h = a_sys.Append(-1, _("Hibernar"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAhiber, t_sh_h)
	t_sh_r = a_sys.Append(-1, _("Reiniciar"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAShutR, t_sh_r)
	t_sh_b = a_sys.Append(-1, _("Reiniciar y entrar en Modo seguro con funciones de red"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_sh_b, t_sh_b)
	t_sh_n = a_sys.Append(-1, _("Reiniciar en Modo normal"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_sh_nor, t_sh_n)
	t_sh_susp = a_sys.Append(-1, _("Suspender"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_susp, t_sh_susp)

	#Menú utilidades del sistema.
	t_wcam_ac = u_sys.Append(-1, _("Activar Webcam"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_webcam_ac, t_wcam_ac)

	t_wcam_d = u_sys.Append(-1, _("Desactivar Webcam"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_webcam_d, t_wcam_d)
	
	t_passUsu = u_sys.Append(-1, _("Asistente guardar contraseñas de usuarios"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAa_usu, t_passUsu)
	t_blueTooth = u_sys.Append(-1, _("Asistente transferir archivos por Bluetooth"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAblue, t_blueTooth)
	t_roa = u_sys.Append(-1, _("Carpeta Roaming"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCARoa, t_roa)
	t_adDisk = u_sys. Append(-1, _("administrador de discos"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAdisk, t_adDisk)
	t_adDev = u_sys.Append(-1, _("administrador de dispositivoss"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAdispo, t_adDev)
	t_savePass = u_sys.Append(-1, _("asistente para guardar la contraseña del sistema"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCArcon, t_savePass)
	t_char = u_sys.Append(-1, _("mapa de caracteres"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAchar, t_char)
	t_monitor = e_sys.Append(-1, _("Monitor de recursos"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAmon, t_monitor)
	t_foldOps = u_sys.Append(-1, _("Opciones de carpeta"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAcar, t_foldOps)
	
	#Menú Voz y sonido.
	t_mvol = s_sys.Append(-1, _("Mezclador de volumen"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAa_mvol, t_mvol)
	t_soundOps = s_sys.Append(-1, _("Opciones de sonido"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAsndOp, t_soundOps)
	t_vo =s_sys.Append(-1, _("Opciones de voz"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAopvox, t_vo)
	#Menú Reparación del sistema.
	
	t_sfc = r_sys.Append(-1, _("Análisis del sistema Con SFC    "))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAsfc, t_sfc)
	t_cache = r_sys.Append(-1, _("Limpiar caché DNS"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_cache, t_cache)

	t_clDisk = r_sys.Append(-1, _("Limpiar disco"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAclean, t_clDisk)
	t_opti = r_sys.Append(-1, _("Optimizar las unidades"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAoptim, t_opti)

	t_resPC = r_sys.Append(-1, _("Restablecer PC"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_resPC, t_resPC)
	#Menú Explorador y procesos.
	t_rExplo = e_sys.Append(-1, _("Reiniciar Explorador"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAr_explo, t_rExplo)
	t_dism = r_sys.Append(-1, _("Reparar sistema con Dism"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAa_dism, t_dism)
	t_wVer = u_sys.Append(-1, _("Saber la versión de Windows"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAver, t_wVer)
	#Menú: Seguridad de Windows.
	t_ab = ws_sys.Append(-1, _("Analizar arranque del sistema"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_scan_sc_boot, t_ab)
	t_af = ws_sys.Append(-1, _("Análisis completo"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_scan_f, t_af)

	t_ar = ws_sys.Append(-1, _("análisis rápido"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_scan_r, t_ar)

	t_ac = ws_sys.Append(-1, _("Escanear archivos comprimidos"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_sc_f, t_ac)

	t_dc = ws_sys.Append(-1, _("No escanear archivos comprimidos"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_scn_nf, t_dc)
	t_lq = ws_sys.Append(-1, _("Listado de archivos en cuarentena al portapapeles"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCA_qclip, t_lq)

	self.menu.AppendSubMenu(a_sys, _("Apagado del sistema"))
	self.menu.AppendSubMenu(e_sys, _("Explorador y Procesos"))
	self.menu.AppendSubMenu(r_sys, _("Reparación y optimización"))
	self.menu.AppendSubMenu(ws_sys, _("Seguridad de Windows"))
	self.menu.AppendSubMenu(s_sys, _("Sonido y voz"))
	
	self.menu.AppendSubMenu(u_sys, _("Utilidades del sistema"))
	t_menu.AppendSubMenu(self.menu, "&TCA_SystemUtilities")

	