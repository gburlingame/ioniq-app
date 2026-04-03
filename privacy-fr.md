---
layout: default
title: Politique de confidentialité
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <a href="privacy-nl">Nederlands</a> · <a href="privacy-de">Deutsch</a> · <strong>Français</strong> · <a href="privacy-es">Español</a>
</div>

# Politique de confidentialité

**Dernière mise à jour : 3 avril 2026**

Ioniq 5 Diagnostics (« l'application ») est développée par Greg Burlingame. Cette politique de confidentialité décrit comment l'application gère vos données.

## Collecte de données

Ioniq 5 Diagnostics ne collecte, ne transmet et ne vend **aucune** donnée personnelle à des tiers. L'application ne contient aucune analyse, publicité ou suivi d'aucune sorte.

## Données stockées sur votre appareil

L'application stocke les données suivantes localement sur votre appareil :

* **Données de diagnostic du véhicule** — L'état de la batterie, les tensions des cellules, les températures, les données de charge, les pressions des pneus et d'autres mesures de capteurs de votre véhicule sont stockés en mémoire pendant que l'application fonctionne. Ces données ne sont pas conservées entre les lancements de l'application, sauf si vous utilisez la fonction d'enregistrement de diagnostic.
* **Paramètres de l'application** — Vos préférences (unités, langue, apparence, paramètres de graphiques temporels, sélection de l'adaptateur) sont stockées localement avec UserDefaults.
* **Informations sur l'appareil Bluetooth** — L'identifiant et le nom de votre adaptateur OBD-II couplé sont stockés localement pour que l'application puisse se reconnecter automatiquement.
* **Enregistrements de diagnostic** — Si vous utilisez la fonction « Démarrer le diagnostic », un fichier journal est enregistré dans le stockage local de votre appareil. Ce fichier contient les événements Bluetooth, les commandes de l'adaptateur et les données brutes du véhicule. Il n'est partagé que lorsque vous utilisez explicitement le bouton de partage.
* **Journaux de snapshots A-B-C** — Si vous utilisez la fonction de comparaison de snapshots, un fichier journal est enregistré localement contenant les données brutes de l'ECU. Il n'est partagé que lorsque vous utilisez explicitement le bouton de partage.

## Aucun service cloud

L'application n'utilise pas iCloud, CloudKit ou tout autre stockage cloud. Toutes les données restent sur votre appareil.

## Aucune intégration tierce

L'application ne s'intègre à aucun service tiers. Il n'y a pas de création de compte, pas de connexion et pas de téléchargement de données.

## Bluetooth

L'application communique avec votre adaptateur OBD-II via Bluetooth Low Energy (BLE). Toute la communication Bluetooth s'effectue directement entre votre appareil et l'adaptateur. Aucune donnée Bluetooth n'est transmise à un serveur ou à un tiers.

## Données du véhicule

L'application lit les données de diagnostic de l'ordinateur de bord de votre véhicule via le port OBD-II. Ces données comprennent l'état de la batterie, les températures, les tensions, les pressions des pneus et d'autres mesures de capteurs. Ces données sont affichées sur votre appareil et ne sont transmises nulle part.

## Notifications

Si vous activez le rappel de débranchement, l'application utilise des notifications locales pour vous rappeler de débrancher l'adaptateur OBD-II lorsque la voiture s'éteint. Aucune donnée de notification n'est envoyée à un serveur.

## Conservation des données

Toutes les données sont stockées sur votre appareil. Les enregistrements de diagnostic et les journaux de snapshots peuvent être supprimés via l'application Fichiers d'iOS. La désinstallation de l'application supprime toutes les données stockées localement, y compris les paramètres et les informations d'adaptateur enregistrées.

## Confidentialité des enfants

L'application ne collecte pas sciemment de données auprès d'enfants de moins de 13 ans.

## Modifications de cette politique

Si cette politique de confidentialité est mise à jour, la version révisée sera publiée sur cette page avec une date mise à jour.

## Contact

Si vous avez des questions sur cette politique de confidentialité, veuillez [ouvrir un issue](https://github.com/gburlingame/ioniq-app/issues) sur GitHub ou envoyer un e-mail à [greg@theburl.com](mailto:greg@theburl.com).
