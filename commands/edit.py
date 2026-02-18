import csv
import os
from config import TIMERS
import autocommands.timer as timer

async def run(bot, message, args):
    if not args:
        await message.channel.send("Euweuweu jsais pas quoi faiiiiiiire TvT")
        return
    if args[0] == "csv":
        if len(args) - 1 < 2:
            await message.channel.send("Hum... tu as oublié un truc je crois haha x)")
            return
        liste_csv = []
        for elem in os.listdir("./data/csv"):
            if elem.endswith(".csv"):
                liste_csv.append(elem)
        if (args[2]+".csv") not in liste_csv:
            await message.channel.send("Oulah... pas de fichier correspondant :(")
            return

        if args[1] == "add":
            if not args[3:]:
                await message.channel.send("Euuh... tu as oublié de préciser quoi ajouter au csv x)")
                return
            with open(f"./data/csv/{args[2]}.csv", "a+", encoding="utf-8") as file:
                file.seek(0, 2)
                if file.tell() > 0:
                    file.write("\n")
                file.write(" ".join(args[3:]))
                file.close()
                await message.channel.send("Hehe, c'est tou bon :3")

        elif args[1] == "display":
            content = []
            with open(f"./data/csv/{args[2]}.csv", mode ="r", encoding="utf-8")as file:
                for i, line in enumerate(file, start=1):
                    content.append(f"{i}) {line.strip()}")
                    if i%10 == 0:
                        await message.channel.send("\n".join(content))
                        content.clear()
                await message.channel.send("\n".join(content))
                file.close()
        
        elif args[1] == "delete":
            if not args[3:]:
                await message.channel.send("Hum actually je sais pas quoi supprimer :/")
                return
            if not args[3].isdigit():
                await message.channel.send("ah... c'est pas un index ca mdr")
                return
            with open(f"./data/csv/{args[2]}.csv", mode = "r", encoding="utf-8") as file:
                lines = file.read().splitlines()
                file.close()
            if int(args[3]) > len(lines) or int(args[3]) <= 0:
                await message.channel.send("Euuhh- tu as mis un index trop grand ://")
                return
            lines.pop(int(args[3]) - 1)
            with open(f"./data/csv/{args[2]}.csv", mode = "w", encoding="utf-8") as file:
                file.write("\n".join(lines))
                file.close()
                await message.channel.send("Supprimé avec succès mouhehe >:3")
        
        else:
            await message.channel.send(f"Euh... j'ai aucune commande pour {args[1]} désolé ^^'")
    
    elif args[0] == "timer": #!edit timer add prout     !edit timer delete 3      !edit timer display
        if len(args) < 2:
            await message.channel.send("Euuuh, il manque un truc la je crois 0.0")
            return
        if args[1] == "add":
            if not args[2].isdigit():
                await message.channel.send(f"Mmmh... c'est pas un seuil ca... c'est juste {args[2]}")
                return
            if int(args[2]) <= 0:
                await message.channel.send(f"Met un seuil positif !! >:3")
            temp = timer.Timer(int(args[2]), " ".join(args[3:]))
            TIMERS.append(temp)
        if args[1] == "display":
            temp = ""
            i = 0
            for t in TIMERS:
                temp += (f"{i+1}) Nb de messages nécessaires : {t.seuil+1}, messages envoyés : {t.compte}, réponse : {t.reponse}\n")
                i+=1
                if i%10 == 0:
                    await message.channel.send(temp)
                    temp = ""
            await message.channel.send(temp)
        if args[1] == "delete":
            if not args[2].isdigit():
                await message.channel.send(f"Mmmh... c'est pas un index ca... c'est juste {args[2]}")
                return
            if int(args[2]) <= 0 and int(args[2]) <= len(TIMERS):
                await message.channel.send(f"Il faut mettre un  VRAI index :333")
                return
            TIMERS.pop(int(args[2]) - 1) 
    else:
        await message.channel.send("J'ai pas de commande pour edit ;-;")