---
layout: default
title: Política de privacidad
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <a href="privacy-nl">Nederlands</a> · <a href="privacy-de">Deutsch</a> · <a href="privacy-fr">Français</a> · <strong>Español</strong> · <a href="privacy-sv">Svenska</a> · <a href="privacy-it">Italiano</a> · <a href="privacy-ko">한국어</a> · <a href="privacy-tr">Türkçe</a> · <a href="privacy-ja">日本語</a>
</div>

# Política de privacidad

**Última actualización: 17 de agosto de 2026**

EV Dashboard ("la aplicación") es desarrollada por Greg Burlingame. Esta política de privacidad describe cómo la aplicación maneja sus datos.

## Recopilación de datos

EV Dashboard **no** recopila, transmite ni vende datos personales a terceros. La aplicación no tiene servidor, ni cuenta, ni inicio de sesión. No contiene análisis, publicidad ni rastreo de ningún tipo, y nunca sube sus datos a ningún sitio.

## Datos almacenados en su dispositivo

La aplicación almacena los siguientes datos localmente en su dispositivo:

* **Datos de diagnóstico del vehículo** — El estado de la batería, las tensiones de celda, las temperaturas, los datos de carga, las presiones de neumáticos y otras lecturas de sensores de su vehículo se mantienen en memoria mientras la aplicación está en ejecución. Estos datos no se conservan entre inicios de la aplicación, salvo que utilice una función de grabación.
* **Historial de conducción y carga** — Cuando utiliza la función Historial, los resúmenes y las muestras de señales registradas de sus trayectos y sesiones de carga (estado de carga, energía, temperaturas y otras lecturas) se guardan en su dispositivo para que pueda revisarlos más tarde. Una sesión también puede almacenar el lugar donde se produjo, para poder mostrarlo en un mapa.
* **Ajustes de la aplicación** — Sus preferencias (unidades, idioma, apariencia, temas, ajustes de gráficos, selección de adaptador, disposición de mosaicos de CarPlay) se almacenan localmente mediante UserDefaults.
* **Destinos guardados** — Las direcciones que guarda para la navegación, y sus destinos recientes, se almacenan localmente en su dispositivo.
* **Información del dispositivo Bluetooth** — El identificador y el nombre de su adaptador OBD-II emparejado se almacenan localmente para que la aplicación pueda reconectarse automáticamente.
* **Registro de actividad de la app** — Un archivo de registro con eventos del ciclo de vida de la aplicación, de conexión Bluetooth, de interferencia del adaptador y de almacenamiento del historial. Solo se comparte cuando usted usa explícitamente el botón Compartir.
* **Registrador de diagnóstico de conducción** — Un archivo de registro por trayecto con posiciones GPS, muestras de velocidad del vehículo y cálculos de distancia, empleado para diagnosticar la precisión de la distancia y la navegación. Solo se comparte cuando usted usa explícitamente el botón Compartir.
* **Grabaciones de diagnóstico y registros de instantáneas** — Si utiliza la grabación de diagnóstico o la función de comparación de instantáneas, se guarda localmente un archivo de registro con eventos Bluetooth, comandos del adaptador y datos brutos del vehículo. Solo se comparte cuando usted usa explícitamente el botón Compartir.

## Ubicación

EV Dashboard utiliza su ubicación para mostrar su posición en el mapa de CarPlay, ofrecer indicaciones giro a giro, medir la distancia y la eficiencia del trayecto durante la conducción y encontrar cargadores cercanos.

La aplicación solicita únicamente el acceso "Mientras se usa la app". Nunca solicita el acceso "Siempre". Dado que la distancia del trayecto se mide de forma continua durante la conducción, las actualizaciones de ubicación pueden continuar mientras la aplicación está en segundo plano o mientras usted usa otra aplicación; esto termina cuando termina el trayecto.

Su ubicación se utiliza en su dispositivo y no se envía al desarrollador. No se recopila, ni se perfila, ni se vende. Los datos de ubicación pueden escribirse en los archivos descritos arriba (el Registrador de diagnóstico de conducción y el lugar guardado con una sesión del historial); estos solo salen de su dispositivo si usted decide compartirlos.

## Mapas y navegación

Los mapas, la búsqueda de direcciones y el cálculo de rutas los proporciona MapKit de Apple. Cuando busca una dirección o inicia una navegación, la información de consulta y ubicación necesaria se envía a Apple para devolver un resultado, y se trata conforme a la [política de privacidad de Apple](https://www.apple.com/legal/privacy/). Esta información no se envía al desarrollador.

## Actualizaciones de la base de cargadores

La lista de puntos de carga rápida DC viene incluida en la aplicación y funciona sin conexión. No se necesita conexión de red para consultar un cargador ni para navegar hasta él.

Si toca **Ajustes → Navegación → Buscar actualización**, y solo entonces, la aplicación descarga una base de cargadores más reciente. Esto genera dos solicitudes: una para un archivo de manifiesto alojado en theburl.com y otra para el archivo de datos que este indica, alojado en GitHub Releases. Ambas son descargas ordinarias de archivos estáticos, verificadas mediante una suma de comprobación. No se envía ninguna información sobre usted, su dispositivo o su vehículo con estas solicitudes, y no existe ninguna comprobación de actualización automática ni periódica.

## Sincronización con iCloud (opcional)

Si activa la sincronización con iCloud, su historial de conducción y carga —incluido el lugar guardado con una sesión— se sincroniza mediante CloudKit de Apple con su propia cuenta privada de iCloud, de modo que se mantenga coherente entre su iPhone, iPad y Mac. Estos datos se almacenan en su iCloud personal, se rigen por la política de privacidad de Apple y nunca se envían al desarrollador ni a ningún servidor de terceros: el desarrollador no tiene acceso a ellos. Si deja la sincronización con iCloud desactivada, todos los datos permanecen únicamente en su dispositivo.

## Bluetooth

La aplicación se comunica con su adaptador OBD-II mediante Bluetooth Low Energy (BLE). Toda la comunicación Bluetooth se produce directamente entre su dispositivo y el adaptador. No se transmiten datos Bluetooth a ningún servidor ni a terceros.

## Datos del vehículo

La aplicación lee datos de diagnóstico del ordenador de a bordo de su vehículo a través del puerto OBD-II. Estos datos incluyen el estado de la batería, temperaturas, tensiones, presiones de neumáticos y otras lecturas de sensores. Estos datos se muestran en su dispositivo y no se transmiten a ninguna parte.

## Notificaciones

Si activa el recordatorio de desconexión, la aplicación usa notificaciones locales para recordarle que desconecte el adaptador OBD-II cuando el coche se apaga. No se envían datos de notificación a ningún servidor.

## Conservación de datos

Todos los datos se almacenan en su dispositivo. Los archivos de registro y las grabaciones pueden eliminarse mediante la app Archivos de iOS. Desinstalar la aplicación elimina todos los datos almacenados localmente, incluidos los ajustes, los destinos guardados y la información guardada del adaptador. Si activó la sincronización con iCloud, su historial también permanece en su cuenta de iCloud hasta que lo elimine desde la aplicación o desactive la sincronización.

## Privacidad de los menores

La aplicación no recopila conscientemente datos de menores de 13 años.

## Cambios en esta política

Si esta política de privacidad se actualiza, la versión revisada se publicará en esta página con una fecha actualizada.

## Contacto

Si tiene preguntas sobre esta política de privacidad, [abra una incidencia](https://github.com/gburlingame/ioniq-app/issues) en GitHub o escriba a [greg@theburl.com](mailto:greg@theburl.com).
