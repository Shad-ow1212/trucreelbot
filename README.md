# Truc Réel Bot
#### Projet de bot débile qui ne sert à rien
## Sommaire :
1. Installation
2. Commandes
3. Contribution

## 1. Installation
Pour faire tourner ce bot sur votre machine, vous devez d'abord avoir un compte de bot enregistré chez discord.
**Etapes d'installation** :  
* Cloner ce repo sur votre machine  
* Créer un fichier token.txt et y coller uniquement la clé d'api fournie par discord  
* dans /data/csv/, créer :  
    * connu.csv (noms de personnes connues, personnalisables, séparés par des retours à la ligne)  
    * ids.csv (les ids publics discord de vos amis, séparés par des retours à la ligne)  
    * inconnu.csv (des noms ou des objets, peu importe, séparés par des retours à la ligne)  
    * places.csv (des lieux, concepts... etc séparés par des retours à la ligne)  
* **Linux** : Lancer setup.sh pour démarrer l'installation et lancer le bot pour la première fois   
* **Windows** : Lancer setup.ps1 dans un terminal powershell pour démarrer l'installation et lancer le bot pour la première fois   
* A partir de maintenant, pour démarrer le bot, lancer main.py avec python dans un terminal.      

## 2. Commandes   
Voici la liste des commandes utilisables avec ce bot. Le préfixe par défaut est "+" mais il est modifiable dans config.py, tout comme les mots clés des commandes, dans main.py.  
* *test* : Renvoie un embed de test, avec quelques petites infos, confirme que le bot fonctionne corectement.  
* *crève*/*kys*/*sleep* : Eteint le bot   
* *reboot* : Relance le bot (et surtout rechargetous les scripts)  
* *stat* : Envoie le nombre de message quel'auteur de la commande. Fonctionne aussi avecles mentions.  
* *edit* : Permet la modifications de plusieursfichiers importants pour le bot : les csv,contenant des informations utiles pour hello.pyou encore timers.py. A complêter  
* *bissap* : envoie un gif de bissap  
* *sixseven*/*67* : envoie blehhh x3  
* *admin* : vérifie les permissions del'utilisateur et permet d'executer d'autrescommandes.  
* *admin test* : 
    
Il existe également plusieurs "autocommandes" qui sont au nombre de 2 pour l'instant :  
* La méthode autocommands.reacts.react(*string*) :  
    * Retourne une liste d'emojis lettres (si le mot n'a pas de répétitions), permettant d'ajouter ces réactions à un message  
* Les méthodes de autocommands.salut  
    * sentence(*array*) : retourne une phrase type "Salut c'est [mot de connu/inconnu/ids.csv] de [mot de places.csv]    
    * init() : initialise la méthode avec les csv fournis    
    * hello() : retourne une phrase de Mr. Frog  


## 3. Contribution




