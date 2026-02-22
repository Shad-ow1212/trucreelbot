import importlib

from discord.ext import commands
import config
#fonction de test pour vérifier la perm admin en vue d'ajouter des commandes admin
async def run(bot, message, args):
    if not message.author.guild_permissions.administrator:
        await message.channel.send("t pa admin loser")
        return

    #args[0] commande
    #args[1:] prout
    if not args:
        await message.channel.send("Tu possède les perms admins :3")
        return

    cmd_name = args[0]
    args = args[1:]

    if cmd_name not in config.COMMANDS:
        await message.channel.send(f"Commande admin inconnue : `{cmd_name}` 0.0")

    module_name = config.ADMINCOMMANDS[cmd_name]
    module = importlib.import_module(module_name)

    await module.run(bot, message,args)