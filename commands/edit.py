import csv
import os
from config import TIMERS

async def run(bot, message, args):
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
            with open(f"./data/csv/{args[1]}.csv", mode = "w", encoding="utf-8") as file:
                file.write("\n".join(lines))
                file.close()
                await message.channel.send("Supprimé avec succès mouhehe >:3")
        
        else:
            await message.channel.send(f"Euh... j'ai aucune commande pour {args[1]} désolé ^^'")