---
layout: default
title: Politique de confidentialité
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <a href="privacy-nl">Nederlands</a> · <a href="privacy-de">Deutsch</a> · <strong>Français</strong> · <a href="privacy-es">Español</a> · <a href="privacy-sv">Svenska</a> · <a href="privacy-it">Italiano</a> · <a href="privacy-ko">한국어</a> · <a href="privacy-tr">Türkçe</a> · <a href="privacy-ja">日本語</a>
</div>

# Politique de confidentialité

**Dernière mise à jour : 17 août 2026**

EV Dashboard (« l'application ») est développée par Greg Burlingame. Cette politique de confidentialité décrit comment l'application gère vos données.

## Collecte de données

EV Dashboard ne collecte, ne transmet et ne vend **aucune** donnée personnelle à des tiers. L'application n'a ni serveur, ni compte, ni connexion. Elle ne contient aucune analyse, publicité ou suivi d'aucune sorte, et n'envoie jamais vos données où que ce soit.

## Données stockées sur votre appareil

L'application stocke les données suivantes localement sur votre appareil :

* **Données de diagnostic du véhicule** — L'état de la batterie, les tensions des cellules, les températures, les données de charge, les pressions des pneus et d'autres mesures de capteurs de votre véhicule sont stockés en mémoire pendant que l'application fonctionne. Ces données ne sont pas conservées entre les lancements de l'application, sauf si vous utilisez une fonction d'enregistrement.
* **Historique de conduite et de recharge** — Lorsque vous utilisez la fonction Historique, les résumés et les échantillons de signaux enregistrés de vos trajets et sessions de recharge (état de charge, énergie, températures et autres mesures) sont enregistrés sur votre appareil afin que vous puissiez les consulter ultérieurement. Une session peut également enregistrer le lieu où elle s'est déroulée, afin de pouvoir l'afficher sur une carte.
* **Paramètres de l'application** — Vos préférences (unités, langue, apparence, thèmes, paramètres de graphiques, sélection de l'adaptateur, dispositions des vignettes CarPlay) sont stockées localement avec UserDefaults.
* **Destinations enregistrées** — Les adresses que vous enregistrez pour la navigation, ainsi que vos destinations récentes, sont stockées localement sur votre appareil.
* **Informations sur l'appareil Bluetooth** — L'identifiant et le nom de votre adaptateur OBD-II couplé sont stockés localement pour que l'application puisse se reconnecter automatiquement.
* **Journal d'activité de l'app** — Un fichier journal enregistrant les événements de cycle de vie de l'application, de connexion Bluetooth, d'interférence de l'adaptateur et de stockage de l'historique. Il n'est partagé que lorsque vous utilisez explicitement le bouton de partage.
* **Enregistreur de diagnostic de conduite** — Un fichier journal par trajet contenant les points GPS, les mesures de vitesse et les calculs de distance, utilisé pour diagnostiquer la précision de la distance et de la navigation. Il n'est partagé que lorsque vous utilisez explicitement le bouton de partage.
* **Enregistrements de diagnostic et journaux de snapshots** — Si vous utilisez l'enregistrement de diagnostic ou la fonction de comparaison de snapshots, un fichier journal est enregistré localement contenant les événements Bluetooth, les commandes de l'adaptateur et les données brutes du véhicule. Il n'est partagé que lorsque vous utilisez explicitement le bouton de partage.

## Localisation

EV Dashboard utilise votre position pour vous localiser sur la carte CarPlay, fournir un guidage détaillé, mesurer la distance et l'efficacité du trajet pendant la conduite et trouver des bornes à proximité.

L'application demande uniquement l'accès « Lorsque l'app est active ». Elle ne demande jamais l'accès « Toujours ». La distance du trajet étant mesurée en continu pendant la conduite, les mises à jour de position peuvent se poursuivre lorsque l'application est en arrière-plan ou que vous utilisez une autre application — cela s'arrête à la fin du trajet.

