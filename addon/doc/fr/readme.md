## TCA SystemUtilities.

Petite extension qui nous permet d'exécuter rapidement certaines actions de Windows via le raccourci clavier. 
Il est capable d'effectuer une réparation du système avec SFC. Il peut copier les informations système dans le presse-papiers, entrer dans le BIOS et bien plus encore. 
Nous pouvons également ouvrir le site officiel pour obtenir des extensions pour NVDA de manière directe, éliminer les configurations et les extensions sur les écrans sécurisés.

* Auteur: Peter Reina <peterrc87@gmail.com>
* Compatibilité: NVDA 2018 à 2023.3

## Fonctions du système:

* Arrêt du système: Arrête Windows 
 de plus, il émet le son classique de fermeture de Windows. Il nous avertit que le système va s'arrêter grâce à un message.
 Il nous offre la possibilité de fermer ou d'annuler l'arrêt pendant 3 secondes.

* Redémarrage du système: Redémarre Windows 
 de plus, il émet le son classique de fermeture de Windows. Il nous avertit que le système va redémarrer grâce à un message.
 Il nous offre la possibilité de fermer ou d'annuler le redémarrage pendant 3 secondes.

* Annuler (l'arrêt ou le redémarrage): Il nous permet d'annuler l'une des 2 options ci-dessus (l'arrêt ou le redémarrage) 
De plus, il nous avertit avec un message qui annule l'arrêt / le redémarrage.
 ! Remarque! Nous n'avons que 3 secondes pour effectuer cette action.

* Mettre en veille: Il nous permet de mettre en mode de mise en veille le système, confortablement à partir de NVDA.

* Redémarrer et entrer en Mode Sans échec avec les fonctions réseau: Cette fonctionnalité très compliquée à mettre, à partir de TCA SystemUtilities est un truc d'enfant. 
Nous permet très facilement d'entrer dans Windows avec des fonctions limitées sans charger des services ou des programmes inutiles, à partir de là, nous pouvons faire un nettoyage plus approfondi, éliminer les programmes indésirables, les logiciels malveillants (malware) et bien plus encore. 
 ! Remarque importante! 
Dans ce mode, dans les systèmes précédant  à Windows 10, le service audio peut ne pas être activé, par conséquent, nous ne pouvons pas avoir la synthèse vocale du lecteur d'écran. 
Une fois cette fonction activée, nous devons alors le désactiver, nous pouvons le faire à partir du même menu TCA SystemUtilities, dans la section: "Arrêt du système".

* Redémarrer en Mode normal: Il nous permet de désactiver le Mode Sans échec si nous l'avons activé, il retourne au démarrage de Windows à ses valeurs normales (ils chargent tous les services et programmes que nous avons au démarrage). 

* Mettre en veille prolongée: Il nous permet  la mise en veille prolongée du système, confortablement à partir de NVDA.

* Entrer dans le BIOS-UEFI: Nous pouvons confortablement à partir de Windows et avec NVDA en lui indiquant au PC d'entrer dans le BIOS-UEFI lors du prochain redémarrage. 
Pas besoin d'appuyer ou de connaître la touche, directement et facilement. 
(Remarque importante!) dans le BIOS-UEFI il n'y a pas de service audio, par conséquent, nous ne pourrons pas utiliser un lecteur d'écran dans son interface). Une fois que nous le voulons il retournera à notre système, pour cela nous pouvons appuyer sur la combinaison de touches: CTRL+ALT+Supr.

* Ouvrir la console CMD dans le chemin actuel: Avec un simple raccourci clavier, nous pouvons ouvrir le symbole du système dans Windows (CMD) et il prendra le chemin de n'importe quel dossier où se trouve le focus.

* Ouvrir la console CMD en tant qu'administrateur: Avec un simple raccourci clavier, nous pouvons ouvrir le symbole du système dans Windows, avec tous les privilèges en tant qu'administrateur (uniquement dans les systèmes avant Windows 10, il prend le chemin du dossier où se trouve le focus, dans d'autres, il s'ouvrira dans System32).

* Supprimer le presse-papiers et son historique: Confortable fonctionnalité qui vide tout ce que nous avons dans le presse-papiers, dans Windows 10 et 11, il nettoie également tout ce que nous avons dans l'historique si nous l'avons activé.

