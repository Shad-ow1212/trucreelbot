from discord.ext import commands
#fonction de test pour vérifier la perm admin en vue d'ajouter des commandes admin
@commands.has_permissions(administrator=True)
async def run(bot, message, args):
    await message.channel.send("c bon t admin")
