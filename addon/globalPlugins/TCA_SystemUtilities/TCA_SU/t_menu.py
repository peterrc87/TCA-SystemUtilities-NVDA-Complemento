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
	t_menu = gui.mainFrame.sysTrayIcon.toolsMenu
	
	t_sh_s = a_sys.Append(-1, _("Apagar"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAShut, t_sh_s)
	t_sh_h = a_sys.Append(-1, _("Hibernar"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAhiber, t_sh_h)
	t_sh_r = a_sys.Append(-1, _("Reiniciar"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAShutR, t_sh_r)
	t_sh_b = a_sys.Append(-1, _("Reiniciar y entrar en BIOS/UEFI"))

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
	t_soundOps = s_sys.Append(-1, _("Opciones de sonido"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAsndOp, t_soundOps)
	t_vo =s_sys.Append(-1, _("Opciones de voz"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAopvox, t_vo)
	t_opti = r_sys.Append(-1, _("Optimizar las unidades"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAoptim, t_opti)
	t_sfc = r_sys.Append(-1, _("Análisis del sistema Con SFC    "))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAsfc, t_sfc)
	t_clDisk = r_sys.Append(-1, _("Limpiar disco"))
	
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAclean, t_clDisk)
	t_rExplo = e_sys.Append(-1, _("Reiniciar Explorador"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAr_explo, t_rExplo)
	t_dism = r_sys.Append(-1, _("Reparar sistema con Dism"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAa_dism, t_dism)

	t_wVer = u_sys.Append(-1, _("Saber la versión de Windows"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAver, t_wVer)
	
	self.menu.AppendSubMenu(a_sys, _("Apagado del sistema"))
	self.menu.AppendSubMenu(e_sys, _("Explorador y Procesos"))
	self.menu.AppendSubMenu(s_sys, _("Sonido y voz"))
	self.menu.AppendSubMenu(r_sys, _("Reparación y optimización"))
	self.menu.AppendSubMenu(u_sys, _("Utilidades del sistema"))
	t_menu.AppendSubMenu(self.menu, "&TCA_SystemUtilities")

	