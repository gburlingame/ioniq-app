---
layout: default
title: Política de privacidad
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <a href="privacy-nl">Nederlands</a> · <a href="privacy-de">Deutsch</a> · <a href="privacy-fr">Français</a> · <strong>Español</strong> · <a href="privacy-sv">Svenska</a> · <a href="privacy-it">Italiano</a> · <a href="privacy-ko">한국어</a> · <a href="privacy-tr">Türkçe</a> · <a href="privacy-ja">日本語</a>
</div>

# Política de privacidad

**Última actualización: 9 de noviembre de 2026**

EV Dashboard ("la aplicación") es desarrollada por Greg Burlingame. Esta política de privacidad describe cómo la aplicación maneja sus datos.

## Recopilación de datos

EV Dashboard no tiene servidor, ni cuenta, ni inicio de sesión. No contiene análisis, publicidad ni rastreo de ningún tipo. El desarrollador nunca recibe sus datos y no se vende nada.

Sus datos solo salen de su dispositivo en estos casos, cada uno descrito más abajo:

* **Compartir con ABRP** — desactivado hasta que usted lo active y vincule un vehículo; envía los datos en vivo de ese vehículo directamente a ABRP.
* **Sincronización con iCloud** — sus ajustes y su historial se sincronizan con su propia cuenta privada de iCloud.
* **Apple Maps** — las búsquedas de direcciones, las direcciones de contactos que elija y las solicitudes de rutas se envían a MapKit de Apple.
* **Archivos que comparte** — los registros, las grabaciones, las exportaciones y las tarjetas para compartir solo salen de su dispositivo cuando toca Compartir.

El mosaico Conexión a Internet y las actualizaciones de la base de cargadores también realizan solicitudes de red. No contienen ninguna información sobre usted ni sobre su vehículo.

## Datos almacenados en su dispositivo

La aplicación almacena los siguientes datos localmente en su dispositivo:

* **Datos de diagnóstico del vehículo** — El estado de la batería, las tensiones de celda, las temperaturas, los datos de carga, las presiones de neumáticos y otras lecturas de sensores de su vehículo se mantienen en memoria mientras la aplicación está en ejecución. Estos datos no se conservan entre inicios de la aplicación, salvo que utilice una función de grabación.
* **Historial de conducción y carga** — Cuando utiliza la función Historial, los resúmenes y las muestras de señales registradas de sus trayectos y sesiones de carga (estado de carga, energía, temperaturas y otras lecturas) se guardan en su dispositivo para que pueda revisarlos más tarde. Una sesión de carga puede almacenar el lugar donde se produjo. Un trayecto almacena su ruta —su ubicación aproximadamente una vez por segundo mientras conduce— para poder mostrarla en su mapa Recorrido. Puede desactivarlo en **Ajustes → Sesiones de conducción → Grabar recorrido**, o eliminar la ruta de un trayecto desde su mapa Recorrido.
* **Fotos de sesiones** — Una foto que añada a una sesión de carga o de conducción se almacena con esa sesión.
* **Ajustes de la aplicación** — Sus preferencias (unidades, idioma, apariencia, temas, ajustes de gráficos, selección de adaptador, disposición de mosaicos de CarPlay, filtros de cargadores, ajustes de neumáticos y nombres de vehículos) se almacenan en su dispositivo y se sincronizan a través de iCloud mientras la opción Sincronizar con iCloud está activada.
* **Destinos guardados** — Las direcciones que guarda para la navegación, y sus destinos recientes, se almacenan en su dispositivo y se sincronizan con sus ajustes.
* **Información del dispositivo Bluetooth** — El identificador y el nombre de su adaptador OBD-II emparejado se almacenan localmente para que la aplicación pueda reconectarse automáticamente.
* **Token de vinculación de ABRP** — Si vincula un vehículo a ABRP, el token que pega desde la app de ABRP se almacena en el llavero de su dispositivo. Desvincular el vehículo lo elimina.
* **Registro de actividad de la app** — Un archivo de registro con eventos del ciclo de vida de la aplicación, de conexión Bluetooth, de interferencia del adaptador y de almacenamiento del historial. Solo se comparte cuando usted usa explícitamente el botón Compartir.
* **Registrador de diagnóstico de conducción** — Un archivo de registro por trayecto con lecturas GPS (posición, rumbo, velocidad y altitud), muestras de velocidad del vehículo y cálculos de distancia, empleado para diagnosticar la precisión de la distancia, la altitud y la navegación. Solo se comparte cuando usted usa explícitamente el botón Compartir.
* **Grabaciones de diagnóstico y registros de instantáneas** — Si utiliza la grabación de diagnóstico o la función de comparación de instantáneas, se guarda localmente un archivo de registro con eventos Bluetooth, comandos del adaptador y datos brutos del vehículo. Solo se comparte cuando usted usa explícitamente el botón Compartir.

