from utils.embeds import make_embed

async def run(bot, message, args):
    #amusez vous avec les inlines mdr
    await message.channel.send(embed=make_embed(
        title="Voyons voir... :3",
        description="Effectuons un test hehe x3",
        fields=[["Bonjour !"],
                [f"Tu es {message.author}"],
                ["Je crois que tout marche :3"],
                ["Voici tes args:", None if not args else " ".join(args)]],
        footer="Ceci est un footer"
    ))