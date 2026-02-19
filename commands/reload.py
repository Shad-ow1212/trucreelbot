import autocommands.salut as salut

async def run(bot, message, args):
    #permet de re-effectuer certaines fonctions init/reset de certains programmes, surtout ceux qui ont des ressources qui ne sont pas en dur dans le code.
    if not args:
        await message.channel.send("Euuh... j'ai besoin d'un truc a reload :3")
        return
    if args[0] == "csv":
        salut.init()
        await message.channel.send("Mouahaha, tous les CSVs sont rechargés ! :3")