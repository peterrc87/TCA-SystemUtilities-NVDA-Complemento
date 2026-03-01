## TCA SystemUtilities.

Pequeño complemento que nos permite ejecutar rápidamente algunas acciones de Windows mediante atajo de teclado. 
Es capaz de realizar una reparación del sistema con SFC. Puede copiar al portapapeles información del sistema, copiar un listado de todos los elementos que se encuentran en una ruta,cocultar o mostrar archivos  y carpetas, entrar a la BIOS y mucho más. 
También eliminar configuraciones y complementos en pantallas seguras.

* Autor: Peter Reina <peterrc87@gmail.com>
* Compatibilidad: ver requisitos por versión en Cambios 0.11/0.12

## Funciones del sistema:

* Apagado del sistema: Apaga Windows 
 además, emite el clásico sonido de cierre de Windows. Nos avisa que el sistema se va a apagar mediante un mensaje.
 Nos ofrece la posibilidad de cerrar o anular el apagado durante 3 segundos.

* Reinicio del sistema: Reinicia Windows 
 además, emite el clásico sonido de cierre de Windows. Nos avisa que el sistema se va a reiniciar mediante un mensaje.
 Nos ofrece la posibilidad de cerrar o anular el reinicio durante 3 segundos.

* Anular (apagado o reinicio): Nos permite anular cualquiera de las 2 opciones anteriores (apagado o reinicio) 
Además, nos avisa con un mensaje que se está anulando el apagado/reinicio.
 ! ¡Nota! solo contamos con 3 segundos para realizar esta acción.

* Hibernar: Nos permite poner en modo hibernación al sistema, cómodamente desde NVDA.

* Reiniciar y entrar en Modo seguro con funciones de red: Esta funcionalidad muy complicada a veces de poner, desde TCA SystemUtilities es cosa de niños. 
Muy fácilmente nos permite ingresar a Windows con funciones limitadas sin cargar servicios o programas innecesarios, desde allí podemos hacer limpiezas más exhaustivas, eliminar programas no deseados, malware y mucho más. 
! ¡Nota importante! 
En este modo, en sistemas anteriores a Windows 10, es posible que no esté activado el servicio de audio, por ende, no podemos disponer de la síntesis de voz del lector de pantalla. 
Una vez activada esta función deberemos luego deshabilitarla, lo podemos hacer desde el mismo menú de TCA SystemUtilities, en el apartado: "Apagado del sistema".

* Reiniciar en Modo normal: nos permite deshabilitar El modo seguro si lo hemos activado, devuelve el inicio de Windows a sus valores normales (cargan todos los servicios y programas que tengamos en el inicio). 

* Suspender: Permite suspender El sistema, cómodamente desde NVDA. 
* Entrar en la BIOS-UEFI: Podremos cómodamente desde Windows y con NVDA indicarle al PC que ingrese a la BIOS-UEFI en el próximo reinicio. 
Sin necesidad de pulsar, o saber la tecla, directamente y de forma sencilla. 
(¡Nota importante!) en la BIOS-UEFI no hay servicio de audio, por ende, no podremos utilizar un lector de pantalla en su interfaz). Una vez deseemos regresara nuestro sistema, podemos pulsar la combinación de teclas: CTRL+ALT+Supr.

* Abrir CMD en la ruta actual: Con un simple atajo de teclado podremos abrir el símbolo del sistema en Windows (CMD), y tomará la ruta de cualquier carpeta donde se encuentre el foco.

* Abrir el CMD como administrador: Con un sencillo atajo de teclado abriremos el símbolo del sistema de Windows, con privilegios de administrador, en la ruta actual en todos los Windows soportados por NVDA.

•	Lanzador de consolas: Saca un menú donde se encuentran las consolas: CMD, Powershell, Windows terminal, Git Bash. Desde este, podremos abrir cualquiera de estas consolas (incluso con privilegios de administrador) en la ruta que tenga el foco del NVDA.
•	Este módulo fue desarrollado por: Héctor Benítez Corredera.

* Borrar el portapapeles y su historial: Cómoda funcionalidad que vacía todo lo que tengamos en el portapapeles, en Windows 10 y 11, también limpia todo lo que tengamos en el historial si lo tenemos activado.
* Habilitar menú de contexto clásico de Windows: Nos devuelve al clásico menú de contexto, utilizado en Windows 10 o anteriores.
* Habilitar menú de contexto tipo: Windows 11: Activa el menú de contexto tipo Windows 11 si así lo deseamos.
* Matar los procesos de cualquier aplicación activa: Intenta terminar cualquier proceso activo que no sea de Windows, incluso si están en segundo plano. 

