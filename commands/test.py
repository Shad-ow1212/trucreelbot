from utils.embeds import make_embed

async def run(bot, message, args):
    #amusez vous avec les inlines mdr
    await message.channel.send(embed=make_embed(
        title="Voyons voir... :3",
        description="Effectuons un test hehe x3",
        fields=[["Alors... premier field", "En gros la on a un field avec un inline activé", True],
                ["Et la ?", "La ya pas d'inline ! ", True],
                ["Et la 2 ?", "La ya pas d'inline 2 ! ", True],
                ["Et la ?", "La ya pas d'inline ! ", False]]
    ))