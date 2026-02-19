import asyncio

async def run(bot, message, args):
    await message.channel.send("2sec...")

    process = await asyncio.create_subprocess_exec(
        "git", "pull",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()

    if process.returncode == 0:
        await message.channel.send(
            f"Pull réussi :\n{stdout.decode()} :D\n je recommande un +reboot btw^^'"
        )
    else:
        await message.channel.send(
            f"Erreur pendant le pull :\n{stderr.decode()}, jsp frr débrouille toi :3"
        )

#merci chat pour la gestion d'erreur