* Reiniciar Explorador: Nos reinicia cómodamente desde NVDA el Explorador de Windows. 
Podemos hacerlo mediante algún atajo que le asignemos, o desde el menú de TCA SystemUtilities.

* Cerrar todas las aplicaciones: Fuerza a cerrarse todos los procesos activos que no sean parte de Windows (¡Nota! todos los procesos serán forzados a cerrarse, así que no se podrán guardar ni documentos, ni proyectos, e incluso el NVDA será cerrado).

* Cerrar tareas que no responden: TCA SystemUtilities intentará cerrar los procesos que no responden. 

* Ocultar archivos o carpetas (según foco): Permite poner el atributo Oculto al archivo o carpeta que tenga el foco.

* Mostrar archivo o carpeta oculto (según foco): Quita el atributo Oculto del archivo o carpeta que tenga el foco.
 

## Funciones de reparación del sistema. 

* Hacer un análisis del sistema con SFC: Nos permite Realizar un análisis / reparación del sistema de archivos de Windows SFC /SCANNOW.

* Desactivar almacenamiento reservado: Devuelve los casi 10 Gb que Windows secuestra de nuestro disco duro para actualizaciones (no es necesario tener activado esto para que funcionen las actualizaciones).

* Activar almacenamiento reservado: Si aún deseas activar esta función de Windows y forzar a tu disco duro a dejar reservados casi 10Gb, con esta acción lo activarás.

* Activar el plan alto rendimiento: Desde un atajo de teclado, o desde el menú de TCA SystemUtilities, podremos activar de forma sencilla, rápida y directa el plan alto rendimiento de Windows. No habrá necesidad de ir a las configuraciones de energía avanzadas del panel de control.
* Activar plan Equilibrado: Desde un atajo de teclado, o desde el menú de TCA SystemUtilities, podremos activar de forma sencilla, rápida y directa el plan equilibrado de Windows, No habrá necesidad de ir a las configuraciones de energía avanzadas del panel de control.
* Limpiar caché DNS: borra de forma rápida y directa toda la caché DNS de Windows (puede mejorar problemas con la navegación por internet).
* Limpiar configuración guardada en pantallas seguras: Elimina todos los complementos y configuraciones que hayamos copiado para ejecutarse en las pantallas seguras, dejando a NVDA como viene de forma nativa. 

* Limpiar disco: Nos permite lanzar el limpiador de Discos de Windows, pero con opciones mucho más avanzadas. Nos limpiará todos y cada uno de los discos y dispositivos de almacenamiento que tengamos conectados al sistema. 
La lógica se ha mejorado y se corrigió un problema por el que el limpiador podía cerrarse de forma repentina.
La primera vez que lo ejecutemos, nos sacará una ventana de diálogo, para crear un perfil de limpieza, podremos marcar todas las casillas que deseemos para limpiar de forma más exhaustiva. es conveniente que pulsemos el botón: "Crear perfil" esto solo es necesario hacerlo una vez. Disponemos de una casilla de verificación que podemos marcar si no queremos que salga más este diálogo. 
 
* Reparar sistema con Dism: Realiza un análisis profundo e intenta reparar problemas en Windows.



## Funciones directas del portapapeles:

* Copiar al portapapeles el listado de carpetas o archivos de la ruta actual: 
Nos copia directamente al portapapeles la lista de elementos de la ruta donde nos encontremos, ahora de forma ordenada en todas las rutas; así podremos pegarla en cualquier sitio editable.

* Copiar al portapapeles la información sobre las tarjetas de sonido: Nos permite copiar de forma directa al portapapeles la información sobre todos los dispositivos de sonido que tengamos en el sistema.
así podremos pegarla en cualquier sitio editable. 

* Copiar información de todo el sistema al portapapeles: Nos permite copiar de forma directa, todo un resumen de nuestro sistema. 
así podremos pegarla en cualquier sitio editable. 

* Copiar la ruta: Copia al portapapeles la ruta de la carpeta o la ruta completa del archivo que tenga el foco. 
así podremos pegarla en cualquier sitio editable. 
 

## Opciones de Seguridad de Windows.
Control de cuentas de usuario (uac). 

* Activar el control de cuentas de usuario (uac): Establece el nivel del control de cuentas de usuario en 34 (activado). 

* Desactivar el control de cuentas de usuario (uac): Establece el nivel del control de cuentas de usuario en 0 (desactivado). 

Windows Defender. 

* Analizar arranque del sistema: Realiza de forma directa un análisis de virus y malware de los archivos pertenecientes al sector de arranque de Windows (Boot sector). 

* Análisis completo: Lanza de forma directa, un análisis de virus de todo el sistema. 

* análisis rápido: Lanza de forma directa, un análisis de virus y malware rápido (de las partes esenciales del sistema). 

