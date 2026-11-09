---
layout: default
title: Politique de confidentialité
nav_exclude: true
---

<div style="text-align: right; margin-bottom: 16px;">
  <a href="privacy">English</a> · <a href="privacy-nl">Nederlands</a> · <a href="privacy-de">Deutsch</a> · <strong>Français</strong> · <a href="privacy-es">Español</a> · <a href="privacy-sv">Svenska</a> · <a href="privacy-it">Italiano</a> · <a href="privacy-ko">한국어</a> · <a href="privacy-tr">Türkçe</a> · <a href="privacy-ja">日本語</a>
</div>

# Politique de confidentialité

**Dernière mise à jour : 9 novembre 2026**

EV Dashboard (« l'application ») est développée par Greg Burlingame. Cette politique de confidentialité décrit comment l'application gère vos données.

## Collecte de données

EV Dashboard n'a ni serveur, ni compte, ni connexion. L'application ne contient aucune analyse, publicité ou suivi d'aucune sorte. Le développeur ne reçoit jamais vos données, et rien n'est vendu.

Vos données ne quittent votre appareil que dans les cas suivants, chacun décrit ci-dessous :

* **Partage avec ABRP** — désactivé jusqu'à ce que vous l'activiez et associiez un véhicule ; il envoie les données en direct de ce véhicule directement à ABRP.
* **Synchronisation iCloud** — vos paramètres et votre historique sont synchronisés avec votre propre compte iCloud privé.
* **Apple Plans** — les recherches d'adresses, les adresses de contacts que vous choisissez et les demandes d'itinéraire sont envoyées à MapKit d'Apple.
* **Fichiers que vous partagez** — les journaux, les enregistrements, les exportations et les cartes de partage ne quittent votre appareil que lorsque vous touchez Partager.

La vignette Connexion Internet et les mises à jour de la base des bornes effectuent également des requêtes réseau. Elles ne contiennent aucune information vous concernant ou concernant votre véhicule.

## Données stockées sur votre appareil

L'application stocke les données suivantes localement sur votre appareil :

* **Données de diagnostic du véhicule** — L'état de la batterie, les tensions des cellules, les températures, les données de charge, les pressions des pneus et d'autres mesures de capteurs de votre véhicule sont stockés en mémoire pendant que l'application fonctionne. Ces données ne sont pas conservées entre les lancements de l'application, sauf si vous utilisez une fonction d'enregistrement.
* **Historique de conduite et de recharge** — Lorsque vous utilisez la fonction Historique, les résumés et les échantillons de signaux enregistrés de vos trajets et sessions de recharge (état de charge, énergie, températures et autres mesures) sont enregistrés sur votre appareil afin que vous puissiez les consulter ultérieurement. Une session de recharge peut enregistrer le lieu où elle s'est déroulée. Un trajet enregistre son itinéraire — votre position environ une fois par seconde pendant que vous conduisez — afin de pouvoir l'afficher sur sa carte Parcours. Vous pouvez désactiver cette fonction dans **Réglages → Sessions de conduite → Enregistrer le parcours**, ou supprimer l'itinéraire d'un trajet depuis sa carte Parcours.
* **Photos des sessions** — Une photo que vous ajoutez à une session de recharge ou de conduite est stockée avec cette session.
* **Paramètres de l'application** — Vos préférences (unités, langue, apparence, thèmes, paramètres de graphiques, sélection de l'adaptateur, dispositions des vignettes CarPlay, filtres de bornes, paramètres des pneus et noms des véhicules) sont stockées sur votre appareil et synchronisées via iCloud tant que Synchroniser avec iCloud est activé.
* **Destinations enregistrées** — Les adresses que vous enregistrez pour la navigation, ainsi que vos destinations récentes, sont stockées sur votre appareil et synchronisées avec vos paramètres.
* **Informations sur l'appareil Bluetooth** — L'identifiant et le nom de votre adaptateur OBD-II couplé sont stockés localement pour que l'application puisse se reconnecter automatiquement.
* **Jeton d'association ABRP** — Si vous associez un véhicule à ABRP, le jeton que vous collez depuis l'app ABRP est stocké dans le trousseau de votre appareil. La dissociation du véhicule le supprime.
* **Journal d'activité de l'app** — Un fichier journal enregistrant les événements de cycle de vie de l'application, de connexion Bluetooth, d'interférence de l'adaptateur et de stockage de l'historique. Il n'est partagé que lorsque vous utilisez explicitement le bouton de partage.
* **Enregistreur de diagnostic de conduite** — Un fichier journal par trajet contenant les points GPS (position, cap, vitesse et altitude), les mesures de vitesse du véhicule et les calculs de distance, utilisé pour diagnostiquer la précision de la distance, de l'altitude et de la navigation. Il n'est partagé que lorsque vous utilisez explicitement le bouton de partage.
* **Enregistrements de diagnostic et journaux de snapshots** — Si vous utilisez l'enregistrement de diagnostic ou la fonction de comparaison de snapshots, un fichier journal est enregistré localement contenant les événements Bluetooth, les commandes de l'adaptateur et les données brutes du véhicule. Il n'est partagé que lorsque vous utilisez explicitement le bouton de partage.

