---
layout: default
title: Integritetspolicy
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <a href="privacy-nl">Nederlands</a> · <a href="privacy-de">Deutsch</a> · <a href="privacy-fr">Français</a> · <a href="privacy-es">Español</a> · <strong>Svenska</strong> · <a href="privacy-it">Italiano</a> · <a href="privacy-ko">한국어</a> · <a href="privacy-tr">Türkçe</a>
</div>

# Integritetspolicy

**Senast uppdaterad: 2 juni 2026**

IONIQ 5 Companion ("appen") utvecklas av Greg Burlingame. Denna integritetspolicy beskriver hur appen hanterar dina data.

## Datainsamling

IONIQ 5 Companion samlar **inte** in, överför eller säljer några personuppgifter till tredje part. Appen innehåller ingen analys, reklam eller spårning av något slag.

## Data som lagras på din enhet

Appen lagrar följande data lokalt på din enhet:

* **Fordonsdiagnostikdata** — Batteristatus, cellspänningar, temperaturer, laddningsdata, däcktryck och andra sensorvärden från ditt fordon lagras i minnet medan appen körs. Dessa data sparas inte mellan appstarter om du inte använder funktionen för diagnostikinspelning.
* **Kör- och laddhistorik** — När du använder Historik-funktionen sparas sammanfattningar och inspelade signalvärden från dina körningar och laddningssessioner (laddningsnivå, energi, temperaturer och andra värden) på din enhet så att du kan granska dem senare.
* **Appinställningar** — Dina inställningar (enheter, språk, utseende, tidsdiagraminställningar, adapterval) lagras lokalt med UserDefaults.
* **Bluetooth-enhetsinformation** — Identifieraren och namnet på din parkopplade OBD-II-adapter lagras lokalt så att appen kan återansluta automatiskt.
* **Diagnostikinspelningar** — Om du använder funktionen "Starta diagnostikinspelning" sparas en loggfil i enhetens lokala lagring. Filen innehåller Bluetooth-händelser, adapterkommandon och rådata från fordonet. Den delas bara när du uttryckligen använder Dela-knappen.
* **A-B-C Snapshot-loggar** — Om du använder snapshot-jämförelsefunktionen sparas en loggfil lokalt med rå ECU-data. Den delas bara när du uttryckligen använder Dela-knappen.

## iCloud-synkronisering (valfritt)

Om du aktiverar iCloud-synkronisering synkroniseras din kör- och laddhistorik via Apples CloudKit till ditt eget privata iCloud-konto, så att den hålls konsekvent på din iPhone, iPad och Mac. Dessa data lagras i din personliga iCloud, omfattas av Apples integritetspolicy och skickas aldrig till utvecklaren eller någon tredjepartsserver – utvecklaren har ingen åtkomst till dem. Om du låter iCloud-synkronisering vara avstängd förblir alla data endast på din enhet.

## Inga tredjepartsintegrationer

Appen integrerar inte med några tredjepartstjänster. Det finns ingen kontoregistrering och ingen inloggning, och dina data laddas aldrig upp till utvecklaren eller någon tredjepartsserver.

## Bluetooth

Appen kommunicerar med din OBD-II-adapter via Bluetooth Low Energy (BLE). All Bluetooth-kommunikation sker direkt mellan din enhet och adaptern. Inga Bluetooth-data överförs till någon server eller tredje part.

## Fordonsdata

Appen läser diagnostikdata från fordonets dator via OBD-II-porten. Dessa data inkluderar batteristatus, temperaturer, spänningar, däcktryck och andra sensorvärden. Dessa data visas på din enhet och överförs inte någon annanstans.

## Aviseringar

Om du aktiverar påminnelsen om att koppla ur använder appen lokala aviseringar för att påminna dig om att koppla ur OBD-II-adaptern när bilen stängs av. Ingen aviseringsdata skickas till någon server.

## Datalagring

All data lagras på din enhet. Diagnostikinspelningar och snapshot-loggar kan raderas via appen Filer i iOS. Avinstallation av appen tar bort all lokalt lagrad data inklusive inställningar och sparad adapterinformation. Om du har aktiverat iCloud-synkronisering finns din historik även kvar i ditt iCloud-konto tills du raderar den i appen eller stänger av synkroniseringen.

## Barns integritet

Appen samlar inte medvetet in några data från barn under 13 år.

## Ändringar av denna policy

Om denna integritetspolicy uppdateras kommer den reviderade versionen att publiceras på denna sida med ett uppdaterat datum.

## Kontakt

Om du har frågor om denna integritetspolicy, vänligen [öppna ett ärende](https://github.com/gburlingame/ioniq-app/issues) på GitHub eller skicka e-post till [greg@theburl.com](mailto:greg@theburl.com).
