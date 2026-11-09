---
layout: default
title: Integritetspolicy
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <a href="privacy-nl">Nederlands</a> · <a href="privacy-de">Deutsch</a> · <a href="privacy-fr">Français</a> · <a href="privacy-es">Español</a> · <strong>Svenska</strong> · <a href="privacy-it">Italiano</a> · <a href="privacy-ko">한국어</a> · <a href="privacy-tr">Türkçe</a> · <a href="privacy-ja">日本語</a>
</div>

# Integritetspolicy

**Senast uppdaterad: 9 november 2026**

EV Dashboard ("appen") utvecklas av Greg Burlingame. Denna integritetspolicy beskriver hur appen hanterar dina data.

## Datainsamling

EV Dashboard har ingen server, inget konto och ingen inloggning. Den innehåller ingen analys, reklam eller spårning av något slag. Utvecklaren tar aldrig emot dina data, och ingenting säljs.

Dina data lämnar din enhet endast i följande fall, som vart och ett beskrivs nedan:

* **Delning med ABRP** — avstängd tills du slår på den och länkar ett fordon; den skickar fordonets livedata direkt till ABRP.
* **iCloud-synkronisering** — dina inställningar och din historik synkroniseras till ditt eget privata iCloud-konto.
* **Apple Kartor** — adressökningar, kontaktadresser som du väljer och ruttförfrågningar går till Apples MapKit.
* **Filer som du delar** — loggar, inspelningar, exporter och delningskort lämnar din enhet endast när du trycker på Dela.

Internetanslutning-rutan och uppdateringar av laddardatabasen gör också nätverksförfrågningar. De innehåller ingen information om dig eller ditt fordon.

## Data som lagras på din enhet

Appen lagrar följande data lokalt på din enhet:

* **Fordonsdiagnostikdata** — Batteristatus, cellspänningar, temperaturer, laddningsdata, däcktryck och andra sensoravläsningar från ditt fordon hålls i minnet medan appen körs. Dessa data sparas inte mellan appstarter om du inte använder en inspelningsfunktion.
* **Kör- och laddhistorik** — När du använder Historik-funktionen sparas sammanfattningar och inspelade signalvärden från dina resor och laddsessioner (laddningsnivå, energi, temperaturer och andra avläsningar) på din enhet så att du kan gå igenom dem senare. En laddsession kan lagra platsen där den ägde rum. En körning lagrar sin rutt — din plats ungefär en gång per sekund medan du kör — så att den kan visas på körningens Färdväg-karta. Du kan stänga av detta under **Inställningar → Körsessioner → Spela in färdväg**, eller ta bort en körnings rutt från dess Färdväg-karta.
* **Sessionsfoton** — Ett foto som du lägger till i en ladd- eller körsession lagras med den sessionen.
* **Appinställningar** — Dina inställningar (enheter, språk, utseende, teman, diagraminställningar, adapterval, CarPlay-rutlayouter, laddfilter, däckinställningar och fordonsnamn) lagras på din enhet och synkroniseras via iCloud medan Synkronisera till iCloud är på.
* **Sparade destinationer** — Adresser som du sparar för navigering, och dina senaste destinationer, lagras på din enhet och synkroniseras med dina inställningar.
* **Bluetooth-enhetsinformation** — Identifieraren och namnet på din parkopplade OBD-II-adapter lagras lokalt så att appen kan återansluta automatiskt.
* **ABRP-länktoken** — Om du länkar ett fordon till ABRP lagras den token som du klistrar in från ABRP-appen i enhetens nyckelring. När du tar bort länken till fordonet raderas den.
* **Appaktivitetslogg** — En loggfil som registrerar händelser för appens livscykel, Bluetooth-anslutning, adapterstörning och historiklagring. Den delas endast när du uttryckligen använder Dela-knappen.
* **Kördiagnostik-inspelning** — En loggfil per körning med GPS-mätningar (position, färdriktning, hastighet och höjd), fordonets hastighetsvärden och avståndsberäkningar, som används för att felsöka avstånds-, höjd- och navigeringsnoggrannhet. Den delas endast när du uttryckligen använder Dela-knappen.
* **Diagnostikinspelningar och ögonblicksloggar** — Om du använder diagnostikinspelning eller jämförelsefunktionen för ögonblicksbilder sparas en loggfil lokalt med Bluetooth-händelser, adapterkommandon och rådata från fordonet. Den delas endast när du uttryckligen använder Dela-knappen.

