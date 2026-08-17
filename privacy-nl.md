---
layout: default
title: Privacybeleid
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <strong>Nederlands</strong> · <a href="privacy-de">Deutsch</a> · <a href="privacy-fr">Français</a> · <a href="privacy-es">Español</a> · <a href="privacy-sv">Svenska</a> · <a href="privacy-it">Italiano</a> · <a href="privacy-ko">한국어</a> · <a href="privacy-tr">Türkçe</a> · <a href="privacy-ja">日本語</a>
</div>

# Privacybeleid

**Laatst bijgewerkt: 17 augustus 2026**

EV Dashboard ("de app") is ontwikkeld door Greg Burlingame. Dit privacybeleid beschrijft hoe de app met uw gegevens omgaat.

## Gegevensverzameling

EV Dashboard verzamelt, verzendt of verkoopt **geen** persoonlijke gegevens aan derden. De app heeft geen server, geen account en geen inlog. De app bevat geen analyses, advertenties of tracking van welke aard dan ook en uploadt uw gegevens nooit ergens naartoe.

## Gegevens die op uw toestel worden bewaard

De app bewaart de volgende gegevens lokaal op uw toestel:

* **Voertuigdiagnosegegevens** — Accustatus, celspanningen, temperaturen, laadgegevens, bandenspanningen en andere sensormetingen van uw voertuig worden in het geheugen gehouden terwijl de app draait. Deze gegevens blijven niet bewaard tussen het starten van de app, tenzij u een opnamefunctie gebruikt.
* **Rit- en laadgeschiedenis** — Wanneer u de Geschiedenis-functie gebruikt, worden samenvattingen en opgenomen signaalwaarden van uw ritten en laadsessies (laadtoestand, energie, temperaturen en andere metingen) op uw toestel bewaard zodat u ze later kunt bekijken. Bij een sessie kan ook de locatie worden bewaard waar deze plaatsvond, zodat die op een kaart getoond kan worden.
* **App-instellingen** — Uw voorkeuren (eenheden, taal, weergave, thema's, grafiekinstellingen, adapterkeuze, CarPlay-tegelindelingen) worden lokaal opgeslagen met UserDefaults.
* **Bewaarde bestemmingen** — Adressen die u voor navigatie bewaart, en uw recente bestemmingen, worden lokaal op uw toestel opgeslagen.
* **Bluetooth-apparaatgegevens** — De identificatie en de naam van uw gekoppelde OBD-II-adapter worden lokaal opgeslagen zodat de app automatisch opnieuw verbinding kan maken.
* **App-activiteitenlogboek** — Een logbestand met gebeurtenissen rond de levenscyclus van de app, de Bluetooth-verbinding, adapterinterferentie en de opslag van de geschiedenis. Het wordt alleen gedeeld wanneer u expliciet de knop Delen gebruikt.
* **Ritdiagnostiek-recorder** — Een logbestand per rit met GPS-posities, snelheidsmetingen en afstandsberekeningen, gebruikt om de nauwkeurigheid van afstand en navigatie te onderzoeken. Het wordt alleen gedeeld wanneer u expliciet de knop Delen gebruikt.
* **Diagnose-opnames en snapshotlogboeken** — Als u de diagnose-opname of de snapshotvergelijking gebruikt, wordt lokaal een logbestand bewaard met Bluetooth-gebeurtenissen, adaptercommando's en ruwe voertuiggegevens. Het wordt alleen gedeeld wanneer u expliciet de knop Delen gebruikt.

## Locatie

EV Dashboard gebruikt uw locatie om uw positie op de CarPlay-kaart te tonen, route-instructies te geven, tijdens het rijden de ritafstand en efficiëntie te meten en laders in de buurt te vinden.

De app vraagt uitsluitend toegang "Tijdens gebruik van de app". De app vraagt nooit om "Altijd"-toegang. Omdat de ritafstand tijdens een rit doorlopend wordt gemeten, kunnen locatie-updates doorlopen terwijl de app op de achtergrond staat of terwijl u een andere app gebruikt — dit stopt wanneer de rit eindigt.

Uw locatie wordt op uw toestel gebruikt en wordt niet naar de ontwikkelaar gestuurd. Ze wordt niet verzameld, niet geprofileerd en niet verkocht. Locatiegegevens kunnen worden weggeschreven naar de hierboven beschreven bestanden (de Ritdiagnostiek-recorder en de locatie die bij een sessie wordt bewaard); die verlaten uw toestel alleen als u ervoor kiest ze te delen.

## Kaarten en navigatie

Kaarten, adreszoekopdrachten en routeberekening worden geleverd door MapKit van Apple. Wanneer u een adres zoekt of navigatie start, wordt de daarvoor benodigde zoek- en locatie-informatie naar Apple gestuurd om een resultaat te geven, en verwerkt volgens het [privacybeleid van Apple](https://www.apple.com/legal/privacy/). Deze informatie wordt niet naar de ontwikkelaar gestuurd.

## Updates van de laderdatabase

De lijst met DC-snellaadlocaties zit in de app en werkt offline. Er is geen netwerkverbinding nodig om een lader te bekijken of ernaartoe te navigeren.

Als u op **Instellingen → Navigatie → Zoek naar update** tikt, en alleen dan, downloadt de app een nieuwere laderdatabase. Daarbij worden twee verzoeken gedaan: één voor een manifestbestand op theburl.com en één voor het databestand dat daarin genoemd wordt, gehost op GitHub Releases. Beide zijn gewone downloads van statische bestanden, geverifieerd met een controlegetal. Er wordt geen informatie over u, uw toestel of uw voertuig meegestuurd, en er is geen automatische of periodieke controle op updates.

## iCloud-synchronisatie (optioneel)

Als u iCloud-synchronisatie inschakelt, wordt uw rit- en laadgeschiedenis — inclusief de locatie die bij een sessie is bewaard — via CloudKit van Apple gesynchroniseerd met uw eigen privé-iCloud-account, zodat deze gelijk blijft op uw iPhone, iPad en Mac. Deze gegevens worden opgeslagen in uw persoonlijke iCloud, vallen onder het privacybeleid van Apple en worden nooit naar de ontwikkelaar of een server van derden gestuurd — de ontwikkelaar heeft er geen toegang toe. Als u iCloud-synchronisatie uit laat staan, blijven alle gegevens alleen op uw toestel.

## Bluetooth

De app communiceert met uw OBD-II-adapter via Bluetooth Low Energy (BLE). Alle Bluetooth-communicatie vindt rechtstreeks plaats tussen uw toestel en de adapter. Er worden geen Bluetooth-gegevens naar een server of derde partij verzonden.

## Voertuiggegevens

De app leest diagnosegegevens uit de boordcomputer van uw voertuig via de OBD-II-poort. Deze gegevens omvatten accustatus, temperaturen, spanningen, bandenspanningen en andere sensormetingen. Deze gegevens worden op uw toestel getoond en worden nergens naartoe verzonden.

## Meldingen

Als u de ontkoppelherinnering inschakelt, gebruikt de app lokale meldingen om u eraan te herinneren de OBD-II-adapter los te koppelen wanneer de auto wordt uitgezet. Er worden geen meldingsgegevens naar een server gestuurd.

## Gegevensbewaring

Alle gegevens worden op uw toestel bewaard. Logbestanden en opnames kunnen worden verwijderd via de Bestanden-app van iOS. Het verwijderen van de app wist alle lokaal opgeslagen gegevens, inclusief instellingen, bewaarde bestemmingen en bewaarde adaptergegevens. Als u iCloud-synchronisatie hebt ingeschakeld, blijft uw geschiedenis ook in uw iCloud-account staan totdat u deze in de app verwijdert of de synchronisatie uitschakelt.

## Privacy van kinderen

De app verzamelt niet bewust gegevens van kinderen jonger dan 13 jaar.

## Wijzigingen in dit beleid

Als dit privacybeleid wordt bijgewerkt, wordt de herziene versie op deze pagina geplaatst met een bijgewerkte datum.

## Contact

Als u vragen hebt over dit privacybeleid, [open dan een issue](https://github.com/gburlingame/ioniq-app/issues) op GitHub of stuur een e-mail naar [greg@theburl.com](mailto:greg@theburl.com).