* Redémarrer l'Explorateur: Nous redémarre confortablement à partir de NVDA l'Explorateur Windows. 
Nous pouvons le faire à partir  d'un raccourci que nous lui attribuons, ou à partir du menu TCA SystemUtilities.

* Fermer toutes les applications: Force à fermer tous les processus actifs qui ne font pas partie de Windows (Remarque! Tous les processus seront obligés de fermer, vous ne pouvez donc pas enregistrer ni documents, ni projets, et même le NVDA sera fermé).

* Fermer les tâches qui ne répondent pas: TCA SystemUtilities tentera de fermer les processus qui ne répondent pas. 

* Connaître l'architecture du système: Il nous dira quelle est l'architecture de Windows (32 ou 64 Bits). 
 
* Masquer les dossiers: Il nous permet de mettre l'attribut de masqués dans le dossier où nous sommes, c'est-à-dire que ce dossier ne sera pas affiché (nous devons y entrer dans celui-ci pour qui prenne effet).

* Afficher les dossiers masqués: Cette fonction nous permet de rendre visibles tous les dossiers et fichiers masqués (valable dans des clés USB, disques externes et plus), très utile lors du branchement de n'importe quel périphérique externe. Nous devons entrer dans le dossier et appuyer sur le raccourci  clavier.
 

## Fonctions de réparation du système. 

* Faire une analyse du système avec SFC: Il nous permet d'effectuer une analyse / réparation du système de fichiers de Windows SFC / SCANNOW.

* Désactiver l'espace de stockage réservé: Il rend les près de 10 Go que Windows kidnappe  de notre disque dur pour les mises à jour (il n'est pas nécessaire d'avoir cela activé pour les mises à jour).

* Activer l'espace de stockage réservé: Si vous souhaitez toujours activer cette fonction Windows et forcer votre disque dur à laisser près de 10 Go d'espace réservé, avec cette action, vous l'activez.

* Nettoyer le cache DNS: Supprime le cache DNS de Windows rapidement et directement (vous pouvez améliorer les problèmes de navigation sur Internet). 

* Nettoyer configuration sauvegardé sur les écrans sécurisés: Il élimine toutes les extensions et configurations que nous avons copiées pour exécuter sur les écrans sécurisés, laissant  à NVDA tel qu'il vient nativement. 

* Nettoyage de disque: Il nous permet de lancer le nettoyeur de disque de Windows, mais avec des options beaucoup plus avancées. Il nettoiera chacun des disques et périphériques de stockage que nous avons connectés au système. 
La première fois que nous l'exécutons, il s'affiche une boîte de dialogue, pour créer un profil de nettoyage, nous pouvons cocher toutes les cases que nous voulons pour nettoyer plus exhaustivement. Il est convenable que nous appuyions sur le bouton: "Créer un profil" il est nécessaire de le faire qu'une seule fois. Nous avons une case à cocher que nous pouvons cocher si nous ne voulons plus afficher ce dialogue. 
 
* Réparer le système avec Dism: Il effectue une analyse profonde et essaye de réparer les problèmes dans Windows.



## Fonctions directes du presse-papiers:

* Copier dans le presse-papiers la liste des dossiers et des fichiers: 
La liste des éléments du chemin où nous sommes se copiera dans le presse-papiers, nous pouvons donc le coller dans n'importe quel endroit éditable.

* Copier dans le presse-papiers les informations sur les cartes son: Il nous permet de copier directement les informations sur tous les périphériques de son que nous avons dans le système.
Nous pouvons donc le coller dans n'importe quel endroit éditable. 

* Copier les informations de l'ensemble du système dans le presse-papiers: Il nous permet de copier directement, un résumé de notre système. 
Nous pouvons donc le coller dans n'importe quel endroit éditable. 

* Copier dans le presse-papiers le chemin: Le chemin  du dossier où nous sommes se copiera dans le presse-papiers. 
 Nous pouvons donc le coller dans n'importe quel endroit éditable. 
 

## Options de Sécurité Windows:

Contrôle de compte d'utilisateur (uac).

* Activer le Contrôle de compte d'utilisateur (uac): Établit le niveau du contrôle de compte d'utilisateur en 34 (activé).

* Désactiver le Contrôle de compte d'utilisateur (uac): Établit le niveau du contrôle de compte d'utilisateur en 0 (désactivé).

Windows Defender.

* Analyser le démarrage du système: Il effectue directement une analyse de virus et de logiciels malveillants (malware) des fichiers appartenant au secteur de démarrage de Windows (Boot sector).
 
