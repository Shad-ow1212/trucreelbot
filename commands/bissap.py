from utils.embeds import make_embed
import discord

#normalement, ya un autre moyen d'envoyer des gifs, mais pour l'instant j'utilise les embeds, désolé ://
async def run(bot, message, args):
    path = "data/images/bissap.gif"
    filename = "bissap.gif"
    
    embed = make_embed(images=[f"attachment://{filename}"])

    await message.channel.send(embed=embed, file=discord.File(path, filename=filename))
