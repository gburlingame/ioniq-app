---
layout: default
title: Datenschutzrichtlinie
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <a href="privacy-nl">Nederlands</a> · <strong>Deutsch</strong> · <a href="privacy-fr">Français</a> · <a href="privacy-es">Español</a> · <a href="privacy-sv">Svenska</a> · <a href="privacy-it">Italiano</a> · <a href="privacy-ko">한국어</a> · <a href="privacy-tr">Türkçe</a> · <a href="privacy-ja">日本語</a>
</div>

# Datenschutzrichtlinie

**Zuletzt aktualisiert: 17. August 2026**

EV Dashboard ("die App") wird von Greg Burlingame entwickelt. Diese Datenschutzrichtlinie beschreibt, wie die App mit Ihren Daten umgeht.

## Datenerhebung

EV Dashboard erhebt, überträgt oder verkauft **keine** personenbezogenen Daten an Dritte. Die App hat kein Backend, kein Konto und keine Anmeldung. Sie enthält keinerlei Analysen, Werbung oder Tracking und lädt Ihre Daten niemals irgendwohin hoch.

## Auf Ihrem Gerät gespeicherte Daten

Die App speichert die folgenden Daten lokal auf Ihrem Gerät:

* **Fahrzeugdiagnosedaten** — Batteriestatus, Zellspannungen, Temperaturen, Ladedaten, Reifendrücke und andere Sensormesswerte Ihres Fahrzeugs werden im Speicher gehalten, während die App läuft. Diese Daten werden nicht zwischen App-Starts gespeichert, es sei denn, Sie verwenden eine Aufzeichnungsfunktion.
* **Fahr- und Ladehistorie** — Wenn Sie die Historie-Funktion verwenden, werden Zusammenfassungen und aufgezeichnete Signalwerte Ihrer Fahrten und Ladevorgänge (Ladezustand, Energie, Temperaturen und andere Messwerte) auf Ihrem Gerät gespeichert, damit Sie sie später ansehen können. Zu einer Sitzung kann auch der Ort gespeichert werden, an dem sie stattfand, damit er auf einer Karte angezeigt werden kann.
* **App-Einstellungen** — Ihre Einstellungen (Einheiten, Sprache, Erscheinungsbild, Designs, Diagramm-Einstellungen, Adapterauswahl, CarPlay-Kachellayouts) werden lokal mit UserDefaults gespeichert.
* **Gespeicherte Ziele** — Adressen, die Sie für die Navigation speichern, sowie Ihre zuletzt verwendeten Ziele werden lokal auf Ihrem Gerät gespeichert.
* **Bluetooth-Geräteinformationen** — Die Kennung und der Name Ihres gekoppelten OBD-II-Adapters werden lokal gespeichert, damit die App automatisch wieder eine Verbindung herstellen kann.
* **App-Aktivitätsprotokoll** — Eine Protokolldatei mit Ereignissen zum App-Lebenszyklus, zur Bluetooth-Verbindung, zu Adapterkonflikten und zur Speicherung der Historie. Sie wird nur geteilt, wenn Sie explizit die Teilen-Taste verwenden.
* **Fahrtdiagnose-Aufzeichnung** — Eine Protokolldatei je Fahrt mit GPS-Positionen, Geschwindigkeitswerten und Distanzberechnungen, die der Fehlersuche bei Distanz- und Navigationsgenauigkeit dient. Sie wird nur geteilt, wenn Sie explizit die Teilen-Taste verwenden.
* **Diagnoseaufzeichnungen und Snapshot-Protokolle** — Wenn Sie die Diagnoseaufzeichnung oder die Snapshot-Vergleichsfunktion verwenden, wird eine Protokolldatei lokal gespeichert, die Bluetooth-Ereignisse, Adapterbefehle und rohe Fahrzeugdaten enthält. Sie wird nur geteilt, wenn Sie explizit die Teilen-Taste verwenden.

## Standort

EV Dashboard verwendet Ihren Standort, um Ihre Position auf der CarPlay-Karte anzuzeigen, Abbiegehinweise zu geben, Fahrtstrecke und Effizienz während der Fahrt zu messen und Ladesäulen in der Nähe zu finden.

Die App fordert ausschließlich den Zugriff "Beim Verwenden der App" an. Sie fordert niemals den Zugriff "Immer" an. Da die Fahrtstrecke während einer Fahrt fortlaufend gemessen wird, können Standortaktualisierungen weiterlaufen, während die App im Hintergrund ist oder Sie eine andere App verwenden — dies endet mit dem Ende der Fahrt.