* Analyse complète: Il lance directement une analyse de virus de l'ensemble du système. 

* Analyse rapide: Il lance directement une analyse de virus et de logiciels malveillants (malware) rapide (des parties essentielles du système). 
 
* Numériser des fichiers compressés: Active directement que l'antivirus de Windows puisse numériser des fichiers compressés (rar, zip, ace, tar, etc.).
 
* Ne pas numériser des fichiers compressés: Désactive directement que l'antivirus de Windows puisse numériser des fichiers compressés (rar, zip, ace, tar, etc.).
* Liste des fichiers en quarantaine dans le presse-papiers: Il copie dans le presse-papiers, une liste et les informations de tous les fichiers que  l'antivirus de Windows a mis en quarantaine.


## Options multimédia.

* Activer la webcam: Il nous permet confortablement à partir de NVDA activer la webcam si nous l'avons (laissez-la prête à l'emploi).

* Désactiver la webcam: Il nous permet confortablement à partir de NVDA de désactiver la webcam si nous l'avons (désactivez-la, aucun programme ne peut l'utiliser).

* Mélangeur de volume: Il nous permet d'ouvrir le Mélangeur de volume de Windows confortablement à partir de NVDA. 
Nous pouvons le faire à partir du menu TCA SystemUtilities, dans la section: "Voix et multimédia", ou nous pouvons lui attribuer un raccourci clavier.

* Ouvrir Options de la voix: Nous ouvrent rapidement les Options ou Propriétés Synthèse vocale. Ici, nous pouvons choisir notre voix TTS installée dans le système par défaut. 
 
 * Ouvrir Options du Son: Il nous permet d'ouvrir directement les options du son du Panneau de configuration (Son, Lecture, Enregistrement, Communications). 
 


## Ouvrir rapidement certaines fonctions système:
* Ouvrir Optimiser les lecteurs: Il nous permet d'ouvrir directement cette fonctionnalité intéressante de Windows, pour améliorer les performances de nos disques durs. 
 
* Ouvrir Table des caractères: Il ouvre directement cette fonctionnalité intéressante de Windows. Ce qui nous permet de choisir et de connaître l'un des signes, chiffres et lettres existants du système. 
Très utile pour connaître des signes rares ou difficiles à obtenir avec le clavier.
 
* Ouvrir Assistant Enregistrer les mots de passe utilisateurs: Ouvre l'assistant de cet utilitaire Windows très utile mais peu connu.
Cela nous permet d'enregistrer les informations d'identification (noms, mots de passe et plus), des comptes d'utilisateurs que nous avons dans le système.
* Ouvrir Assistant Transfert de fichiers par Bluetooth: Il nous permet de lancer directement cet assistant afin de recevoir ou d'envoyer des fichiers via nos périphériques Bluetooth. 
* Ouvrir Options de dossier: Il ouvre directement cette fonctionnalité largement utilisée, pour gérer l'Explorateur Windows, les vues des dossiers, la visualisation des extensions de fichiers et plus encore. 
* Ouvrir Dossier Roaming: Il ouvre directement le dossier  Appdata>Roaming (nous trouvons ici le dossier  de configuration NVDA, et de nombreux autres programmes).
* Ouvrir Gestion des disques: Il nous permet d'ouvrir directement cette fonctionnalité intéressante pour gérer les disques, partitions et autres périphériques de stockage, installés sur notre PC.
 
* Assistant pour enregistrer le mot de passe du système: 
Nous ouvrirons cet assistant utile mais peu connu qui nous permet d'enregistrer  le mot de passe de Windows, pour pouvoir le récupérer à partir d'un périphérique externe.
 
* Ouvrir Moniteur de ressources: Nous pouvons ouvrir directement ce puissant outil de Windows, peu connu. C'est comme un gestionnaire des tâches amélioré, nous pouvons gérer tous les services, applications et processus qui s'exécutent dans notre système.
En outre, nous pouvons savoir combien de mémoire, de disque, de réseau et plus qu'ils consomment.
 
* Ouvrir Gestionnaire de périphériques: Il nous permet d'ouvrir cette fonctionnalité utile de Windows pour gérer le matériel et les contrôleurs de l'ordinateur.
 
* Connaître la version de Windows: Nous ouvriront les informations avec la version du système d'exploitation. 
* Ouvrir la boutique officielle d'extensions: Il ouvrira avec notre navigateur prédéterminé, le site officiel pour obtenir les extensions pour NVDA.

