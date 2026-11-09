---
layout: default
title: Datenschutzrichtlinie
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <a href="privacy-nl">Nederlands</a> · <strong>Deutsch</strong> · <a href="privacy-fr">Français</a> · <a href="privacy-es">Español</a> · <a href="privacy-sv">Svenska</a> · <a href="privacy-it">Italiano</a> · <a href="privacy-ko">한국어</a> · <a href="privacy-tr">Türkçe</a> · <a href="privacy-ja">日本語</a>
</div>

# Datenschutzrichtlinie

**Zuletzt aktualisiert: 9. November 2026**

EV Dashboard ("die App") wird von Greg Burlingame entwickelt. Diese Datenschutzrichtlinie beschreibt, wie die App mit Ihren Daten umgeht.

## Datenerhebung

EV Dashboard hat kein Backend, kein Konto und keine Anmeldung. Die App enthält keinerlei Analysen, Werbung oder Tracking. Der Entwickler erhält Ihre Daten niemals, und nichts wird verkauft.

Ihre Daten verlassen Ihr Gerät nur in den folgenden Fällen, die jeweils weiter unten beschrieben sind:

* **Teilen mit ABRP** — deaktiviert, bis Sie es aktivieren und ein Fahrzeug verknüpfen; dann werden die Live-Daten dieses Fahrzeugs direkt an ABRP gesendet.
* **iCloud-Synchronisierung** — Ihre Einstellungen und Ihre Historie werden mit Ihrem eigenen privaten iCloud-Konto synchronisiert.
* **Apple Karten** — Adresssuchen, von Ihnen ausgewählte Kontaktadressen und Routenanfragen gehen an Apples MapKit.
* **Von Ihnen geteilte Dateien** — Protokolle, Aufzeichnungen, Exporte und Karten zum Teilen verlassen Ihr Gerät nur, wenn Sie auf die Teilen-Taste tippen.

Die Internetverbindung-Kachel und die Aktualisierungen der Ladesäulen-Datenbank stellen ebenfalls Netzwerkanfragen. Diese enthalten keine Informationen über Sie oder Ihr Fahrzeug.

## Auf Ihrem Gerät gespeicherte Daten

Die App speichert die folgenden Daten lokal auf Ihrem Gerät:

* **Fahrzeugdiagnosedaten** — Batteriestatus, Zellspannungen, Temperaturen, Ladedaten, Reifendrücke und andere Sensormesswerte Ihres Fahrzeugs werden im Speicher gehalten, während die App läuft. Diese Daten werden nicht zwischen App-Starts gespeichert, es sei denn, Sie verwenden eine Aufzeichnungsfunktion.
* **Fahr- und Ladehistorie** — Wenn Sie die Historie-Funktion verwenden, werden Zusammenfassungen und aufgezeichnete Signalwerte Ihrer Fahrten und Ladevorgänge (Ladezustand, Energie, Temperaturen und andere Messwerte) auf Ihrem Gerät gespeichert, damit Sie sie später ansehen können. Zu einer Ladesitzung kann der Ort gespeichert werden, an dem sie stattfand. Zu einer Fahrt wird ihre Route gespeichert — Ihr Standort etwa einmal pro Sekunde während der Fahrt —, damit sie auf ihrer Strecke-Karte angezeigt werden kann. Sie können dies unter **Einstellungen → Fahrsitzungen → Strecke aufzeichnen** deaktivieren oder die Route einer Fahrt auf ihrer Strecke-Karte entfernen.
* **Sitzungsfotos** — Ein Foto, das Sie einer Lade- oder Fahrsitzung hinzufügen, wird mit dieser Sitzung gespeichert.
* **App-Einstellungen** — Ihre Einstellungen (Einheiten, Sprache, Erscheinungsbild, Designs, Diagramm-Einstellungen, Adapterauswahl, CarPlay-Kachellayouts, Ladesäulenfilter, Reifeneinstellungen und Fahrzeugnamen) werden auf Ihrem Gerät gespeichert und über iCloud synchronisiert, solange „Mit iCloud synchronisieren“ aktiviert ist.
* **Gespeicherte Ziele** — Adressen, die Sie für die Navigation speichern, sowie Ihre zuletzt verwendeten Ziele werden auf Ihrem Gerät gespeichert und mit Ihren Einstellungen synchronisiert.
* **Bluetooth-Geräteinformationen** — Die Kennung und der Name Ihres gekoppelten OBD-II-Adapters werden lokal gespeichert, damit die App automatisch wieder eine Verbindung herstellen kann.
* **ABRP-Verknüpfungstoken** — Wenn Sie ein Fahrzeug mit ABRP verknüpfen, wird das Token, das Sie aus der ABRP-App einfügen, im Schlüsselbund Ihres Geräts gespeichert. Wenn Sie die Verknüpfung des Fahrzeugs aufheben, wird es gelöscht.
* **App-Aktivitätsprotokoll** — Eine Protokolldatei mit Ereignissen zum App-Lebenszyklus, zur Bluetooth-Verbindung, zu Adapterkonflikten und zur Speicherung der Historie. Sie wird nur geteilt, wenn Sie explizit die Teilen-Taste verwenden.
* **Fahrtdiagnose-Aufzeichnung** — Eine Protokolldatei je Fahrt mit GPS-Messungen (Position, Fahrtrichtung, Geschwindigkeit und Höhe), Geschwindigkeitswerten des Fahrzeugs und Distanzberechnungen, die der Fehlersuche bei Distanz-, Höhen- und Navigationsgenauigkeit dient. Sie wird nur geteilt, wenn Sie explizit die Teilen-Taste verwenden.
* **Diagnoseaufzeichnungen und Snapshot-Protokolle** — Wenn Sie die Diagnoseaufzeichnung oder die Snapshot-Vergleichsfunktion verwenden, wird eine Protokolldatei lokal gespeichert, die Bluetooth-Ereignisse, Adapterbefehle und rohe Fahrzeugdaten enthält. Sie wird nur geteilt, wenn Sie explizit die Teilen-Taste verwenden.

