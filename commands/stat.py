import discord

async def run(bot, message, args):
    #permet de lire des infos de la db... merci chat
    guild_id = message.guild.id
    
    if not args:
        target = message.author
    else:
        try:
            target = message.mentions[0] if message.mentions else await message.guild.fetch_member(int(args[0]))
        except Exception:
            await message.channel.send("Impossible de trouver cet utilisateur >.<")
            return

    count = await bot.db.get_message_count(guild_id, target.id)

    if count is not None:
        await message.channel.send(f"{target.display_name} a envoyé **{count} messages** sur ce serveur :D")
    else:
        await message.channel.send(f"Aucun message enregistré pour {target.display_name} :/")