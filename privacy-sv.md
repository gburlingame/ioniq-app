---
layout: default
title: Integritetspolicy
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <a href="privacy-nl">Nederlands</a> · <a href="privacy-de">Deutsch</a> · <a href="privacy-fr">Français</a> · <a href="privacy-es">Español</a> · <strong>Svenska</strong> · <a href="privacy-it">Italiano</a> · <a href="privacy-ko">한국어</a> · <a href="privacy-tr">Türkçe</a> · <a href="privacy-ja">日本語</a>
</div>

# Integritetspolicy

**Senast uppdaterad: 17 augusti 2026**

EV Dashboard ("appen") utvecklas av Greg Burlingame. Denna integritetspolicy beskriver hur appen hanterar dina data.

## Datainsamling

EV Dashboard samlar **inte** in, överför eller säljer några personuppgifter till tredje part. Appen har ingen server, inget konto och ingen inloggning. Den innehåller ingen analys, reklam eller spårning av något slag och laddar aldrig upp dina data någonstans.

## Data som lagras på din enhet

Appen lagrar följande data lokalt på din enhet:

* **Fordonsdiagnostikdata** — Batteristatus, cellspänningar, temperaturer, laddningsdata, däcktryck och andra sensoravläsningar från ditt fordon hålls i minnet medan appen körs. Dessa data sparas inte mellan appstarter om du inte använder en inspelningsfunktion.
* **Kör- och laddhistorik** — När du använder Historik-funktionen sparas sammanfattningar och inspelade signalvärden från dina resor och laddsessioner (laddningsnivå, energi, temperaturer och andra avläsningar) på din enhet så att du kan gå igenom dem senare. En session kan också lagra platsen där den ägde rum, så att den kan visas på en karta.
* **Appinställningar** — Dina inställningar (enheter, språk, utseende, teman, diagraminställningar, adapterval, CarPlay-rutlayouter) lagras lokalt med UserDefaults.
* **Sparade destinationer** — Adresser som du sparar för navigering, och dina senaste destinationer, lagras lokalt på din enhet.
* **Bluetooth-enhetsinformation** — Identifieraren och namnet på din parkopplade OBD-II-adapter lagras lokalt så att appen kan återansluta automatiskt.
* **Appaktivitetslogg** — En loggfil som registrerar händelser för appens livscykel, Bluetooth-anslutning, adapterstörning och historiklagring. Den delas endast när du uttryckligen använder Dela-knappen.
* **Kördiagnostik-inspelning** — En loggfil per körning med GPS-positioner, hastighetsvärden och avståndsberäkningar, som används för att felsöka avstånds- och navigeringsnoggrannhet. Den delas endast när du uttryckligen använder Dela-knappen.
* **Diagnostikinspelningar och ögonblicksloggar** — Om du använder diagnostikinspelning eller jämförelsefunktionen för ögonblicksbilder sparas en loggfil lokalt med Bluetooth-händelser, adapterkommandon och rådata från fordonet. Den delas endast när du uttryckligen använder Dela-knappen.

## Plats

EV Dashboard använder din plats för att visa din position på CarPlay-kartan, ge sväng-för-sväng-vägledning, mäta körsträcka och effektivitet under körning och hitta laddare i närheten.

Appen begär endast åtkomst "När appen används". Den begär aldrig "Alltid"-åtkomst. Eftersom körsträckan mäts kontinuerligt under en körning kan platsuppdateringar fortsätta medan appen är i bakgrunden eller medan du använder en annan app — detta upphör när körningen avslutas.

Din plats används på din enhet och skickas inte till utvecklaren. Den samlas inte in, profileras inte och säljs inte. Platsdata kan skrivas till filerna som beskrivs ovan (Kördiagnostik-inspelningen och platsen som sparas med en historiksession); dessa lämnar din enhet endast om du själv väljer att dela dem.

## Kartor och navigering

Kartor, adressökning och ruttberäkning tillhandahålls av Apples MapKit. När du söker efter en adress eller startar en navigering skickas den sök- och platsinformation som behövs till Apple för att ge ett resultat, och hanteras enligt [Apples integritetspolicy](https://www.apple.com/legal/privacy/). Denna information skickas inte till utvecklaren.

## Uppdateringar av laddardatabasen

Listan över DC-snabbladdplatser ingår i appen och fungerar offline. Ingen nätverksanslutning behövs för att bläddra bland laddare eller navigera till en.

Om du trycker på **Inställningar → Navigering → Sök efter uppdatering**, och endast då, hämtar appen en nyare laddardatabas. Detta gör två förfrågningar: en för en manifestfil som ligger på theburl.com och en för datafilen som den anger, som ligger på GitHub Releases. Båda är vanliga nedladdningar av statiska filer, verifierade mot en kontrollsumma. Ingen information om dig, din enhet eller ditt fordon skickas med dessa förfrågningar, och det finns ingen automatisk eller periodisk uppdateringskontroll.

## iCloud-synkronisering (valfritt)

Om du aktiverar iCloud-synkronisering synkroniseras din kör- och laddhistorik — inklusive platsen som sparats med en session — via Apples CloudKit till ditt eget privata iCloud-konto, så att den hålls konsekvent mellan iPhone, iPad och Mac. Dessa data lagras i ditt personliga iCloud, omfattas av Apples integritetspolicy och skickas aldrig till utvecklaren eller någon tredjepartsserver — utvecklaren har ingen åtkomst till dem. Om du låter iCloud-synkroniseringen vara avstängd stannar alla data endast på din enhet.

## Bluetooth

Appen kommunicerar med din OBD-II-adapter via Bluetooth Low Energy (BLE). All Bluetooth-kommunikation sker direkt mellan din enhet och adaptern. Inga Bluetooth-data överförs till någon server eller tredje part.

## Fordonsdata

Appen läser diagnostikdata från fordonets omborddator via OBD-II-porten. Dessa data omfattar batteristatus, temperaturer, spänningar, däcktryck och andra sensoravläsningar. Dessa data visas på din enhet och överförs inte någonstans.

## Aviseringar

Om du aktiverar urkopplingspåminnelsen använder appen lokala aviseringar för att påminna dig om att koppla ur OBD-II-adaptern när bilen stängs av. Inga aviseringsdata skickas till någon server.

## Datalagring

Alla data lagras på din enhet. Loggfiler och inspelningar kan raderas via iOS Filer-app. Att avinstallera appen tar bort alla lokalt lagrade data inklusive inställningar, sparade destinationer och sparad adapterinformation. Om du aktiverade iCloud-synkronisering finns din historik även kvar i ditt iCloud-konto tills du raderar den i appen eller stänger av synkroniseringen.

## Barns integritet

Appen samlar inte medvetet in data från barn under 13 år.

## Ändringar av denna policy

Om denna integritetspolicy uppdateras publiceras den reviderade versionen på denna sida med ett uppdaterat datum.

## Kontakt

Om du har frågor om denna integritetspolicy, [öppna ett ärende](https://github.com/gburlingame/ioniq-app/issues) på GitHub eller mejla [greg@theburl.com](mailto:greg@theburl.com).