## Plats

EV Dashboard använder din plats för att visa din position på CarPlay-kartan, ge sväng-för-sväng-vägledning, mäta körsträcka och effektivitet, spela in en körnings färdväg, visa din höjd och hitta laddare i närheten.

Appen begär endast åtkomst "När appen används". Den begär aldrig "Alltid"-åtkomst. Platsuppdateringar kan fortsätta medan appen är i bakgrunden eller medan du använder en annan app: om du öppnar appen medan den är ansluten till ditt fordon behåller den en platssession i bakgrunden tills fordonet stängs av eller adaptern är utom Bluetooth-räckvidd, och iOS visar platssymbolen under tiden. GPS-mätningar för körsträcka och färdväg görs endast medan du kör.

Din plats skickas inte till utvecklaren, och den profileras inte och säljs inte. Den lagras på din enhet i historiken och filerna som beskrivs ovan; dessa lämnar din enhet via iCloud-synkronisering eller när du väljer att dela dem. Om du slår på delning med ABRP skickas fordonets plats till ABRP (se avsnittet Delning med ABRP).

## Kartor och navigering

Kartor, adressökning och ruttberäkning tillhandahålls av Apples MapKit. När du söker efter en adress, väljer en kontakts adress eller startar en navigering skickas den sök- och platsinformation som behövs till Apple för att ge ett resultat, och hanteras enligt [Apples integritetspolicy](https://www.apple.com/legal/privacy/). Denna information skickas inte till utvecklaren.

## Kontakter

Om du slår på **Visa kontakter i sökningen** när du lägger till en destination på din mobila enhet ber appen om åtkomst till dina kontakter och visar deras adresser medan du skriver, i appen och i CarPlay. När du väljer en kontakt skickas dess adress till Apples MapKit för att placera den på kartan, och kontaktens namn sparas som destinationens etikett. Appen lagrar inte dina kontakter och skickar dem inte någon annanstans.

## Kamera och foton

När du trycker på en sessions fotoruta kan du ta ett foto med kameran eller välja ett från ditt bibliotek. Ett foto som du tar lagras med sessionen, och originalet i full upplösning sparas också i ditt fotobibliotek. För det ber appen om åtkomst endast för att lägga till: den kan lägga till foton i ditt bibliotek men kan inte se fotona i det. När du väljer ett foto från ditt bibliotek ger den inbyggda bildväljaren i iOS appen endast det foto som du väljer.

## Rörelse och träning

Appen använder enhetens barometer för att följa stigningar och nedförsbackar för Höjd-rutan i CarPlay och Färdväg-kartan, vilket betyder mest för fordon vars CarPlay-system inte rapporterar höjd. Den ber om åtkomst till Rörelse och träning för detta. Barometeravläsningar används på din enhet och skickas inte någonstans.

## Delning med ABRP (valfritt)

ABRP (A Better Routeplanner) är en ruttplaneringstjänst som drivs av Iternio. Delningen är avstängd tills du slår på **Dela livedata med ABRP** under **Inställningar → Datadelning → ABRP** och länkar ett fordon med token från din ABRP-app. När du länkar skickar appen token till ABRP för att kontrollera den.

Medan ett länkat fordon är påslaget skickar appen dess livedata direkt från din enhet till ABRP:s servrar (api.iternio.com): tiden; laddningsnivå, batterienergi och hälsotillstånd; effekt, ström och spänning; hastighet; plats (latitud, longitud, höjd och färdriktning); om fordonet laddar, DC-snabbladdar eller är parkerat; mätarställningen; batteri-, kabin- och utetemperatur; samt däcktryck. VIN skickas inte. Avläsningar som inte kunde skickas hålls i minnet, upp till en gräns, tills anslutningen återkommer, och kasseras om appen stängs.

Dessa data passerar inte via utvecklaren. ABRP hanterar dem enligt sin egen integritetspolicy. För att sluta dela stänger du av reglaget eller tar bort länken till fordonet.

## Internetanslutning-rutan

Internetanslutning-rutan i CarPlay mäter din anslutning. Medan rutan visas på din CarPlay-skärm begär appen en tom testsida ungefär var 30:e sekund, växelvis från Cloudflare (cp.cloudflare.com) och Google (connectivitycheck.gstatic.com). Dessa förfrågningar innehåller ingen information om dig eller ditt fordon, men liksom alla internetförfrågningar avslöjar de din nätverksadress för dessa tjänster. Inga förfrågningar görs medan rutan inte visas på skärmen.

## Uppdateringar av laddardatabasen

Listan över DC-snabbladdplatser ingår i appen och fungerar offline. Ingen nätverksanslutning behövs för att bläddra bland laddare eller navigera till en.

Om du trycker på **Inställningar → Navigering → Sök efter uppdatering**, och endast då, hämtar appen en nyare laddardatabas. Detta gör två förfrågningar: en för en manifestfil som ligger på theburl.com och en för datafilen som den anger, som ligger på GitHub Releases. Båda är vanliga nedladdningar av statiska filer, verifierade mot en kontrollsumma. Ingen information om dig, din enhet eller ditt fordon skickas med dessa förfrågningar, och det finns ingen automatisk eller periodisk uppdateringskontroll.

## iCloud-synkronisering

Båda typerna av synkronisering är på som standard och kan stängas av under **Inställningar → iCloud**.

* **Inställningar** — Medan **Synkronisera till iCloud** är på synkroniseras dina appinställningar, sparade destinationer, däckinställningar och fordonsnamn via Apples nyckel-värde-lagring i iCloud till ditt eget iCloud-konto, så att de stämmer överens på alla dina enheter. Om appen ska återansluta automatiskt till en adapter ställs in på varje enhet och synkroniseras inte.
* **Historik** — Medan historiksynkroniseringen är på synkroniseras din kör- och laddhistorik — inklusive sessionsfoton, platsen som sparats med en laddsession och varje körnings färdväg — via Apples CloudKit till ditt eget privata iCloud-konto, så att den hålls konsekvent mellan iPhone, iPad och Mac.

Båda lagras i ditt personliga iCloud, omfattas av Apples integritetspolicy och skickas aldrig till utvecklaren eller någon tredjepartsserver — utvecklaren har ingen åtkomst till dem. Om du stänger av båda stannar alla data endast på din enhet.

## Bluetooth

Appen kommunicerar med din OBD-II-adapter via Bluetooth: Bluetooth Low Energy (BLE) för de flesta adaptrar, och Bluetooth Classic, via Apples ramverk External Accessory, för OBDLink MX+, Vgate vLinker FS och Vgate vLinker MS. All Bluetooth-kommunikation sker direkt mellan din enhet och adaptern. Inga Bluetooth-data överförs till någon server eller tredje part.

## Fordonsdata

Appen läser diagnostikdata från fordonets omborddator via OBD-II-porten. Dessa data omfattar batteristatus, temperaturer, spänningar, däcktryck och andra sensoravläsningar. Dessa data visas och lagras på din enhet och överförs inte någonstans, utom till ditt eget iCloud medan historiksynkroniseringen är på, och till ABRP om du slår på delning.

## Aviseringar

Om du aktiverar urkopplingspåminnelsen använder appen lokala aviseringar för att påminna dig om att koppla ur OBD-II-adaptern när bilen stängs av. Inga aviseringsdata skickas till någon server.

## Datalagring

Alla data lagras på din enhet. Loggfiler och inspelningar kan raderas via iOS Filer-app. Att avinstallera appen tar bort alla lokalt lagrade data inklusive inställningar, sparade destinationer och sparad adapterinformation. Foton som appen har sparat i ditt fotobibliotek finns kvar där tills du raderar dem. Om du aktiverade iCloud-synkronisering finns din historik även kvar i ditt iCloud-konto tills du raderar den i appen eller stänger av synkroniseringen. Data som redan har skickats till ABRP sparas av ABRP enligt dess egen policy.

## Barns integritet

Appen samlar inte medvetet in data från barn under 13 år.

## Ändringar av denna policy

Om denna integritetspolicy uppdateras publiceras den reviderade versionen på denna sida med ett uppdaterat datum.

## Kontakt

Om du har frågor om denna integritetspolicy, [öppna ett ärende](https://github.com/gburlingame/ioniq-app/issues) på GitHub eller mejla [greg@theburl.com](mailto:greg@theburl.com).
