import discord

@commands.has_permissions(administrator=True)
async def run(bot, message, args):
    await message.channel.send("c bon t admin")

@commands.has_permissions(administrator=False)
async def run(bot, message, args):
    await message.channel.send("t pa admin loser")