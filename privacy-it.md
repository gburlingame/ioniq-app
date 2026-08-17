---
layout: default
title: Informativa sulla privacy
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <a href="privacy-nl">Nederlands</a> · <a href="privacy-de">Deutsch</a> · <a href="privacy-fr">Français</a> · <a href="privacy-es">Español</a> · <a href="privacy-sv">Svenska</a> · <strong>Italiano</strong> · <a href="privacy-ko">한국어</a> · <a href="privacy-tr">Türkçe</a> · <a href="privacy-ja">日本語</a>
</div>

# Informativa sulla privacy

**Ultimo aggiornamento: 17 agosto 2026**

EV Dashboard ("l'app") è sviluppata da Greg Burlingame. Questa informativa sulla privacy descrive come l'app gestisce i Suoi dati.

## Raccolta dei dati

EV Dashboard **non** raccoglie, trasmette né vende alcun dato personale a terzi. L'app non ha alcun server, alcun account e alcun accesso. Non contiene analisi, pubblicità o tracciamento di alcun tipo e non carica mai i Suoi dati da nessuna parte.

## Dati memorizzati sul Suo dispositivo

L'app memorizza i seguenti dati localmente sul Suo dispositivo:

* **Dati diagnostici del veicolo** — Stato della batteria, tensioni delle celle, temperature, dati di ricarica, pressioni degli pneumatici e altre letture dei sensori del Suo veicolo sono mantenuti in memoria mentre l'app è in esecuzione. Questi dati non vengono conservati tra un avvio e l'altro, a meno che non utilizzi una funzione di registrazione.
* **Cronologia di guida e ricarica** — Quando utilizza la funzione Cronologia, i riepiloghi e i campioni di segnale registrati dei Suoi viaggi e delle Sue sessioni di ricarica (stato di carica, energia, temperature e altre letture) vengono salvati sul Suo dispositivo per poterli consultare in seguito. Una sessione può anche memorizzare il luogo in cui si è svolta, così da poterlo mostrare su una mappa.
* **Impostazioni dell'app** — Le Sue preferenze (unità, lingua, aspetto, temi, impostazioni dei grafici, selezione dell'adattatore, disposizione dei riquadri CarPlay) sono memorizzate localmente tramite UserDefaults.
* **Destinazioni salvate** — Gli indirizzi che salva per la navigazione e le Sue destinazioni recenti sono memorizzati localmente sul Suo dispositivo.
* **Informazioni sul dispositivo Bluetooth** — L'identificatore e il nome del Suo adattatore OBD-II abbinato sono memorizzati localmente affinché l'app possa riconnettersi automaticamente.
* **Registro attività dell'app** — Un file di log con gli eventi del ciclo di vita dell'app, della connessione Bluetooth, dell'interferenza dell'adattatore e dell'archiviazione della cronologia. Viene condiviso solo quando utilizza esplicitamente il pulsante Condividi.
* **Registratore diagnostica di guida** — Un file di log per ogni viaggio contenente posizioni GPS, campioni di velocità del veicolo e calcoli di distanza, usato per diagnosticare la precisione di distanza e navigazione. Viene condiviso solo quando utilizza esplicitamente il pulsante Condividi.
* **Registrazioni diagnostiche e log degli snapshot** — Se utilizza la registrazione diagnostica o la funzione di confronto degli snapshot, viene salvato localmente un file di log contenente eventi Bluetooth, comandi dell'adattatore e dati grezzi del veicolo. Viene condiviso solo quando utilizza esplicitamente il pulsante Condividi.

## Posizione

EV Dashboard utilizza la Sua posizione per mostrare dove si trova sulla mappa di CarPlay, fornire indicazioni dettagliate, misurare distanza ed efficienza del viaggio durante la guida e trovare colonnine nelle vicinanze.

L'app richiede esclusivamente l'accesso "Quando si usa l'app". Non richiede mai l'accesso "Sempre". Poiché la distanza del viaggio viene misurata in modo continuo durante la guida, gli aggiornamenti di posizione possono proseguire mentre l'app è in background o mentre utilizza un'altra app: ciò termina al termine del viaggio.