## Localisation

EV Dashboard utilise votre position pour vous localiser sur la carte CarPlay, fournir un guidage détaillé, mesurer la distance et l'efficacité du trajet, enregistrer le Parcours d'un trajet, afficher votre altitude et trouver des bornes à proximité.

L'application demande uniquement l'accès « Lorsque l'app est active ». Elle ne demande jamais l'accès « Toujours ». Les mises à jour de position peuvent se poursuivre lorsque l'application est en arrière-plan ou que vous utilisez une autre application : si vous ouvrez l'application alors qu'elle est connectée à votre véhicule, elle maintient une session de localisation en arrière-plan jusqu'à ce que le véhicule s'éteigne ou que l'adaptateur soit hors de portée Bluetooth, et iOS affiche l'indicateur de localisation pendant ce temps. Les relevés GPS pour la distance du trajet et l'itinéraire du Parcours ne sont effectués que pendant que vous conduisez.

Votre position n'est pas envoyée au développeur, et elle n'est ni profilée ni vendue. Elle est stockée sur votre appareil dans l'historique et les fichiers décrits ci-dessus, qui quittent votre appareil via la synchronisation iCloud ou lorsque vous choisissez de les partager. Si vous activez le partage avec ABRP, la position de votre véhicule est envoyée à ABRP (voir Partage avec ABRP).

## Cartes et navigation

