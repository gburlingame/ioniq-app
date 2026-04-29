---
layout: default
title: Política de privacidad
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <a href="privacy-nl">Nederlands</a> · <a href="privacy-de">Deutsch</a> · <a href="privacy-fr">Français</a> · <strong>Español</strong> · <a href="privacy-sv">Svenska</a>
</div>

# Política de privacidad

**Última actualización: 29 de abril de 2026**

IONIQ 5 Companion ("la aplicación") es desarrollada por Greg Burlingame. Esta política de privacidad describe cómo la aplicación maneja sus datos.

## Recopilación de datos

IONIQ 5 Companion **no** recopila, transmite ni vende datos personales a terceros. La aplicación no contiene análisis, publicidad ni rastreo de ningún tipo.

## Datos almacenados en su dispositivo

La aplicación almacena los siguientes datos localmente en su dispositivo:

* **Datos de diagnóstico del vehículo** — El estado de la batería, voltajes de celdas, temperaturas, datos de carga, presiones de neumáticos y otras lecturas de sensores de su vehículo se almacenan en memoria mientras la aplicación está en funcionamiento. Estos datos no se conservan entre inicios de la aplicación, a menos que utilice la función de grabación de diagnósticos.
* **Configuración de la aplicación** — Sus preferencias (unidades, idioma, apariencia, configuración de gráficos temporales, selección de adaptador) se almacenan localmente usando UserDefaults.
* **Información del dispositivo Bluetooth** — El identificador y nombre de su adaptador OBD-II emparejado se almacenan localmente para que la aplicación pueda reconectarse automáticamente.
* **Grabaciones de diagnóstico** — Si utiliza la función "Iniciar diagnóstico", se guarda un archivo de registro en el almacenamiento local de su dispositivo. Este archivo contiene eventos Bluetooth, comandos del adaptador y datos brutos del vehículo. Solo se comparte cuando usted utiliza explícitamente el botón de compartir.
* **Registros de snapshots A-B-C** — Si utiliza la función de comparación de snapshots, se guarda un archivo de registro localmente con datos brutos de la ECU. Solo se comparte cuando usted utiliza explícitamente el botón de compartir.

## Sin servicios en la nube

La aplicación no utiliza iCloud, CloudKit ni ningún almacenamiento en la nube. Todos los datos permanecen en su dispositivo.

## Sin integraciones de terceros

La aplicación no se integra con ningún servicio de terceros. No hay creación de cuentas, no hay inicio de sesión y no hay carga de datos.

## Bluetooth

La aplicación se comunica con su adaptador OBD-II a través de Bluetooth Low Energy (BLE). Toda la comunicación Bluetooth se realiza directamente entre su dispositivo y el adaptador. No se transmiten datos Bluetooth a ningún servidor o tercero.

## Datos del vehículo

La aplicación lee datos de diagnóstico del ordenador de a bordo de su vehículo a través del puerto OBD-II. Estos datos incluyen el estado de la batería, temperaturas, voltajes, presiones de neumáticos y otras lecturas de sensores. Estos datos se muestran en su dispositivo y no se transmiten a ningún lugar.

## Notificaciones

Si activa el recordatorio de desconexión, la aplicación utiliza notificaciones locales para recordarle que desconecte el adaptador OBD-II cuando el coche se apague. No se envían datos de notificación a ningún servidor.

## Retención de datos

Todos los datos se almacenan en su dispositivo. Las grabaciones de diagnóstico y los registros de snapshots se pueden eliminar a través de la aplicación Archivos de iOS. La desinstalación de la aplicación elimina todos los datos almacenados localmente, incluida la configuración y la información del adaptador guardado.

## Privacidad de los niños

La aplicación no recopila a sabiendas datos de niños menores de 13 años.

## Cambios en esta política

Si esta política de privacidad se actualiza, la versión revisada se publicará en esta página con una fecha actualizada.

## Contacto

Si tiene preguntas sobre esta política de privacidad, por favor [abra un issue](https://github.com/gburlingame/ioniq-app/issues) en GitHub o envíe un correo electrónico a [greg@theburl.com](mailto:greg@theburl.com).