Votre position est utilisée sur votre appareil et n'est pas envoyée au développeur. Elle n'est ni collectée, ni profilée, ni vendue. Des données de position peuvent être écrites dans les fichiers décrits ci-dessus (l'Enregistreur de diagnostic de conduite et le lieu enregistré avec une session de l'historique) ; ceux-ci ne quittent votre appareil que si vous choisissez de les partager.

## Cartes et navigation

Les cartes, la recherche d'adresse et le calcul d'itinéraire sont fournis par MapKit d'Apple. Lorsque vous recherchez une adresse ou démarrez une navigation, les informations de requête et de position nécessaires sont envoyées à Apple pour obtenir un résultat, et sont traitées conformément à la [politique de confidentialité d'Apple](https://www.apple.com/legal/privacy/). Ces informations ne sont pas envoyées au développeur.

## Mises à jour de la base des bornes

La liste des sites de recharge rapide DC est incluse dans l'application et fonctionne hors ligne. Aucune connexion réseau n'est nécessaire pour parcourir les bornes ou naviguer vers l'une d'elles.

Si vous touchez **Réglages → Navigation → Rechercher une mise à jour**, et seulement dans ce cas, l'application télécharge une base de bornes plus récente. Cela génère deux requêtes : une pour un fichier manifeste hébergé sur theburl.com, et une pour le fichier de données qu'il désigne, hébergé sur GitHub Releases. Il s'agit dans les deux cas de téléchargements ordinaires de fichiers statiques, vérifiés par une somme de contrôle. Aucune information vous concernant, concernant votre appareil ou votre véhicule n'est transmise avec ces requêtes, et il n'existe aucune vérification automatique ou périodique.

## Synchronisation iCloud (facultative)

Si vous activez la synchronisation iCloud, votre historique de conduite et de recharge — y compris le lieu enregistré avec une session — est synchronisé via CloudKit d'Apple avec votre propre compte iCloud privé, afin qu'il reste cohérent sur votre iPhone, iPad et Mac. Ces données sont stockées dans votre iCloud personnel, sont régies par la politique de confidentialité d'Apple et ne sont jamais envoyées au développeur ni à un serveur tiers — le développeur n'y a pas accès. Si vous laissez la synchronisation iCloud désactivée, toutes les données restent uniquement sur votre appareil.

## Bluetooth

L'application communique avec votre adaptateur OBD-II via Bluetooth Low Energy (BLE). Toute la communication Bluetooth s'effectue directement entre votre appareil et l'adaptateur. Aucune donnée Bluetooth n'est transmise à un serveur ou à un tiers.

## Données du véhicule

L'application lit les données de diagnostic de l'ordinateur de bord de votre véhicule via le port OBD-II. Ces données comprennent l'état de la batterie, les températures, les tensions, les pressions des pneus et d'autres mesures de capteurs. Ces données sont affichées sur votre appareil et ne sont transmises nulle part.

## Notifications

Si vous activez le rappel de débranchement, l'application utilise des notifications locales pour vous rappeler de débrancher l'adaptateur OBD-II lorsque la voiture s'éteint. Aucune donnée de notification n'est envoyée à un serveur.

## Conservation des données

Toutes les données sont stockées sur votre appareil. Les fichiers journaux et les enregistrements peuvent être supprimés via l'app Fichiers d'iOS. La désinstallation de l'application supprime toutes les données stockées localement, y compris les paramètres, les destinations enregistrées et les informations d'adaptateur enregistrées. Si vous avez activé la synchronisation iCloud, votre historique reste également dans votre compte iCloud jusqu'à ce que vous le supprimiez depuis l'application ou désactiviez la synchronisation.

## Confidentialité des enfants

L'application ne collecte pas sciemment de données auprès d'enfants de moins de 13 ans.

## Modifications de cette politique

Si cette politique de confidentialité est mise à jour, la version révisée sera publiée sur cette page avec une date actualisée.

## Contact

Si vous avez des questions concernant cette politique de confidentialité, veuillez [ouvrir un ticket](https://github.com/gburlingame/ioniq-app/issues) sur GitHub ou envoyer un e-mail à [greg@theburl.com](mailto:greg@theburl.com).