La Sua posizione viene utilizzata sul Suo dispositivo e non viene inviata allo sviluppatore. Non viene raccolta, profilata né venduta. I dati di posizione possono essere scritti nei file descritti sopra (il Registratore diagnostica di guida e il luogo salvato con una sessione della cronologia); questi lasciano il Suo dispositivo solo se sceglie di condividerli.

## Mappe e navigazione

Mappe, ricerca di indirizzi e calcolo del percorso sono forniti da MapKit di Apple. Quando cerca un indirizzo o avvia una navigazione, le informazioni di ricerca e di posizione necessarie vengono inviate ad Apple per restituire un risultato e sono trattate secondo l'[informativa sulla privacy di Apple](https://www.apple.com/legal/privacy/). Queste informazioni non vengono inviate allo sviluppatore.

## Aggiornamenti del database delle colonnine

L'elenco dei punti di ricarica rapida DC è incluso nell'app e funziona offline. Non serve alcuna connessione di rete per consultare una colonnina o per navigare fino a essa.

Se tocca **Impostazioni → Navigazione → Cerca aggiornamento**, e solo allora, l'app scarica un database delle colonnine più recente. Ciò comporta due richieste: una per un file manifest ospitato su theburl.com e una per il file di dati che esso indica, ospitato su GitHub Releases. Entrambi sono normali download di file statici, verificati con un checksum. Con queste richieste non viene inviata alcuna informazione su di Lei, sul Suo dispositivo o sul Suo veicolo, e non esiste alcun controllo di aggiornamento automatico o periodico.

## Sincronizzazione iCloud (facoltativa)

Se attiva la sincronizzazione iCloud, la Sua cronologia di guida e ricarica — incluso il luogo salvato con una sessione — viene sincronizzata tramite CloudKit di Apple con il Suo account iCloud privato, così da restare coerente su iPhone, iPad e Mac. Questi dati sono archiviati nel Suo iCloud personale, sono regolati dall'informativa sulla privacy di Apple e non vengono mai inviati allo sviluppatore né ad alcun server di terze parti: lo sviluppatore non vi ha accesso. Se lascia disattivata la sincronizzazione iCloud, tutti i dati restano solo sul Suo dispositivo.

## Bluetooth

L'app comunica con il Suo adattatore OBD-II tramite Bluetooth Low Energy (BLE). Tutta la comunicazione Bluetooth avviene direttamente tra il Suo dispositivo e l'adattatore. Nessun dato Bluetooth viene trasmesso ad alcun server o terza parte.

## Dati del veicolo

L'app legge i dati diagnostici dal computer di bordo del Suo veicolo tramite la porta OBD-II. Questi dati includono stato della batteria, temperature, tensioni, pressioni degli pneumatici e altre letture dei sensori. Questi dati vengono mostrati sul Suo dispositivo e non sono trasmessi da nessuna parte.

## Notifiche

Se attiva il promemoria di scollegamento, l'app utilizza notifiche locali per ricordarLe di scollegare l'adattatore OBD-II quando l'auto si spegne. Nessun dato di notifica viene inviato ad alcun server.

## Conservazione dei dati

Tutti i dati sono archiviati sul Suo dispositivo. I file di log e le registrazioni possono essere eliminati tramite l'app File di iOS. La disinstallazione dell'app rimuove tutti i dati archiviati localmente, incluse impostazioni, destinazioni salvate e informazioni sull'adattatore salvate. Se ha attivato la sincronizzazione iCloud, la Sua cronologia resta inoltre nel Suo account iCloud finché non la elimina dall'app o disattiva la sincronizzazione.

## Privacy dei minori

L'app non raccoglie consapevolmente dati da minori di 13 anni.

## Modifiche a questa informativa

Se questa informativa sulla privacy viene aggiornata, la versione rivista sarà pubblicata su questa pagina con una data aggiornata.

## Contatti

In caso di domande su questa informativa sulla privacy, [apra una segnalazione](https://github.com/gburlingame/ioniq-app/issues) su GitHub o scriva a [greg@theburl.com](mailto:greg@theburl.com).