* Escanear archivos comprimidos: Activa de forma directa, que el antivirus de Windows pueda escanear archivos comprimidos (rar, zip, ace, tar, etc.). 

* No escanear archivos comprimidos: Desactiva de forma directa, que el antivirus de Windows pueda escanear archivos comprimidos (rar, zip, ace, tar, etc.). 
* Listado de archivos en cuarentena al portapapeles: Copia al portapapeles, un listado y la información de todos los archivos que el antivirus de Windows haya puesto encuarentena.
 
## Opciones multimedia.

* Activar Webcam: Nos permite cómodamente desde NVDA activar la webcam si la tenemos (dejarla lista para usarse).

* Desactivar Webcam: Nos permite cómodamente desde NVDA desactivar la webcam si la tenemos (deshabilitarla, ningún programa podrá utilizarla).


* Abrir opciones de voz: Nos abre rápidamente las Opciones o Propiedades de texto a voz. Aquí podemos elegir nuestra voz TTS instalada en el sistema por defecto. 
 
 * Abrir Opciones de Sonido: Nos permite abrir de forma directa las opciones de Sonido del Panel de Control (Sonido, Reproducción, Grabación, Comunicaciones). 
 


## Abrir rápidamente algunas funciones del sistema:
* Abrir Optimizar las unidades: Nos permite abrir de forma directa ésta interesante funcionalidad de Windows, para mejorar el rendimiento de nuestros discos duros. 
 
* Abrir mapa de caracteres: Abre de forma directa ésta interesante funcionalidad de Windows. Que nos permite elegir y conocer cualquiera de los signos, números y letras existentes en el sistema. 
Muy útil para saber signos raros o difíciles de sacar con el teclado.
 
* Abrir Asistente guardar contraseñas de usuarios: Abre el asistente de esta muy útil pero poco conocida utilidad de Windows.
Que nos permite guardar las credenciales (nombres, contraseñas y más), de las cuentas de usuario que tengamos en el sistema. 
* Abrir Asistente transferir archivos por BlueTooth: Nos permite lanzar directamente este asistente para recibir o enviar archivos mediante nuestros dispositivos BlueTooth. 
* Abrir Carpeta Roaming: Abre de forma directa la carpeta Appdata>Roaming (Aquí encontramos la carpeta de configuración del NVDA, y de muchos otros programas).).
 
* Abrir el asistente para guardar la contraseña del sistema: 
Nos abrirá este útil Asistente poco conocido que nos permite hacer un respaldo de la contraseña de Windows, para poder recuperarla desde un dispositivo externo.
 
* abrir Monitor de Recursos: podremos abrir de forma directa esta potente herramienta de Windows, poco conocida. Es como un administrador de tareas mejorado, podemos gestionar todos los servicios, aplicaciones y procesos que estén corriendo en nuestro sistema.
Aparte podremos saber cuánta memoria, disco, red y más consumen.
 
 

## ¿Nota importante!

Todos y cada uno de los atajos de teclado, se pueden asignar a gusto personal, desde el diálogo de: Preferencias > Gestos de entrada de NVDA.

## Cambios en la versión 0.12:
* Compatibilidad: mínima versión soportada: NVDA 2026.1 (64 bits).
* Se retiran funciones: Administrador de discos, Administrador de dispositivos, Sitio oficial de complementos, Opciones de carpeta, Mezclador de volumen, Saber arquitectura del sistema, Saber la versión de Windows.
* Nueva función: Habilitar menú de contexto clásico de Windows.
* Nueva función: Habilitar menú de contexto tipo: Windows 11.
* Nueva lógica interna para obtener la ruta del sistema, mejorándo las siguientes funciones:
  - Copiar la ruta (ahora copia también la ruta completa de archivos).
  - Abrir CMD en la ruta actual.
  - Abrir CMD como administrador en la ruta actual (funciona en todos los Windows soportados por NVDA).
  - Ocultar/Mostrar ahora actúa sobre archivos y carpetas que tengan el foco.
  - Copiar listado de archivos y carpetas  al portapapeles ahora se muestran ordenados en todas las rutas.
* Mejorada la lógica de “Limpiar disco” y corregido cierre repentino del limpiador.

## Cambios en la versión 0.11:
* Esta será la última versión lanzada, compatible con NVDA de 32 bits.
* Lanzada junto con la versión 0.12.
* Mismas nuevas  funciones del menú de contexto de Windows que en la versión: 0.12.
* Incluye la nueva lógica interna para la ruta del sistema y las mejoras en: Copiar ruta, abrir CMD en ruta actual, abrir CMD como administrador en la ruta actual, ocultar/mostrar por foco y copiar listado ordenado.
* Se retiran las mismas funciones indicadas en la versión 0.12.
* Mejora y corrección en la función: Limpiar disco.

