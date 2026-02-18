import subprocess

async def run(bot, message, args):
    await message.channel.send("Je re :3")
    await bot.db.close()
    await bot.close()
    
    subprocess.Popen('powershell.exe python main.py')