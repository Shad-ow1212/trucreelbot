import subprocess

async def run(bot, message, args):
    #permet de pull le code du github... je suis pas super sur il faudrait VRAIMENT mettre un système de vérification je pense...
    await message.channel.send("2sec...")

    try:
        result = subprocess.run(
            ["git", "pull"],
            capture_output=True,
            text=True,
            check=True
        )

        await message.channel.send(f"Pull réussi :\n{result.stdout} :D")

    except subprocess.CalledProcessError as e:
        await message.channel.send(
            f"Erreur pendant le pull :\n{e.stderr}... débrouille toi :3"
        )

#merci chat pour la gestion d'erreur