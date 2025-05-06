# -*- coding: utf-8 -*-
# Copyright (C) 2024 Héctor J. Benítez Corredera <xebolax@gmail.com>
# This file is covered by the GNU General Public License.
#
# Agradecimientos a los creadores del complemento NAO.
#
# Autores: Alessandro Albano, Davide De Carne y Simone Dal  Maso
#
# Por las funciones extraídas de dicho complemento para obtener rutas.
#
# Las funciones extraídas son:
# is_explorer, get_selected_files_explorer_ps y get_selected_file_explorer
#
import addonHandler
#import globalPluginHandler
import ui
import gui
import api
import globalVars
import wx
#from scriptHandler import script
import os
import ctypes
import threading
import subprocess
import json
from comtypes.client import CreateObject as COMCreate

# Inicializa las traducciones para el complemento (si es necesario).
#addonHandler.initTranslation()

_(''' *** Agradecimientos ***
*** Módulo Lanzar_consolas ***
Este módulo ha sido desarrollado por: Héctor J. Benítez Corredera <xebolax@gmail.com
Copyright (C) 2024
Agradecemos por haberlo cedido gentilmente para utilizarse en el complemento TCA SystemUtilities.
Se agradece también a los desarrolladores del complemento Nao: (Autores: Alessandro Albano, Davide De Carne y Simone Dal Maso);
De dicho complemento se han extraído las siguiente funciones para extraer rutas:
 : is_explorer, get_selected_files_explorer_ps y get_selected_file_explorer''')


def disableInSecureMode(decoratedCls):
	"""Decorador que deshabilita una clase de complemento global en modo seguro.

	Args:
		decoratedCls (class): La clase a decorar.

	Returns:
		class: La clase original o GlobalPlugin dependiendo del modo seguro.
	"""
	if globalVars.appArgs.secure:
		return globalPluginHandler.GlobalPlugin
	return decoratedCls

