# Truc Réel Bot
#### Projet de bot débile qui ne sert à rien
## Sommaire :
1. Installation
2. Commandes
3. Contribution

## 1. Installation
Pour faire tourner ce bot sur votre machine, vous devez d'abord avoir un compte de bot enregistré chez discord.
**Etapes d'installation** :  
    - Cloner ce repo sur votre machine  
    - Créer un fichier token.txt et y coller uniquement la clé d'api fournie par discord  
    - dans /data/csv/, créer :  
        - connu.csv (noms de personnes connues, personnalisables, séparés par des retours à la ligne)  
        - ids.csv (les ids publics discord de vos amis, séparés par des retours à la ligne)  
        - inconnu.csv (des noms ou des objets, peu importe, séparés par des retours à la ligne)  
        - places.csv (des lieux, concepts... etc séparés par des retours à la ligne)  
    - **Linux** : Lancer setup.sh pour démarrer l'installation et lancer le bot pour la première fois   
    - **Windows** : Lancer setup.ps1 dans un terminal powershell pour démarrer l'installation et lancer le bot pour la première fois   
    - A partir de maintenant, pour démarrer le bot, lancer main.py avec python dans un terminal.      

## 2. Commandes   
Voici la liste des commandes utilisables avec ce bot. Le préfixe par défaut est "!" mais il est modifiable, tout comme les 
mots clés des commandes, dans main.py.  
    - *test* : Retourne "Ok ! Tout marche :3" si le bot est fonctionnel  
    - *crève*/*kys*/*sleep* : Eteint le bot  
    - *stat* : Retourne "[pseudo de l'utilisateur] a envoyé [x] messages sur ce serveur :D"
    - *editcsv* : permet la modification des fichiers .csv dans /data/csv. L'arg 0 permet de choisir les modification apporté (add, display ou delete). L'arg 1 doit donner le nom *SANS L'EXTENSION* du fichier .csv souhaité. Pour display, aucun autre argument n'est requis. Pour add, il suffit d'indiquer ensuite ce que vous voulez ajouter (aucune mise en format n'est nécessaire). Pour delete, il suffit de mettre l'index *STRICTEMENT POSITIF* de l'élément que vous souhaitez supprimer. Pour aider, l'index de chaque ligne du csv est écrit lors d'un "[!editcsv display nom_du_ficher]".
Il existe également plusieurs "autocommandes" qui sont au nombre de 2 pour l'instant :  
    - La méthode autocommands.reacts.react(*string*) :  
        Retourne une liste d'emojis lettres (si le mot n'a pas de répétitions), permettant d'ajouter ces réactions à un message  
    - Les méthodes de autocommands.salut  
        sentence(*array*) : retourne une phrase type "Salut c'est [mot de connu/inconnu/ids.csv] de [mot de places.csv]  
        init() : initialise la méthode avec les csv fournis  
        hello() : retourne une phrase de Mr. Frog  


## 3. Contribution




