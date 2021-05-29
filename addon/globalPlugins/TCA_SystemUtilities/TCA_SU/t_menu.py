# -*- coding: UTF-8 -*-
#TCASystemUtilities, Shut down and restart the PC with Windows classic sound, an Open system Options.
#Autor: Peter Reina<peterrc87@gmail.com><Tecnoconocimiento Accesible  2020>
# This file is covered by the GNU General Public License.
from scriptHandler import script
import api, keyboardHandler, globalPluginHandler, tones, ui, globalVars, addonHandler,winUser, gui
#import subprocess, os, sys, threading
import webbrowser, wx
addonHandler.initTranslation()
def create_menu(self):
	#Barra de herramientas.
	self.menu = wx.Menu()	
	t_menu = gui.mainFrame.sysTrayIcon.toolsMenu
	t_passUsu = self.menu.Append(-1, _("Asistente guardar contraseñas de usuarios"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAa_usu, t_passUsu)
	t_blueTooth = self.menu.Append(-1, _("Asistente transferir archivos por Bluetooth"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAblue, t_blueTooth)
	t_roa = self.menu.Append(-1, _("Carpeta Roaming"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCARoa, t_roa)
	t_adDisk = self.menu. Append(-1, _("administrador de discos"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAdisk, t_adDisk)
	t_adDev = self.menu.Append(-1, _("administrador de dispositivoss"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAdispo, t_adDev)
	t_savePass = self.menu.Append(-1, _("asistente para guardar la contraseña del sistema"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCArcon, t_savePass)
	t_char = self.menu.Append(-1, _("mapa de caracteres"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAchar, t_char)
	t_monitor = self.menu.Append(-1, _("Monitor de recursos"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAmon, t_monitor)
	t_foldOps = self.menu.Append(-1, _("Opciones de carpeta"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAcar, t_foldOps)
	t_soundOps = self.menu.Append(-1, _("Opciones de sonido"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAsndOp, t_soundOps)
	t_vo =self.menu.Append(-1, _("Opciones de voz"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAopvox, t_vo)
	t_opti = self.menu.Append(-1, _("Optimizar las unidades"))
	gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.script_TCAoptim, t_opti)

	t_menu.AppendSubMenu(self.menu, "&TCA_SystemUtilities")

	