## Standort

EV Dashboard verwendet Ihren Standort, um Ihre Position auf der CarPlay-Karte anzuzeigen, Abbiegehinweise zu geben, Fahrtstrecke und Effizienz zu messen, die Strecke einer Fahrt aufzuzeichnen, Ihre Höhe anzuzeigen und Ladesäulen in der Nähe zu finden.

Die App fordert ausschließlich den Zugriff "Beim Verwenden der App" an. Sie fordert niemals den Zugriff "Immer" an. Standortaktualisierungen können weiterlaufen, während die App im Hintergrund ist oder Sie eine andere App verwenden: Wenn Sie die App öffnen, während sie mit Ihrem Fahrzeug verbunden ist, hält sie eine Standortsitzung im Hintergrund aufrecht, bis das Fahrzeug ausgeschaltet wird oder der Adapter außerhalb der Bluetooth-Reichweite ist, und iOS zeigt währenddessen das Standortsymbol an. GPS-Messungen für die Fahrtstrecke und die Streckenaufzeichnung werden nur während der Fahrt erfasst.

Ihr Standort wird nicht an den Entwickler gesendet und weder zu Profilen verarbeitet noch verkauft. Er wird auf Ihrem Gerät in der Historie und den Dateien gespeichert, die oben beschrieben sind; diese verlassen Ihr Gerät über die iCloud-Synchronisierung oder wenn Sie sie selbst teilen. Wenn Sie das Teilen mit ABRP aktivieren, wird der Standort Ihres Fahrzeugs an ABRP gesendet (siehe Abschnitt Teilen mit ABRP).

## Karten und Navigation