Ihr Standort wird auf Ihrem Gerät verwendet und nicht an den Entwickler gesendet. Er wird nicht erhoben, nicht zu Profilen verarbeitet und nicht verkauft. Standortdaten können in die oben beschriebenen Dateien auf dem Gerät geschrieben werden (die Fahrtdiagnose-Aufzeichnung und der zu einer Sitzung gespeicherte Ort); diese verlassen Ihr Gerät nur, wenn Sie sie selbst teilen.

## Karten und Navigation

Karten, Adresssuche und Routenberechnung werden von Apples MapKit bereitgestellt. Wenn Sie eine Adresse suchen oder eine Navigation starten, werden die dafür erforderlichen Anfrage- und Standortinformationen an Apple gesendet, um ein Ergebnis zu liefern, und unterliegen der [Datenschutzrichtlinie von Apple](https://www.apple.com/legal/privacy/). Diese Informationen werden nicht an den Entwickler gesendet.

## Aktualisierungen der Ladesäulen-Datenbank

Die Liste der DC-Schnellladestandorte ist in der App enthalten und funktioniert offline. Für das Durchsuchen einer Ladesäule oder die Navigation dorthin ist keine Internetverbindung erforderlich.

Wenn Sie **Einstellungen → Navigation → Nach Update suchen** antippen, und nur dann, lädt die App eine neuere Ladesäulen-Datenbank herunter. Dabei werden zwei Anfragen gestellt: eine für eine Manifest-Datei auf theburl.com und eine für die darin genannte Datendatei, die über GitHub Releases bereitgestellt wird. Beides sind gewöhnliche Downloads statischer Dateien, die anhand einer Prüfsumme verifiziert werden. Es werden keinerlei Informationen über Sie, Ihr Gerät oder Ihr Fahrzeug mitgesendet, und es gibt keine automatische oder periodische Update-Prüfung.

## iCloud-Synchronisierung (optional)

Wenn Sie die iCloud-Synchronisierung aktivieren, wird Ihre Fahr- und Ladehistorie — einschließlich eines zu einer Sitzung gespeicherten Ortes — über Apples CloudKit mit Ihrem eigenen privaten iCloud-Konto synchronisiert, sodass sie auf iPhone, iPad und Mac konsistent bleibt. Diese Daten werden in Ihrer persönlichen iCloud gespeichert, unterliegen der Datenschutzrichtlinie von Apple und werden niemals an den Entwickler oder einen Drittanbieter-Server gesendet – der Entwickler hat keinen Zugriff darauf. Wenn Sie die iCloud-Synchronisierung deaktiviert lassen, verbleiben alle Daten ausschließlich auf Ihrem Gerät.

## Bluetooth

Die App kommuniziert mit Ihrem OBD-II-Adapter über Bluetooth Low Energy (BLE). Die gesamte Bluetooth-Kommunikation findet direkt zwischen Ihrem Gerät und dem Adapter statt. Es werden keine Bluetooth-Daten an einen Server oder Dritte übertragen.

## Fahrzeugdaten

Die App liest Diagnosedaten vom Bordcomputer Ihres Fahrzeugs über den OBD-II-Anschluss. Diese Daten umfassen Batteriestatus, Temperaturen, Spannungen, Reifendrücke und andere Sensormesswerte. Diese Daten werden auf Ihrem Gerät angezeigt und nirgendwohin übertragen.

## Benachrichtigungen

Wenn Sie die Erinnerung zum Abstecken aktivieren, verwendet die App lokale Benachrichtigungen, um Sie daran zu erinnern, den OBD-II-Adapter abzustecken, wenn das Auto ausgeschaltet wird. Es werden keine Benachrichtigungsdaten an einen Server gesendet.

## Datenspeicherung

Alle Daten werden auf Ihrem Gerät gespeichert. Protokolldateien und Aufzeichnungen können über die iOS-Dateien-App gelöscht werden. Das Deinstallieren der App entfernt alle lokal gespeicherten Daten einschließlich Einstellungen, gespeicherter Ziele und gespeicherter Adapterinformationen. Wenn Sie die iCloud-Synchronisierung aktiviert haben, verbleibt Ihre Historie außerdem in Ihrem iCloud-Konto, bis Sie sie in der App löschen oder die Synchronisierung deaktivieren.

## Datenschutz für Kinder

Die App erhebt wissentlich keine Daten von Kindern unter 13 Jahren.

## Änderungen dieser Richtlinie

Wenn diese Datenschutzrichtlinie aktualisiert wird, wird die überarbeitete Version auf dieser Seite mit einem aktualisierten Datum veröffentlicht.

## Kontakt

Wenn Sie Fragen zu dieser Datenschutzrichtlinie haben, öffnen Sie bitte ein [Issue](https://github.com/gburlingame/ioniq-app/issues) auf GitHub oder senden Sie eine E-Mail an [greg@theburl.com](mailto:greg@theburl.com).