## Ubicación

EV Dashboard utiliza su ubicación para mostrar su posición en el mapa de CarPlay, ofrecer indicaciones giro a giro, medir la distancia y la eficiencia del trayecto, grabar el Recorrido de un trayecto, mostrar su altitud y encontrar cargadores cercanos.

La aplicación solicita únicamente el acceso "Mientras se usa la app". Nunca solicita el acceso "Siempre". Las actualizaciones de ubicación pueden continuar mientras la aplicación está en segundo plano o mientras usted usa otra aplicación: si abre la aplicación mientras está conectada a su vehículo, esta mantiene una sesión de ubicación en segundo plano hasta que el vehículo se apague o el adaptador quede fuera del alcance de Bluetooth, e iOS muestra el indicador de ubicación mientras tanto. Las lecturas GPS para la distancia del trayecto y la ruta del Recorrido solo se toman mientras usted conduce.

Su ubicación no se envía al desarrollador, y no se perfila ni se vende. Se almacena en su dispositivo en el historial y los archivos descritos arriba, que salen de su dispositivo mediante la sincronización con iCloud o cuando usted decide compartirlos. Si activa la opción de compartir con ABRP, la ubicación de su vehículo se envía a ABRP (consulte Compartir con ABRP).

## Mapas y navegación

Los mapas, la búsqueda de direcciones y el cálculo de rutas los proporciona MapKit de Apple. Cuando busca una dirección, elige la dirección de un contacto o inicia una navegación, la información de consulta y ubicación necesaria se envía a Apple para devolver un resultado, y se trata conforme a la [política de privacidad de Apple](https://www.apple.com/legal/privacy/). Esta información no se envía al desarrollador.

## Contactos

Si activa **Mostrar contactos en la búsqueda** al añadir un destino en su dispositivo móvil, la aplicación solicita acceso a sus contactos y muestra sus direcciones mientras escribe, en la aplicación y en CarPlay. Cuando elige uno, su dirección se envía a MapKit de Apple para situarla en el mapa, y el nombre del contacto se guarda como etiqueta del destino. La aplicación no almacena sus contactos ni los envía a ningún otro lugar.

## Cámara y fotos

Al tocar el recuadro de foto de una sesión, puede hacer una foto con la cámara o elegir una de su fototeca. Una foto que haga se almacena con la sesión, y el original a resolución completa también se guarda en su fototeca. Para ello, la aplicación solicita acceso solo para añadir: puede añadir fotos a su fototeca, pero no puede ver las fotos que contiene. Cuando elige una foto de su fototeca, el propio selector de iOS da a la aplicación únicamente la foto que usted elige.

## Movimiento y estado físico

La aplicación usa el barómetro de su dispositivo para seguir las subidas y bajadas en el mosaico Altitud de CarPlay y en el mapa Recorrido, algo que importa sobre todo en los vehículos cuyo sistema CarPlay no informa de la altitud. Para ello, solicita acceso a Movimiento y estado físico. Las lecturas del barómetro se usan en su dispositivo y no se envían a ninguna parte.

## Compartir con ABRP (opcional)

ABRP (A Better Routeplanner) es un servicio de planificación de rutas operado por Iternio. El uso compartido está desactivado hasta que active **Compartir datos en vivo con ABRP** en **Ajustes → Compartir datos → ABRP** y vincule un vehículo con el token de su app de ABRP. Al vincularlo, la aplicación envía el token a ABRP para comprobarlo.

Mientras un vehículo vinculado está encendido, la aplicación envía sus datos en vivo directamente desde su dispositivo a los servidores de ABRP (api.iternio.com): la hora; el estado de carga, la energía de la batería y el estado de salud; la potencia, la corriente y la tensión; la velocidad; la ubicación (latitud, longitud, altitud y rumbo); si está cargando, en carga rápida DC o estacionado; el odómetro; las temperaturas de la batería, del habitáculo y exterior; y las presiones de los neumáticos. El VIN no se envía. Las lecturas que no se han podido enviar se conservan en memoria, con un límite, hasta que se restablece la conexión, y se descartan si la aplicación se cierra.

Estos datos no pasan por el desarrollador. ABRP los trata conforme a su propia política de privacidad. Para dejar de compartir, desactive el interruptor o desvincule el vehículo.

## Mosaico Conexión a Internet

El mosaico Conexión a Internet de CarPlay mide su conexión. Mientras el mosaico está en la pantalla de CarPlay, la aplicación solicita una página de prueba vacía aproximadamente cada 30 segundos, alternando entre Cloudflare (cp.cloudflare.com) y Google (connectivitycheck.gstatic.com). Estas solicitudes no contienen ninguna información sobre usted ni sobre su vehículo, aunque, como cualquier solicitud por Internet, revelan su dirección de red a esos servicios. No se realiza ninguna solicitud mientras el mosaico no está en pantalla.

## Actualizaciones de la base de cargadores

La lista de puntos de carga rápida DC viene incluida en la aplicación y funciona sin conexión. No se necesita conexión de red para consultar un cargador ni para navegar hasta él.

Si toca **Ajustes → Navegación → Buscar actualización**, y solo entonces, la aplicación descarga una base de cargadores más reciente. Esto genera dos solicitudes: una para un archivo de manifiesto alojado en theburl.com y otra para el archivo de datos que este indica, alojado en GitHub Releases. Ambas son descargas ordinarias de archivos estáticos, verificadas mediante una suma de comprobación. No se envía ninguna información sobre usted, su dispositivo o su vehículo con estas solicitudes, y no existe ninguna comprobación de actualización automática ni periódica.

## Sincronización con iCloud

Ambos tipos de sincronización están activados de forma predeterminada y pueden desactivarse en **Ajustes → iCloud**.

* **Ajustes** — Mientras **Sincronizar con iCloud** está activado, los ajustes de la aplicación, los destinos guardados, los ajustes de neumáticos y los nombres de los vehículos se sincronizan mediante el almacenamiento de clave-valor de iCloud de Apple con su propia cuenta de iCloud, para que coincidan en todos sus dispositivos. La opción de reconectarse automáticamente a un adaptador se configura en cada dispositivo y no se sincroniza.
* **Historial** — Mientras la sincronización del Historial está activada, su historial de conducción y carga —incluidas las fotos de sesiones, el lugar guardado con una sesión de carga y la ruta del Recorrido de cada trayecto— se sincroniza mediante CloudKit de Apple con su propia cuenta privada de iCloud, de modo que se mantenga coherente entre su iPhone, iPad y Mac.

Ambos tipos de datos se almacenan en su iCloud personal, se rigen por la política de privacidad de Apple y nunca se envían al desarrollador ni a ningún servidor de terceros: el desarrollador no tiene acceso a ellos. Si desactiva ambas sincronizaciones, todos los datos permanecen únicamente en su dispositivo.

## Bluetooth

La aplicación se comunica con su adaptador OBD-II mediante Bluetooth: Bluetooth Low Energy (BLE) para la mayoría de los adaptadores, y Bluetooth Classic, a través del framework External Accessory de Apple, para el OBDLink MX+, el Vgate vLinker FS y el Vgate vLinker MS. Toda la comunicación Bluetooth se produce directamente entre su dispositivo y el adaptador. No se transmiten datos Bluetooth a ningún servidor ni a terceros.

## Datos del vehículo

La aplicación lee datos de diagnóstico del ordenador de a bordo de su vehículo a través del puerto OBD-II. Estos datos incluyen el estado de la batería, temperaturas, tensiones, presiones de neumáticos y otras lecturas de sensores. Estos datos se muestran y se almacenan en su dispositivo, y no se transmiten a ninguna parte salvo a su propio iCloud mientras la sincronización del Historial está activada, y a ABRP si activa el uso compartido.

## Notificaciones

Si activa el recordatorio de desconexión, la aplicación usa notificaciones locales para recordarle que desconecte el adaptador OBD-II cuando el coche se apaga. No se envían datos de notificación a ningún servidor.

## Conservación de datos

Todos los datos se almacenan en su dispositivo. Los archivos de registro y las grabaciones pueden eliminarse mediante la app Archivos de iOS. Desinstalar la aplicación elimina todos los datos almacenados localmente, incluidos los ajustes, los destinos guardados y la información guardada del adaptador. Las fotos que la aplicación guardó en su fototeca permanecen allí hasta que usted las elimine. Si activó la sincronización con iCloud, su historial también permanece en su cuenta de iCloud hasta que lo elimine desde la aplicación o desactive la sincronización. Los datos ya enviados a ABRP los conserva ABRP conforme a su propia política.

## Privacidad de los menores

La aplicación no recopila conscientemente datos de menores de 13 años.

## Cambios en esta política

Si esta política de privacidad se actualiza, la versión revisada se publicará en esta página con una fecha actualizada.

## Contacto

Si tiene preguntas sobre esta política de privacidad, [abra una incidencia](https://github.com/gburlingame/ioniq-app/issues) en GitHub o escriba a [greg@theburl.com](mailto:greg@theburl.com).