Karten, Adresssuche und Routenberechnung werden von Apples MapKit bereitgestellt. Wenn Sie eine Adresse suchen, die Adresse eines Kontakts auswählen oder eine Navigation starten, werden die dafür erforderlichen Anfrage- und Standortinformationen an Apple gesendet, um ein Ergebnis zu liefern, und unterliegen der [Datenschutzrichtlinie von Apple](https://www.apple.com/legal/privacy/). Diese Informationen werden nicht an den Entwickler gesendet.

## Kontakte

Wenn Sie beim Hinzufügen eines Ziels auf Ihrem Mobilgerät **Kontakte in der Suche anzeigen** aktivieren, fragt die App nach Zugriff auf Ihre Kontakte und zeigt deren Adressen während der Eingabe an, in der App und in CarPlay. Wenn Sie einen Kontakt auswählen, wird seine Adresse an Apples MapKit gesendet, um sie auf der Karte zu platzieren, und der Name des Kontakts wird als Bezeichnung des Ziels gespeichert. Die App speichert Ihre Kontakte nicht und sendet sie nirgendwo anders hin.

## Kamera und Fotos

Wenn Sie auf das Fotofeld einer Sitzung tippen, können Sie mit der Kamera ein Foto aufnehmen oder eines aus Ihrer Mediathek auswählen. Ein aufgenommenes Foto wird mit der Sitzung gespeichert, und das Original in voller Auflösung wird außerdem in Ihrer Fotomediathek gesichert. Dafür fragt die App nur nach Zugriff zum Hinzufügen: Die App kann Fotos zu Ihrer Mediathek hinzufügen, die Fotos darin aber nicht sehen. Wenn Sie ein Foto aus Ihrer Mediathek auswählen, gibt die Fotoauswahl von iOS der App nur das Foto, das Sie auswählen.

## Bewegung & Fitness

Die App nutzt das Barometer Ihres Geräts, um Anstiege und Gefälle für die Höhe-Kachel in CarPlay und die Strecke-Karte zu verfolgen, was vor allem bei Fahrzeugen wichtig ist, deren CarPlay-System keine Höhe meldet. Dafür fragt die App nach Zugriff auf „Bewegung & Fitness“. Barometerwerte werden auf Ihrem Gerät verwendet und nirgendwohin gesendet.

## Teilen mit ABRP (optional)

ABRP (A Better Routeplanner) ist ein Routenplanungsdienst von Iternio. Das Teilen ist deaktiviert, bis Sie unter **Einstellungen → Datenfreigabe → ABRP** die Option **Live-Daten mit ABRP teilen** aktivieren und ein Fahrzeug mit dem Token aus Ihrer ABRP-App verknüpfen. Beim Verknüpfen sendet die App das Token an ABRP, um es zu prüfen.

Während ein verknüpftes Fahrzeug eingeschaltet ist, sendet die App dessen Live-Daten direkt von Ihrem Gerät an die Server von ABRP (api.iternio.com): die Uhrzeit; Ladezustand, Batterieenergie und Gesundheitszustand; Leistung, Strom und Spannung; Geschwindigkeit; Standort (Breitengrad, Längengrad, Höhe und Fahrtrichtung); ob das Fahrzeug lädt, per DC schnellgeladen wird oder geparkt ist; den Kilometerstand; Batterie-, Innenraum- und Außentemperatur; und Reifendrücke. Die VIN wird nicht gesendet. Messwerte, die nicht gesendet werden konnten, werden bis zu einer Obergrenze im Speicher gehalten, bis die Verbindung wiederhergestellt ist, und verworfen, wenn die App geschlossen wird.

Diese Daten laufen nicht über den Entwickler. ABRP verarbeitet sie gemäß seiner eigenen Datenschutzrichtlinie. Um das Teilen zu beenden, schalten Sie den Schalter aus oder heben Sie die Verknüpfung des Fahrzeugs auf.

## Internetverbindung-Kachel

Die Internetverbindung-Kachel in CarPlay misst Ihre Verbindung. Solange die Kachel auf Ihrem CarPlay-Bildschirm angezeigt wird, ruft die App etwa alle 30 Sekunden eine leere Testseite ab, abwechselnd bei Cloudflare (cp.cloudflare.com) und Google (connectivitycheck.gstatic.com). Diese Anfragen enthalten keine Informationen über Sie oder Ihr Fahrzeug, geben jedoch wie jede Internetanfrage Ihre Netzwerkadresse an diese Dienste preis. Solange die Kachel nicht angezeigt wird, werden keine Anfragen gestellt.

## Aktualisierungen der Ladesäulen-Datenbank

Die Liste der DC-Schnellladestandorte ist in der App enthalten und funktioniert offline. Für das Durchsuchen einer Ladesäule oder die Navigation dorthin ist keine Internetverbindung erforderlich.

Wenn Sie **Einstellungen → Navigation → Nach Update suchen** antippen, und nur dann, lädt die App eine neuere Ladesäulen-Datenbank herunter. Dabei werden zwei Anfragen gestellt: eine für eine Manifest-Datei auf theburl.com und eine für die darin genannte Datendatei, die über GitHub Releases bereitgestellt wird. Beides sind gewöhnliche Downloads statischer Dateien, die anhand einer Prüfsumme verifiziert werden. Es werden keinerlei Informationen über Sie, Ihr Gerät oder Ihr Fahrzeug mitgesendet, und es gibt keine automatische oder periodische Update-Prüfung.

## iCloud-Synchronisierung

Beide Arten der Synchronisierung sind standardmäßig aktiviert und können unter **Einstellungen → iCloud** deaktiviert werden.

* **Einstellungen** — Solange **Mit iCloud synchronisieren** aktiviert ist, werden Ihre App-Einstellungen, gespeicherten Ziele, Reifeneinstellungen und Fahrzeugnamen über den iCloud-Schlüssel-Wert-Speicher von Apple mit Ihrem eigenen iCloud-Konto synchronisiert, sodass sie auf allen Ihren Geräten übereinstimmen. Ob die App automatisch wieder eine Verbindung zu einem Adapter herstellt, wird auf jedem Gerät einzeln festgelegt und nicht synchronisiert.
* **Verlauf** — Solange die Verlaufssynchronisierung aktiviert ist, wird Ihre Fahr- und Ladehistorie — einschließlich Sitzungsfotos, des zu einer Ladesitzung gespeicherten Ortes und der Strecke jeder Fahrt — über Apples CloudKit mit Ihrem eigenen privaten iCloud-Konto synchronisiert, sodass sie auf iPhone, iPad und Mac konsistent bleibt.

Beide werden in Ihrer persönlichen iCloud gespeichert, unterliegen der Datenschutzrichtlinie von Apple und werden niemals an den Entwickler oder einen Drittanbieter-Server gesendet – der Entwickler hat keinen Zugriff darauf. Wenn Sie beide deaktivieren, verbleiben alle Daten ausschließlich auf Ihrem Gerät.

## Bluetooth

Die App kommuniziert mit Ihrem OBD-II-Adapter über Bluetooth: bei den meisten Adaptern über Bluetooth Low Energy (BLE) und beim OBDLink MX+, Vgate vLinker FS und Vgate vLinker MS über Bluetooth Classic mithilfe von Apples Framework External Accessory. Die gesamte Bluetooth-Kommunikation findet direkt zwischen Ihrem Gerät und dem Adapter statt. Es werden keine Bluetooth-Daten an einen Server oder Dritte übertragen.

## Fahrzeugdaten

Die App liest Diagnosedaten vom Bordcomputer Ihres Fahrzeugs über den OBD-II-Anschluss. Diese Daten umfassen Batteriestatus, Temperaturen, Spannungen, Reifendrücke und andere Sensormesswerte. Diese Daten werden auf Ihrem Gerät angezeigt und gespeichert und nirgendwohin übertragen, außer an Ihre eigene iCloud, solange die Verlaufssynchronisierung aktiviert ist, und an ABRP, wenn Sie das Teilen aktivieren.

## Benachrichtigungen

Wenn Sie die Erinnerung zum Abstecken aktivieren, verwendet die App lokale Benachrichtigungen, um Sie daran zu erinnern, den OBD-II-Adapter abzustecken, wenn das Auto ausgeschaltet wird. Es werden keine Benachrichtigungsdaten an einen Server gesendet.

## Datenspeicherung

Alle Daten werden auf Ihrem Gerät gespeichert. Protokolldateien und Aufzeichnungen können über die iOS-Dateien-App gelöscht werden. Das Deinstallieren der App entfernt alle lokal gespeicherten Daten einschließlich Einstellungen, gespeicherter Ziele und gespeicherter Adapterinformationen. Fotos, die die App in Ihrer Fotomediathek gesichert hat, bleiben dort, bis Sie sie löschen. Wenn Sie die iCloud-Synchronisierung aktiviert haben, verbleibt Ihre Historie außerdem in Ihrem iCloud-Konto, bis Sie sie in der App löschen oder die Synchronisierung deaktivieren. Bereits an ABRP gesendete Daten werden von ABRP gemäß seiner eigenen Richtlinie aufbewahrt.

## Datenschutz für Kinder

Die App erhebt wissentlich keine Daten von Kindern unter 13 Jahren.

## Änderungen dieser Richtlinie

Wenn diese Datenschutzrichtlinie aktualisiert wird, wird die überarbeitete Version auf dieser Seite mit einem aktualisierten Datum veröffentlicht.

## Kontakt

Wenn Sie Fragen zu dieser Datenschutzrichtlinie haben, öffnen Sie bitte ein [Issue](https://github.com/gburlingame/ioniq-app/issues) auf GitHub oder senden Sie eine E-Mail an [greg@theburl.com](mailto:greg@theburl.com).