## Cambios en la versión 0.10:
* Compatibilidad con NVDA 2025.1.
* Nueva función: Activar plan alto rendimiento (energía de Windows).
* Nueva función: Activar plan equilibrado (energía de Windows).
* Nueva función: Abrir el lanzador de consolas.
* Corregida función: Abrir CMD en la ruta actual.
* Corregida la función: Limpiar disco.
* Corregida la función: Optimizar unidades.
* Optimizadas las funciones: apagado, reinicio y anular el apagado del sistema.

## Cambios en la versión 0.9:
* Compatibilidad con NVDA 2024.1.
* Nueva función Matar los procesos de cualquier aplicación activa.
* Optimizada la función: GetPath, necesaria en Windows 11 23H2.
* Incluida dll: pywintypes311.dll compatible con Python 3.11.
* Se retiraron los atajos por defecto: apagar, reiniciar y anular apagado del sistema.

## Cambios en la versión 0.8
* Desde esta versión TCA SystemUtilities cambia su nomenclatura de versiones (para ser compatible con NVDA 2023.3)
Ahora las versiones tendrán 3 dígitos esta será 0.8.2.
* Nueva función desactivar el control de cuentas de usuario (uac).
* Nueva función Activar el control de cuentas de usuario (uac).
* Tanto la función activar, como la función desactivar el control de cuentas de usuario estarán en el menú de TCA SystemUtilities en la categoría: Seguridad de Windows;
Así mismo se les podrá establecer atajos de teclado si lo deseamos desde Gestos de entrada.

## Cambios en la versión 06:
* Nueva función interna para tomar la ruta del sistema (path), ahora son 2, en caso de que falle una, TCA SystemUtilities intentará usar la otra.
(Una de las funciones ha sido desarrollada por: Héctor Benítez).
* Nueva función: Cerrar todos los procesos activos.
* Cerrar tareas que no están respondiendo en Windows.
* Corregido, el menú de TCA SystemUtilities ya no se repetirá si se recargan los complementos.
(Cortesía de Héctor Benítez).
* Corregido: ya no existen atajos de teclados predefinidos.


## Cambios en la versión 05.

* Nueva función para limpiar complementos y configuraciones en pantallas seguras.
* Nueva función borrar el portapapeles incluyendo el historial en Windows.
* Nueva función abrir el CMD en la ruta actual.
* Nueva función abrir el CMD con privilegios de administrador.
* Nueva función: Desactivar el almacenamiento reservado en Windows.
* Nueva función: activar el almacenamiento reservado en Windows.
* Corregida y optimizada función para obtener el objeto, con esto mejoran varias funciones como: copiar la ruta al portapapeles, copiar listado de archivos al portapapeles, ocultar o mostrar archivos y carpetas.


## Cambios en la versión: 04.

* Nueva función para entrar en la BIOS-UEFI del sistema (en el apartado: "Apagado del sistema").
* Se cambió el menú: "Sonido y voz", a: "Voz y multimedia".
* 2 Nuevas funciones en el apartado: "Voz y multimedia" (Activar/desactivar la webcam).
* Nueva función: "Limpiar caché DNS" (en el apartado Reparación y optimización").
* Restructuración de la documentación del complemento.
* Traducido al italiano.
* Compatible con NVDA 2022.

* Corrección de seguridad (sys.path.remove())


## Cambios en la versión 03:
* En esta versión TCA SystemUtilities es ya totalmente compatible con el nuevo sistema: Windows 11.
* Nuevo Menú: Seguridad de Windows 
con varias opciones referentes al antivirus de Windows.
* Otra opción en el menú: Apagado del sistema, la opción: "suspender el sistema".
* En esta versión el complemento está traducido a los idiomas: árabe, portugués (Portugal, portugués Brasil), y rumano.


## Cambios en la versión: 02.

* En esta versión el complemento cuenta con un cómodo Menú desde donde podemos ejecutar la mayoría de sus funcionalidades (no todas). 
El mismo se encuentra en el Menú: "Herramientas" de NVDA, y tiene el nombre del complemento: "TCA SystemUtilities".
* Se retiraron en esta versión todos los atajos prestablecidos, con lo que ahora deberéis asignar los atajos a cualquiera de las funciones, desde el menú: "Gestos de entrada" de NVDA.
* Mas funciones en los apartados: Apagado del sistema, Explorador de Windows, Sonido y voz, Reparación del sistema.
* Optimización de todo el código del complemento.

***

Código del proyecto en GitHub: 
[https://github.com/peterrc87/TCA-SystemUtilities-NVDA-Complemento](https://github.com/peterrc87/TCA-SystemUtilities-NVDA-Complemento)
