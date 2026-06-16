---
layout: default
title: Politique de confidentialité
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <a href="privacy-nl">Nederlands</a> · <a href="privacy-de">Deutsch</a> · <strong>Français</strong> · <a href="privacy-es">Español</a> · <a href="privacy-sv">Svenska</a> · <a href="privacy-it">Italiano</a> · <a href="privacy-ko">한국어</a> · <a href="privacy-tr">Türkçe</a>
</div>

# Politique de confidentialité

**Dernière mise à jour : 2 juin 2026**

IONIQ 5 Companion (« l'application ») est développée par Greg Burlingame. Cette politique de confidentialité décrit comment l'application gère vos données.

## Collecte de données

IONIQ 5 Companion ne collecte, ne transmet et ne vend **aucune** donnée personnelle à des tiers. L'application ne contient aucune analyse, publicité ou suivi d'aucune sorte.

## Données stockées sur votre appareil

L'application stocke les données suivantes localement sur votre appareil :

* **Données de diagnostic du véhicule** — L'état de la batterie, les tensions des cellules, les températures, les données de charge, les pressions des pneus et d'autres mesures de capteurs de votre véhicule sont stockés en mémoire pendant que l'application fonctionne. Ces données ne sont pas conservées entre les lancements de l'application, sauf si vous utilisez la fonction d'enregistrement de diagnostic.
* **Historique de conduite et de recharge** — Lorsque vous utilisez la fonction Historique, les résumés et les échantillons de signaux enregistrés de vos trajets et sessions de recharge (état de charge, énergie, températures et autres mesures) sont enregistrés sur votre appareil afin que vous puissiez les consulter ultérieurement.
* **Paramètres de l'application** — Vos préférences (unités, langue, apparence, paramètres de graphiques temporels, sélection de l'adaptateur) sont stockées localement avec UserDefaults.
* **Informations sur l'appareil Bluetooth** — L'identifiant et le nom de votre adaptateur OBD-II couplé sont stockés localement pour que l'application puisse se reconnecter automatiquement.
* **Enregistrements de diagnostic** — Si vous utilisez la fonction « Démarrer le diagnostic », un fichier journal est enregistré dans le stockage local de votre appareil. Ce fichier contient les événements Bluetooth, les commandes de l'adaptateur et les données brutes du véhicule. Il n'est partagé que lorsque vous utilisez explicitement le bouton de partage.
* **Journaux de snapshots A-B-C** — Si vous utilisez la fonction de comparaison de snapshots, un fichier journal est enregistré localement contenant les données brutes de l'ECU. Il n'est partagé que lorsque vous utilisez explicitement le bouton de partage.

## Synchronisation iCloud (facultative)

Si vous activez la synchronisation iCloud, votre historique de conduite et de recharge est synchronisé via CloudKit d'Apple avec votre propre compte iCloud privé, afin qu'il reste cohérent sur votre iPhone, iPad et Mac. Ces données sont stockées dans votre iCloud personnel, sont régies par la politique de confidentialité d'Apple et ne sont jamais envoyées au développeur ni à un serveur tiers — le développeur n'y a pas accès. Si vous laissez la synchronisation iCloud désactivée, toutes les données restent uniquement sur votre appareil.

## Aucune intégration tierce

L'application ne s'intègre à aucun service tiers. Il n'y a pas de création de compte ni de connexion, et vos données ne sont jamais téléversées vers le développeur ni vers un serveur tiers.

## Bluetooth

L'application communique avec votre adaptateur OBD-II via Bluetooth Low Energy (BLE). Toute la communication Bluetooth s'effectue directement entre votre appareil et l'adaptateur. Aucune donnée Bluetooth n'est transmise à un serveur ou à un tiers.

## Données du véhicule

L'application lit les données de diagnostic de l'ordinateur de bord de votre véhicule via le port OBD-II. Ces données comprennent l'état de la batterie, les températures, les tensions, les pressions des pneus et d'autres mesures de capteurs. Ces données sont affichées sur votre appareil et ne sont transmises nulle part.

## Notifications

Si vous activez le rappel de débranchement, l'application utilise des notifications locales pour vous rappeler de débrancher l'adaptateur OBD-II lorsque la voiture s'éteint. Aucune donnée de notification n'est envoyée à un serveur.

## Conservation des données

Toutes les données sont stockées sur votre appareil. Les enregistrements de diagnostic et les journaux de snapshots peuvent être supprimés via l'application Fichiers d'iOS. La désinstallation de l'application supprime toutes les données stockées localement, y compris les paramètres et les informations d'adaptateur enregistrées. Si vous avez activé la synchronisation iCloud, votre historique reste également dans votre compte iCloud jusqu'à ce que vous le supprimiez depuis l'application ou désactiviez la synchronisation.

## Confidentialité des enfants

L'application ne collecte pas sciemment de données auprès d'enfants de moins de 13 ans.

## Modifications de cette politique

Si cette politique de confidentialité est mise à jour, la version révisée sera publiée sur cette page avec une date mise à jour.

## Contact

Si vous avez des questions sur cette politique de confidentialité, veuillez [ouvrir un issue](https://github.com/gburlingame/ioniq-app/issues) sur GitHub ou envoyer un e-mail à [greg@theburl.com](mailto:greg@theburl.com).
