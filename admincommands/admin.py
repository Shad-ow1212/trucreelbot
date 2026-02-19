from discord.ext import commands
#fonction de test pour vérifier la perm admin en vue d'ajouter des commandes admin
async def run(bot, message, args):
    if not message.author.guild_permissions.administrator:
        await message.channel.send("t pa admin loser")
        return

    await message.channel.send("c bon t admin")