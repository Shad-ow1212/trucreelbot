async def run(bot, message, args):
    temp = f"test :3 {args}" if args else f"test :3"
    await message.channel.send(temp)