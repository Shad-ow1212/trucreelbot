import os
import importlib
import random
import discord
import discord.opus
import re
discord.opus._load_default()
from discord.ext import commands

import autocommands.salut as salut
import autocommands.reacts as reacts
salut.init()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

COMMANDS = {
    "test": "commands.test",
    "crève" : "commands.shutdown",
    "kys" : "commands.shutdown",
    "sleep" : "commands.shutdown",
    "stat" : "commands.stat",
    "editcsv" : "commands.editcsv",
    "reloadcsv" : "commands.reloadcsv"
}

SALUTATIONS = ["salut", "bonjour", "coucou", "bonsoir", "enchanté", "hi", "hey", "hewo", "bonjoir", "bonjoouj"]
REPONSES = ["salut", "bonjour", "coucou", "bonsoir", "re", "hey", "enchanté", "bonjoir", "bonjoouj"]

MOTSREACTIONS = {"npac": "npac",
                 "prout": "prout"}

from autocommands.message_timer import Timer
GPERDU = Timer(5, "J'ai perdu")

from autocommands.database import Database
from autocommands.message_counter import MessageCounter
from listeners.message_listener import register_message_listener

db = Database("data/botdata.db")
counter = MessageCounter(db)
bot.db = db
register_message_listener(bot, counter)

OWNER_ID = 712600626223120478

def getToken(file):
    f = open(file)
    token = f.read()
    f.close()
    return token


@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user} :3")

    await db.connect()
    await db.init_schema()

    for guild in bot.guilds:
        if guild.text_channels:
            channel = guild.text_channels[7]
            await channel.send("Salut :3")
            break

@bot.event
async def on_message(message):
    print(message.content)
    if message.author.bot:
        return
    
    await GPERDU.verif(message)

    #cette ligne est infernale mais j'ai pas trouvé mieux. Permet de considérer aussi les mots 
    if any(rep in re.sub('[!,.?]', '', i) for i in message.content.lower().split() for rep in SALUTATIONS):
        await message.channel.send(f"{salut.sentence(random.choice(REPONSES))}")
    
    if "hello" in message.content.lower():
        await message.channel.send(f"{salut.hello()}")

    for mot, react in MOTSREACTIONS.items():
        if mot in message.content.lower():
            reactArray = reacts.react(react)
            for i in reactArray:
                await message.add_reaction(i)

    
    if not message.content.startswith("!"):
        return

    parts = message.content[1:].split()
    if not parts:
        return

    cmd_name = parts[0].lower()
    args = parts[1:]

    if cmd_name not in COMMANDS:
        await message.channel.send(f"Commande inconnue : `{cmd_name}` 0.0")
        return

    module_name = COMMANDS[cmd_name]
    module = importlib.import_module(module_name)

    await module.run(bot, message, args)


bot.run(getToken("token.txt"))