Les cartes, la recherche d'adresse et le calcul d'itinéraire sont fournis par MapKit d'Apple. Lorsque vous recherchez une adresse, choisissez l'adresse d'un contact ou démarrez une navigation, les informations de requête et de position nécessaires sont envoyées à Apple pour obtenir un résultat, et sont traitées conformément à la [politique de confidentialité d'Apple](https://www.apple.com/legal/privacy/). Ces informations ne sont pas envoyées au développeur.

## Contacts

Si vous activez **Afficher les contacts dans la recherche** lors de l'ajout d'une destination sur votre appareil mobile, l'application demande l'accès à vos contacts et affiche leurs adresses au fil de votre saisie, dans l'application et dans CarPlay. Lorsque vous en choisissez un, son adresse est envoyée à MapKit d'Apple pour la placer sur la carte, et le nom du contact est enregistré comme étiquette de la destination. L'application ne stocke pas vos contacts et ne les envoie nulle part ailleurs.

## Appareil photo et photos

Toucher le carré photo d'une session vous permet de prendre une photo avec l'appareil photo ou d'en choisir une dans votre photothèque. Une photo que vous prenez est stockée avec la session, et l'original en pleine résolution est également enregistré dans votre photothèque. Pour cela, l'application demande un accès en ajout uniquement : elle peut ajouter des photos à votre photothèque, mais ne peut pas voir les photos qu'elle contient. Lorsque vous choisissez une photo dans votre photothèque, le sélecteur propre à iOS ne donne à l'application que la photo que vous choisissez.

## Mouvement et remise en forme

L'application utilise le baromètre de votre appareil afin de suivre les montées et les descentes dans la vignette Altitude de CarPlay et sur la carte Parcours, ce qui compte surtout sur les véhicules dont le système CarPlay ne communique pas l'altitude. Elle demande pour cela l'accès à Mouvement et remise en forme. Les relevés du baromètre sont utilisés sur votre appareil et ne sont envoyés nulle part.

## Partage avec ABRP (facultatif)

ABRP (A Better Routeplanner) est un service de planification d'itinéraires exploité par Iternio. Le partage est désactivé jusqu'à ce que vous activiez **Partager les données en direct avec ABRP** dans **Réglages → Partage de données → ABRP** et associiez un véhicule avec le jeton de votre app ABRP. Lors de l'association, l'application envoie le jeton à ABRP pour le vérifier.

Tant qu'un véhicule associé est allumé, l'application transmet ses données en direct, sans intermédiaire, de votre appareil aux serveurs d'ABRP (api.iternio.com) : l'heure ; l'état de charge, l'énergie de la batterie et l'état de santé ; la puissance, le courant et la tension ; la vitesse ; la position (latitude, longitude, altitude et cap) ; s'il est en charge, en recharge rapide DC ou stationné ; l'odomètre ; les températures de la batterie, de l'habitacle et extérieure ; et les pressions des pneus. Le VIN n'est pas envoyé. Les relevés qui n'ont pas pu être envoyés sont conservés en mémoire, dans une certaine limite, jusqu'au rétablissement de la connexion, et sont supprimés si l'application se ferme.

Ces données ne passent pas par le développeur. ABRP les traite conformément à sa propre politique de confidentialité. Pour arrêter le partage, désactivez l'option ou dissociez le véhicule.

## Vignette Connexion Internet

La vignette Connexion Internet de CarPlay mesure votre connexion. Tant que la vignette est affichée sur votre écran CarPlay, l'application demande une page de test vide environ toutes les 30 secondes, en alternant entre Cloudflare (cp.cloudflare.com) et Google (connectivitycheck.gstatic.com). Ces requêtes ne contiennent aucune information vous concernant ou concernant votre véhicule, bien que, comme toute requête Internet, elles révèlent votre adresse réseau à ces services. Aucune requête n'est effectuée tant que la vignette n'est pas affichée à l'écran.

## Mises à jour de la base des bornes

La liste des sites de recharge rapide DC est incluse dans l'application et fonctionne hors ligne. Aucune connexion réseau n'est nécessaire pour parcourir les bornes ou naviguer vers l'une d'elles.

Si vous touchez **Réglages → Navigation → Rechercher une mise à jour**, et seulement dans ce cas, l'application télécharge une base de bornes plus récente. Cela génère deux requêtes : une pour un fichier manifeste hébergé sur theburl.com, et une pour le fichier de données qu'il désigne, hébergé sur GitHub Releases. Il s'agit dans les deux cas de téléchargements ordinaires de fichiers statiques, vérifiés par une somme de contrôle. Aucune information vous concernant, concernant votre appareil ou votre véhicule n'est transmise avec ces requêtes, et il n'existe aucune vérification automatique ou périodique.

## Synchronisation iCloud

Les deux types de synchronisation sont activés par défaut et peuvent être désactivés dans **Réglages → iCloud**.

* **Réglages** — Tant que **Synchroniser avec iCloud** est activé, les paramètres de l'application, les destinations enregistrées, les paramètres des pneus et les noms des véhicules sont synchronisés via le stockage clé-valeur iCloud d'Apple avec votre propre compte iCloud, afin qu'ils soient identiques sur tous vos appareils. La reconnexion automatique à un adaptateur se règle sur chaque appareil et n'est pas synchronisée.
* **Historique** — Tant que la synchronisation de l'Historique est activée, votre historique de conduite et de recharge — y compris les photos des sessions, le lieu enregistré avec une session de recharge et l'itinéraire du Parcours de chaque trajet — est synchronisé via CloudKit d'Apple avec votre propre compte iCloud privé, afin qu'il reste cohérent sur votre iPhone, iPad et Mac.

Les deux ensembles de données sont stockés dans votre iCloud personnel, sont régis par la politique de confidentialité d'Apple et ne sont jamais envoyés au développeur ni à un serveur tiers — le développeur n'y a pas accès. Si vous désactivez les deux synchronisations, toutes les données restent uniquement sur votre appareil.

## Bluetooth

L'application communique avec votre adaptateur OBD-II via Bluetooth : Bluetooth Low Energy (BLE) pour la plupart des adaptateurs, et Bluetooth Classic, par l'intermédiaire du framework External Accessory d'Apple, pour l'OBDLink MX+, le Vgate vLinker FS et le Vgate vLinker MS. Toute la communication Bluetooth s'effectue directement entre votre appareil et l'adaptateur. Aucune donnée Bluetooth n'est transmise à un serveur ou à un tiers.

## Données du véhicule

L'application lit les données de diagnostic de l'ordinateur de bord de votre véhicule via le port OBD-II. Ces données comprennent l'état de la batterie, les températures, les tensions, les pressions des pneus et d'autres mesures de capteurs. Ces données sont affichées et stockées sur votre appareil, et ne sont transmises nulle part, sauf vers votre propre iCloud tant que la synchronisation de l'Historique est activée, et vers ABRP si vous activez le partage.

## Notifications

Si vous activez le rappel de débranchement, l'application utilise des notifications locales pour vous rappeler de débrancher l'adaptateur OBD-II lorsque la voiture s'éteint. Aucune donnée de notification n'est envoyée à un serveur.

## Conservation des données

Toutes les données sont stockées sur votre appareil. Les fichiers journaux et les enregistrements peuvent être supprimés via l'app Fichiers d'iOS. La désinstallation de l'application supprime toutes les données stockées localement, y compris les paramètres, les destinations enregistrées et les informations d'adaptateur enregistrées. Les photos que l'application a enregistrées dans votre photothèque y restent jusqu'à ce que vous les supprimiez. Si vous avez activé la synchronisation iCloud, votre historique reste également dans votre compte iCloud jusqu'à ce que vous le supprimiez depuis l'application ou désactiviez la synchronisation. Les données déjà envoyées à ABRP sont conservées par ABRP conformément à sa propre politique.

## Confidentialité des enfants

L'application ne collecte pas sciemment de données auprès d'enfants de moins de 13 ans.

## Modifications de cette politique

Si cette politique de confidentialité est mise à jour, la version révisée sera publiée sur cette page avec une date actualisée.

## Contact

Si vous avez des questions concernant cette politique de confidentialité, veuillez [ouvrir un ticket](https://github.com/gburlingame/ioniq-app/issues) sur GitHub ou envoyer un e-mail à [greg@theburl.com](mailto:greg@theburl.com).