@disableInSecureMode
class Lanzar_consolas():
	def __init__(self, *args, **kwargs):
		
		self._shell = None
		self.is_run = False
		self.terminales = self.comprobar_terminales()
		self.git_disponibilidad, self.git_ruta = self.comprobar_git_powershell()

	def comprobar_terminales(self):
		"""
		Comprueba la disponibilidad de cmd, PowerShell y trata de encontrar si Windows Terminal (wt) está en el PATH.

		Returns:
			dict: Un diccionario indicando la disponibilidad de 'cmd', 'PowerShell', y 'wt'.
		"""
		resultados = {'cmd': False, 'PowerShell': False, 'wt': False}

		# Comprobar cmd y PowerShell mediante la ejecución de un comando simple
		comandos = {
			'cmd': ['cmd.exe', '/c', 'echo'],
			'PowerShell': ['powershell.exe', '-Command', "echo $null"],
		}

		for terminal, comando in comandos.items():
			try:
				subprocess.Popen(comando, creationflags=subprocess.CREATE_NO_WINDOW, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				resultados[terminal] = True
			except Exception as e:
				pass

		# Intenta encontrar 'wt.exe' en el PATH para verificar la disponibilidad de Windows Terminal
		resultados['wt'] = any(os.access(os.path.join(path, 'wt.exe'), os.X_OK) for path in os.environ["PATH"].split(os.pathsep))

		return resultados

	def comprobar_git_powershell(self):
		"""
		Comprueba si Git está instalado y encuentra su ubicación utilizando PowerShell.
    
		Returns:
			tuple: (bool, str) Un booleano que indica si Git está instalado, y una cadena
			con la ubicación de Git si está instalado, de lo contrario, una cadena vacía.
		"""
		# Comando PowerShell para buscar Git y extraer su ruta de instalación
		comando_ps = "Get-Command git | Select-Object -ExpandProperty Source | ConvertTo-Json"
    
		try:
			# Ejecución del comando PowerShell
			resultado = subprocess.Popen(["powershell", "-Command", comando_ps], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
			salida, error = resultado.communicate()
        
			# Si se obtiene una salida válida de PowerShell, asume que Git está instalado
			if resultado.returncode == 0 and salida:
				# Convierte la salida de JSON a cadena para obtener la ruta
				ruta_git = json.loads(salida.decode('utf-8'))
				return (True, os.path.dirname(os.path.dirname(ruta_git)))
			else:
				return (False, "")
		except Exception as e:
			return (False, "")

	def is_explorer(self, obj=None):
		"""Determina si el objeto en primer plano es el explorador de Windows.

		Args:
			obj (NVDA object, optional): Objeto a comprobar. Si no se proporciona, se utiliza el objeto en primer plano.

		Returns:
			bool: True si el objeto en primer plano es el explorador de Windows, False en caso contrario.
		"""
		if obj is None: obj = api.getForegroundObject()
		return obj and obj.appModule and obj.appModule.appName and obj.appModule.appName == 'explorer'

	def get_selected_files_explorer_ps(self):
		"""
		Obtiene los archivos seleccionados en el explorador de Windows usando PowerShell.
    
		Este método intenta ejecutar un script de PowerShell que recupera los elementos actualmente seleccionados en todas las ventanas abiertas del explorador de Windows. Cada elemento seleccionado se identifica por el manejador de ventana (HWND) y la ruta del archivo seleccionado.
    
		Returns:
			dict: Un diccionario donde cada clave es el HWND de una ventana del explorador y cada valor es la ruta del archivo seleccionado en esa ventana. Retorna un diccionario vacío si no hay selecciones o en caso de error.
		"""
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		cmd = "$OutputEncoding = [console]::InputEncoding = [console]::OutputEncoding = New-Object System.Text.UTF8Encoding; (New-Object -ComObject 'Shell.Application').Windows() | ForEach-Object { echo \\\"$($_.HWND):$($_.Document.FocusedItem.Path)\\\" }"
		cmd = "powershell.exe \"{}\"".format(cmd)
		try:
			p = subprocess.Popen(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, startupinfo=si, encoding="utf-8", text=True)
			stdout, stderr = p.communicate()
			if p.returncode == 0 and stdout:
				ret = {}
				lines = stdout.splitlines()
				for line in lines:
					hwnd, name = line.split(':',1)
					ret[str(hwnd)] = name
				return ret
		except:
			pass
		return False

	def get_selected_file_explorer(self, obj=None):
		"""
		Obtiene la ruta del archivo seleccionado en el explorador de Windows.

		Args:
			obj (NVDA object, optional): Objeto del explorador de Windows. Si no se proporciona, se utiliza el objeto en primer plano.

		Returns:
			str or None: La ruta del archivo seleccionado si hay alguno, None si no hay selección o si ocurre un error.
		"""
		if obj is None: obj = api.getForegroundObject()
		file_path = False
		if self.is_explorer(obj):
			desktop = False
			try:
				if not self._shell:
					self._shell = COMCreate("shell.application")
				for window in self._shell.Windows():
					if window.hwnd == obj.windowHandle:
						file_path = str(window.Document.FocusedItem.path)
						break
				else:
					desktop = True
			except:
				try:
					windows = self.get_selected_files_explorer_ps()
					if windows:
						if str(obj.windowHandle) in windows:
							file_path = windows[str(obj.windowHandle)]
						else:
							desktop = True
				except:
					pass
			if desktop:
				desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
				file_path = desktop_path + '\\' + api.getDesktopObject().objectWithFocus().name
		return file_path

	def encontrar_directorio_valido(self, ruta):
		"""
		Encuentra el directorio válido más cercano para una ruta dada.

		Args:
			ruta (str): La ruta a analizar.

		Returns:
			str or None: El directorio encontrado o None si no se encuentra un directorio válido.
		"""
		if not isinstance(ruta, str):
			return None

		if os.path.isdir(ruta):
			return ruta

		partes_ruta = ruta.split(os.sep)

		for i in range(len(partes_ruta), 0, -1):
			directorio = os.sep.join(partes_ruta[:i])
			if os.path.isdir(directorio):
				return directorio

		return None

	def cmd_asincrona(self, directorio, tipo='cmd', admin=False):
		"""
		Ejecuta un comando en un directorio específico, opcionalmente con privilegios de administrador.

		Args:
			directorio (str): El directorio en el cual ejecutar el comando.
			tipo (str, opcional): Tipo de terminal a abrir ('cmd', 'powershell', 'wt', 'git-bash').
			admin (bool, opcional): Si es True, ejecuta el comando con privilegios de administrador.
		"""
		oldValue = ctypes.c_void_p()
		ctypes.windll.kernel32.Wow64DisableWow64FsRedirection(ctypes.byref(oldValue))
		try:
			if tipo == 'cmd':
				ejecutable = 'cmd.exe'
				parametros = '/k pushd "{}"'.format(directorio)
			elif tipo == 'powershell':
				ejecutable = 'powershell.exe'
				parametros = f'-NoExit -Command "Set-Location -LiteralPath \\"{directorio}\\""'
			elif tipo == 'wt':
				ejecutable = 'wt.exe'
				parametros = f'-d "{directorio}"'
			elif tipo == 'git-bash':
				ejecutable = os.path.join(self.git_ruta, 'git-bash.exe')
				parametros = f'--cd="{directorio}"'
			else:
				raise ValueError(_("Tipo de terminal no soportado."))

			ret = ctypes.windll.shell32.ShellExecuteW(None, 'runas' if admin else 'open', ejecutable, parametros, None, 1)
		finally:
			ctypes.windll.kernel32.Wow64RevertWow64FsRedirection(oldValue)

	def lanzar(self):
		"""Función para abrir el dialogo de lanzar consolas."""
		if not self.is_run:
			directorio = self.encontrar_directorio_valido(self.get_selected_file_explorer())
			self._shell = None
			if not directorio:
				ui.message(_('No se encontró una selección válida.'))
				return
			gui.mainFrame.prePopup()
			dlg = OpcionesConsolas(None, self, directorio)
			dlg.ShowModal()
			dlg.Destroy()
			gui.mainFrame.postPopup()
		else:
			ui.message(_("Ya hay una instancia de lanzador de consolas abierta."))

class OpcionesConsolas(wx.Dialog):
	def __init__(self, parent, frame, directorio, title=_("Lanzador de consolas")):
		super(OpcionesConsolas, self).__init__(parent, title=title)

		self.frame = frame
		self.directorio = directorio
		self.frame.is_run = True
		self.SetSize((300, 250))
		self.Centre()

		# Lista de opciones para el menú.
		self.opciones = [
			_("Abrir CMD aquí"),
			_("Abrir CMD como Administrador"),
			_("Abrir PowerShell aquí"),
			_("Abrir PowerShell como Administrador"),
			_("Abrir Windows Terminal aquí"),
			_("Abrir Windows Terminal como Administrador"),
			_("Abrir git-bash aquí"),
			_("Abrir git-bash como Administrador"),
		]
		# Filtra las opciones basándote en la disponibilidad
		opciones_filtradas = self._filtrar_opciones()
		self.listBox = wx.ListBox(self, choices=opciones_filtradas, style=wx.LB_SINGLE)
		self.listBox.SetFocus()
		self.listBox.SetSelection(0)  # Selecciona la primera opción por defecto.

		# Configura el layout.
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.listBox, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
		self.SetSizer(sizer)

		# Maneja el cierre con la tecla Escape y otras teclas.
		self.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)

	def _filtrar_opciones(self):
		"""
		Filtra y retorna las opciones de terminales disponibles basándose en la disponibilidad
		de CMD, PowerShell y Windows Terminal (wt) en el sistema.

		CMD se asume siempre disponible en sistemas Windows, por lo tanto, las opciones
		relacionadas con CMD se incluyen por defecto. Las opciones para abrir PowerShell
		y Windows Terminal se incluyen solo si se detecta su disponibilidad en el sistema.

		Returns:
			list: Una lista de opciones de terminales filtradas que están disponibles para ser
			mostradas en un ListBox, dependiendo de la disponibilidad de cada terminal.
		"""
		opciones_filtradas = self.opciones[:2]  # CMD siempre está disponible en Windows, así que lo incluimos por defecto
		if self.frame.terminales['PowerShell']:
			opciones_filtradas.extend(self.opciones[2:4])
		if self.frame.terminales['wt']:
			opciones_filtradas.extend(self.opciones[4:6])
		if self.frame.git_disponibilidad:
			opciones_filtradas.extend(self.opciones[6:8])
		return opciones_filtradas

	def ejecutarSeleccion(self):
		"""
		Ejecuta la acción seleccionada en el ListBox.
		"""
		seleccion = self.opciones.index(self.listBox.GetString(self.listBox.GetSelection()))
		if seleccion == 0:
			self.abrirCMD(asAdmin=False)
		elif seleccion == 1:
			self.abrirCMD(asAdmin=True)
		elif seleccion == 2:
			self.abrirPOWERSHELL(asAdmin=False)
		elif seleccion == 3:
			self.abrirPOWERSHELL(asAdmin=True)
		elif seleccion == 4:
			self.abrirWT(asAdmin=False)
		elif seleccion == 5:
			self.abrirWT(asAdmin=True)
		elif seleccion == 6:
			self.abrirGITBASH(asAdmin=False)
		elif seleccion == 7:
			self.abrirGITBASH(asAdmin=True)

		self.frame.is_run = False
		self.Close()

	def abrirCMD(self, asAdmin):
		"""
		Abre la línea de comandos (CMD), opcionalmente con privilegios de administrador.

		Args:
			asAdmin (bool): Determina si CMD debe abrirse con privilegios de administrador.
		"""
		if asAdmin:
			threading.Thread(target=self.frame.cmd_asincrona, args=(self.directorio, "cmd", True,), daemon=True).start()
		else:
			threading.Thread(target=self.frame.cmd_asincrona, args=(self.directorio, "cmd", False,), daemon=True).start()

	def abrirPOWERSHELL(self, asAdmin):
		"""
		Abre la línea de comandos (PowerShell), opcionalmente con privilegios de administrador.

		Args:
			asAdmin (bool): Determina si PowerShell debe abrirse con privilegios de administrador.
		"""
		if asAdmin:
			threading.Thread(target=self.frame.cmd_asincrona, args=(self.directorio, "powershell", True,), daemon=True).start()
		else:
			threading.Thread(target=self.frame.cmd_asincrona, args=(self.directorio, "powershell", False,), daemon=True).start()

	def abrirWT(self, asAdmin):
		"""
		Abre la línea de comandos (Windows Terminal), opcionalmente con privilegios de administrador.

		Args:
			asAdmin (bool): Determina si Windows Terminal debe abrirse con privilegios de administrador.
		"""
		if asAdmin:
			threading.Thread(target=self.frame.cmd_asincrona, args=(self.directorio, "wt", True,), daemon=True).start()
		else:
			threading.Thread(target=self.frame.cmd_asincrona, args=(self.directorio, "wt", False,), daemon=True).start()

	def abrirGITBASH(self, asAdmin):
		"""
		Abre la línea de comandos (git-bash), opcionalmente con privilegios de administrador.

		Args:
			asAdmin (bool): Determina si git-bash debe abrirse con privilegios de administrador.
		"""
		if asAdmin:
			threading.Thread(target=self.frame.cmd_asincrona, args=(self.directorio, "git-bash", True,), daemon=True).start()
		else:
			threading.Thread(target=self.frame.cmd_asincrona, args=(self.directorio, "git-bash", False,), daemon=True).start()

	def onKeyPress(self, event):
		"""
		Manejador de eventos para teclas presionadas en el diálogo.

		Args:
			event: El evento de teclado.
		"""
		if event.GetKeyCode() == wx.WXK_RETURN:
			self.ejecutarSeleccion()
		elif event.GetKeyCode() == wx.WXK_ESCAPE:
			self.frame.is_run = False
			self.Close()
		event.Skip()

