---
layout: default
title: Privacybeleid
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <strong>Nederlands</strong> · <a href="privacy-de">Deutsch</a> · <a href="privacy-fr">Français</a> · <a href="privacy-es">Español</a> · <a href="privacy-sv">Svenska</a> · <a href="privacy-it">Italiano</a> · <a href="privacy-ko">한국어</a> · <a href="privacy-tr">Türkçe</a> · <a href="privacy-ja">日本語</a>
</div>

# Privacybeleid

**Laatst bijgewerkt: 9 november 2026**

EV Dashboard ("de app") is ontwikkeld door Greg Burlingame. Dit privacybeleid beschrijft hoe de app met uw gegevens omgaat.

## Gegevensverzameling

EV Dashboard heeft geen server, geen account en geen inlog. De app bevat geen analyses, advertenties of tracking van welke aard dan ook. De ontwikkelaar ontvangt uw gegevens nooit, en er wordt niets verkocht.

Uw gegevens verlaten uw toestel alleen in de volgende gevallen, die hieronder elk worden beschreven:

* **Delen met ABRP** — staat uit totdat u het inschakelt en een voertuig koppelt; het stuurt de live gegevens van dat voertuig rechtstreeks naar ABRP.
* **iCloud-synchronisatie** — uw instellingen en geschiedenis worden gesynchroniseerd met uw eigen privé-iCloud-account.
* **Apple Kaarten** — adreszoekopdrachten, contactadressen die u kiest en routeaanvragen gaan naar MapKit van Apple.
* **Bestanden die u deelt** — logbestanden, opnames, exports en kaarten om te delen verlaten uw toestel alleen wanneer u op Delen tikt.

De Internetverbinding-tegel en de updates van de laderdatabase doen ook netwerkverzoeken. Die bevatten geen informatie over u of uw voertuig.

## Gegevens die op uw toestel worden bewaard

De app bewaart de volgende gegevens lokaal op uw toestel:

* **Voertuigdiagnosegegevens** — Accustatus, celspanningen, temperaturen, laadgegevens, bandenspanningen en andere sensormetingen van uw voertuig worden in het geheugen gehouden terwijl de app draait. Deze gegevens blijven niet bewaard tussen het starten van de app, tenzij u een opnamefunctie gebruikt.
* **Rit- en laadgeschiedenis** — Wanneer u de Geschiedenis-functie gebruikt, worden samenvattingen en opgenomen signaalwaarden van uw ritten en laadsessies (laadtoestand, energie, temperaturen en andere metingen) op uw toestel bewaard zodat u ze later kunt bekijken. Bij een laadsessie kan de locatie worden bewaard waar deze plaatsvond. Bij een rit wordt de route bewaard — uw locatie ongeveer eenmaal per seconde terwijl u rijdt — zodat die op de Route-kaart van de rit getoond kan worden. U kunt dit uitschakelen via **Instellingen → Rijsessies → Route vastleggen**, of de route van een rit verwijderen van de bijbehorende Route-kaart.
* **Sessiefoto's** — Een foto die u aan een laad- of rijsessie toevoegt, wordt bij die sessie bewaard.
* **App-instellingen** — Uw voorkeuren (eenheden, taal, weergave, thema's, grafiekinstellingen, adapterkeuze, CarPlay-tegelindelingen, laderfilters, bandeninstellingen en voertuignamen) worden op uw toestel opgeslagen en via iCloud gesynchroniseerd zolang Synchroniseren met iCloud aanstaat.
* **Bewaarde bestemmingen** — Adressen die u voor navigatie bewaart, en uw recente bestemmingen, worden op uw toestel opgeslagen en samen met uw instellingen gesynchroniseerd.
* **Bluetooth-apparaatgegevens** — De identificatie en de naam van uw gekoppelde OBD-II-adapter worden lokaal opgeslagen zodat de app automatisch opnieuw verbinding kan maken.
* **ABRP-koppeltoken** — Als u een voertuig aan ABRP koppelt, wordt het token dat u uit de ABRP-app plakt bewaard in de sleutelhanger van uw toestel. Als u het voertuig ontkoppelt, wordt het token verwijderd.
* **App-activiteitenlogboek** — Een logbestand met gebeurtenissen rond de levenscyclus van de app, de Bluetooth-verbinding, adapterinterferentie en de opslag van de geschiedenis. Het wordt alleen gedeeld wanneer u expliciet de knop Delen gebruikt.
* **Ritdiagnostiek-recorder** — Een logbestand per rit met GPS-metingen (positie, rijrichting, snelheid en hoogte), snelheidsmetingen van het voertuig en afstandsberekeningen, gebruikt om de nauwkeurigheid van afstand, hoogte en navigatie te onderzoeken. Het wordt alleen gedeeld wanneer u expliciet de knop Delen gebruikt.
* **Diagnose-opnames en snapshotlogboeken** — Als u de diagnose-opname of de snapshotvergelijking gebruikt, wordt lokaal een logbestand bewaard met Bluetooth-gebeurtenissen, adaptercommando's en ruwe voertuiggegevens. Het wordt alleen gedeeld wanneer u expliciet de knop Delen gebruikt.

## Locatie

EV Dashboard gebruikt uw locatie om uw positie op de CarPlay-kaart te tonen, route-instructies te geven, de ritafstand en efficiëntie te meten, de route van een rit vast te leggen, uw hoogte te tonen en laders in de buurt te vinden.

De app vraagt uitsluitend toegang "Tijdens gebruik van de app". De app vraagt nooit om "Altijd"-toegang. Locatie-updates kunnen doorlopen terwijl de app op de achtergrond staat of terwijl u een andere app gebruikt: als u de app opent terwijl deze met uw voertuig verbonden is, houdt de app een locatiesessie op de achtergrond actief totdat het voertuig wordt uitgezet of de adapter buiten Bluetooth-bereik is, en iOS toont in die tijd het locatiesymbool. GPS-metingen voor de ritafstand en de route worden alleen tijdens het rijden gedaan.

Uw locatie wordt niet naar de ontwikkelaar gestuurd en wordt niet geprofileerd of verkocht. Ze wordt op uw toestel bewaard in de geschiedenis en de bestanden die hierboven zijn beschreven; die verlaten uw toestel via iCloud-synchronisatie of wanneer u ervoor kiest ze te delen. Als u het delen met ABRP inschakelt, wordt de locatie van uw voertuig naar ABRP gestuurd (zie het onderdeel Delen met ABRP).

## Kaarten en navigatie

Kaarten, adreszoekopdrachten en routeberekening worden geleverd door MapKit van Apple. Wanneer u een adres zoekt, het adres van een contact kiest of navigatie start, wordt de daarvoor benodigde zoek- en locatie-informatie naar Apple gestuurd om een resultaat te geven, en verwerkt volgens het [privacybeleid van Apple](https://www.apple.com/legal/privacy/). Deze informatie wordt niet naar de ontwikkelaar gestuurd.

## Contacten

Als u **Contacten tonen in zoekresultaten** inschakelt terwijl u op uw mobiele toestel een bestemming toevoegt, vraagt de app om toegang tot uw contacten en toont de app hun adressen terwijl u typt, in de app en in CarPlay. Wanneer u er een kiest, wordt het adres naar MapKit van Apple gestuurd om het op de kaart te plaatsen, en wordt de naam van het contact bewaard als label van de bestemming. De app bewaart uw contacten niet en stuurt ze nergens anders naartoe.

## Camera en foto's

Als u op het fotovak van een sessie tikt, kunt u een foto maken met de camera of er een kiezen uit uw bibliotheek. Een foto die u maakt, wordt bij de sessie bewaard, en het origineel in volledige resolutie wordt ook in uw fotobibliotheek bewaard. Daarvoor vraagt de app alleen toegang om foto's toe te voegen: de app kan foto's aan uw bibliotheek toevoegen, maar kan de foto's daarin niet zien. Wanneer u een foto uit uw bibliotheek kiest, geeft de eigen fotokiezer van iOS de app alleen de foto die u kiest.

## Beweging en fitness

De app gebruikt de barometer van uw toestel om stijgingen en dalingen te volgen voor de Hoogte-tegel in CarPlay en de Route-kaart, wat vooral belangrijk is bij voertuigen waarvan het CarPlay-systeem geen hoogte doorgeeft. Daarvoor vraagt de app toegang tot Beweging en fitness. Barometermetingen worden op uw toestel gebruikt en nergens naartoe gestuurd.

## Delen met ABRP (optioneel)

ABRP (A Better Routeplanner) is een routeplanningsdienst van Iternio. Delen staat uit totdat u **Live gegevens delen met ABRP** inschakelt onder **Instellingen → Gegevens delen → ABRP** en een voertuig koppelt met het token uit uw ABRP-app. Bij het koppelen stuurt de app het token naar ABRP om het te controleren.

Zolang een gekoppeld voertuig aanstaat, stuurt de app de live gegevens ervan rechtstreeks van uw toestel naar de servers van ABRP (api.iternio.com): de tijd; laadtoestand, accu-energie en gezondheidsstaat; vermogen, stroom en spanning; snelheid; locatie (breedtegraad, lengtegraad, hoogte en rijrichting); of het voertuig laadt, aan een DC-snellader laadt of geparkeerd staat; de kilometerstand; accu-, cabine- en buitentemperatuur; en bandenspanningen. Het VIN wordt niet verstuurd. Metingen die niet verstuurd konden worden, worden tot een bepaalde limiet in het geheugen gehouden totdat de verbinding terug is, en worden weggegooid als de app wordt afgesloten.

Deze gegevens gaan niet via de ontwikkelaar. ABRP verwerkt ze volgens zijn eigen privacybeleid. Om het delen te stoppen, zet u de schakelaar uit of ontkoppelt u het voertuig.

## Internetverbinding-tegel

De Internetverbinding-tegel in CarPlay meet uw verbinding. Zolang de tegel op uw CarPlay-scherm staat, vraagt de app ongeveer elke 30 seconden een lege testpagina op, afwisselend bij Cloudflare (cp.cloudflare.com) en Google (connectivitycheck.gstatic.com). Deze verzoeken bevatten geen informatie over u of uw voertuig, hoewel ze, zoals elk internetverzoek, uw netwerkadres aan die diensten prijsgeven. Er worden geen verzoeken gedaan zolang de tegel niet op het scherm staat.

## Updates van de laderdatabase

De lijst met DC-snellaadlocaties zit in de app en werkt offline. Er is geen netwerkverbinding nodig om een lader te bekijken of ernaartoe te navigeren.

Als u op **Instellingen → Navigatie → Zoek naar update** tikt, en alleen dan, downloadt de app een nieuwere laderdatabase. Daarbij worden twee verzoeken gedaan: één voor een manifestbestand op theburl.com en één voor het databestand dat daarin genoemd wordt, gehost op GitHub Releases. Beide zijn gewone downloads van statische bestanden, geverifieerd met een controlegetal. Er wordt geen informatie over u, uw toestel of uw voertuig meegestuurd, en er is geen automatische of periodieke controle op updates.

## iCloud-synchronisatie

Beide soorten synchronisatie staan standaard aan en kunnen worden uitgeschakeld via **Instellingen → iCloud**.

* **Instellingen** — Zolang **Synchroniseren met iCloud** aanstaat, worden uw app-instellingen, bewaarde bestemmingen, bandeninstellingen en voertuignamen via de iCloud-sleutel-waardeopslag van Apple gesynchroniseerd met uw eigen iCloud-account, zodat ze op al uw toestellen overeenkomen. Of de app automatisch opnieuw verbinding maakt met een adapter, wordt per toestel ingesteld en niet gesynchroniseerd.
* **Geschiedenis** — Zolang synchronisatie van de geschiedenis aanstaat, wordt uw rit- en laadgeschiedenis — inclusief sessiefoto's, de locatie die bij een laadsessie is bewaard en de route van elke rit — via CloudKit van Apple gesynchroniseerd met uw eigen privé-iCloud-account, zodat deze gelijk blijft op uw iPhone, iPad en Mac.

Beide worden opgeslagen in uw persoonlijke iCloud, vallen onder het privacybeleid van Apple en worden nooit naar de ontwikkelaar of een server van derden gestuurd — de ontwikkelaar heeft er geen toegang toe. Als u beide uitschakelt, blijven alle gegevens alleen op uw toestel.

## Bluetooth

De app communiceert met uw OBD-II-adapter via Bluetooth: Bluetooth Low Energy (BLE) voor de meeste adapters, en Bluetooth Classic, via het External Accessory-framework van Apple, voor de OBDLink MX+, Vgate vLinker FS en Vgate vLinker MS. Alle Bluetooth-communicatie vindt rechtstreeks plaats tussen uw toestel en de adapter. Er worden geen Bluetooth-gegevens naar een server of derde partij verzonden.

## Voertuiggegevens

De app leest diagnosegegevens uit de boordcomputer van uw voertuig via de OBD-II-poort. Deze gegevens omvatten accustatus, temperaturen, spanningen, bandenspanningen en andere sensormetingen. Deze gegevens worden op uw toestel getoond en bewaard, en worden nergens naartoe verzonden, behalve naar uw eigen iCloud zolang synchronisatie van de geschiedenis aanstaat, en naar ABRP als u het delen inschakelt.

## Meldingen

Als u de ontkoppelherinnering inschakelt, gebruikt de app lokale meldingen om u eraan te herinneren de OBD-II-adapter los te koppelen wanneer de auto wordt uitgezet. Er worden geen meldingsgegevens naar een server gestuurd.

## Gegevensbewaring

Alle gegevens worden op uw toestel bewaard. Logbestanden en opnames kunnen worden verwijderd via de Bestanden-app van iOS. Het verwijderen van de app wist alle lokaal opgeslagen gegevens, inclusief instellingen, bewaarde bestemmingen en bewaarde adaptergegevens. Foto's die de app in uw fotobibliotheek heeft bewaard, blijven daar totdat u ze verwijdert. Als u iCloud-synchronisatie hebt ingeschakeld, blijft uw geschiedenis ook in uw iCloud-account staan totdat u deze in de app verwijdert of de synchronisatie uitschakelt. Gegevens die al naar ABRP zijn gestuurd, worden door ABRP bewaard volgens zijn eigen beleid.

## Privacy van kinderen

De app verzamelt niet bewust gegevens van kinderen jonger dan 13 jaar.

## Wijzigingen in dit beleid

Als dit privacybeleid wordt bijgewerkt, wordt de herziene versie op deze pagina geplaatst met een bijgewerkte datum.

## Contact

Als u vragen hebt over dit privacybeleid, [open dan een issue](https://github.com/gburlingame/ioniq-app/issues) op GitHub of stuur een e-mail naar [greg@theburl.com](mailto:greg@theburl.com).