## Remarque importante!

Tous et chacun des raccourcis clavier, peuvent être attribués, selon le goût personnel à partir du dialogue: Préférences > Gestes de commandes de NVDA.

## Changements pour la version 0.8.

* À partir de cette version TCA SystemUtilities change sa nomenclature de version (pour être compatible avec NVDA 2023.3)
Maintenant, les versions auront 3 chiffres ce sera 0.8.2.
* Nouvelle fonction: désactiver le Contrôle de compte d'utilisateur (uac).
* Nouvelle fonction: activer le Contrôle de compte d'utilisateur (uac).
* À la fois la fonction activer, ainsi que la fonction désactiver le Contrôle de compte d'utilisateur seront dans le menu  de TCA SystemUtilities dans la catégorie: Sécurité Windows;
De même, nous pouvons établir des raccourcis clavier si nous le souhaitons à partir  du dialogue Gestes de commandes.

## Changements pour la version 06.

* Nouvelle fonction interne Pour prendre le chemin du système (path), maintenant il y en a 2, en cas d'échec, TCA SystemUtilities tentera d'utiliser l'autre.
(L'une des fonctions a été développée par: Héctor Benítez).
* Nouvelle fonction: fermez tous les processus actifs.
* Fermer des tâches qui ne répondent pas sous Windows.
* Corrigé, le menu de TCA SystemUtilities ne sera plus répété si les extensions sont rechargées.
(Courtoisie de Héctor Benítez).
* Corrigé: Il n'y a plus de raccourcis claviers par défaut.

## Changements pour la version 05.

* Nouvelle fonction pour le nettoyage des extensions et configurations sur les écrans sécurisés.
* Nouvelle fonction supprimer le presse-papiers, y compris l'historique dans Windows.
* Nouvelle fonction ouvrir la console CMD dans le chemin actuel.
* Nouvelle fonction ouvrir la console CMD avec les privilèges en tant qu'administrateur.
* Nouvelle fonction: Désactiver l'espace de stockage réservé dans Windows.
* Nouvelle fonction: Activer l'espace de stockage réservé dans Windows.
* Fonction corrigée et optimisée pour obtenir l'objet, avec cela, ils améliorent plusieurs fonctions telles que: copier le chemin dans le presse-papiers, copier la liste des fichiers dans le presse-papiers, masquer  ou afficher des fichiers et des dossiers.


## Changements pour la version 04.

* Nouvelle fonction pour entrer dans le BIOS-UEFI du système  (dans la section: "Arrêt du système").
* Le menu a été modifié de: "Son et voix", en: "Voix et multimédia".
* 2 nouvelles fonctions dans la section: "Voix et multimédia" (activer / désactiver la webcam).
* Nouvelle fonction: "Nettoyer le cache DNS" (dans la section "Réparation et optimisation").
* Restructuration de la documentation de l'extension.
* Traduit en italien.
* Compatible avec NVDA 2022.1.

* Correction de sécurité (sys.path.remove())


## Changements pour la version 03.
* Dans cette version TCA SystemUtilities elle est déjà entièrement compatible avec le nouveau système: Windows 11.
* Nouveau menu: Sécurité Windows 
avec plusieurs options liées à l'antivirus de Windows.
* Une autre option dans le menu: Arrêt du système, l'option: "Mettre en veille prolongée le système".
* Dans cette version, l'extension est traduite dans les  langues: arabe, portugais (Portugal, portugais Brésil) et roumain.


## Changements pour la version 02.

* Dans cette version, l'extension a un menu confortable d'où nous pouvons exécuter la plupart de ses fonctionnalités (pas tous). 
Celui-ci se trouve dans le Menu: "Outils" de NVDA, et a le nom de l'extension: "TCA SystemUtilities".
* Dans cette version, ont été retirés tous les raccourcis fourni par défaut, vous devez donc désormais attribuer les raccourcis à l'une des fonctions, à partir du menu: "Gestes de commandes" de NVDA.
* Plus de fonctions dans les sections: Arrêt du système, Explorateur Windows, Son et voix, Réparation du système.
* Optimisation de l'ensemble du code de l'extension.

***

Code du projet sur GitHub: 
[https://github.com/peterrc87/TCA-SystemUtilities-NVDA-Complemento](https://github.com/peterrc87/TCA-SystemUtilities-NVDA-Complemento)
