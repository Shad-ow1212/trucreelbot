import subprocess

async def run(bot, message, args):
    #permet de save la db et de reboot... ok gg mais surtout ca permet de reload tout
    await message.channel.send("Je re :3")
    await bot.db.close()
    await bot.close()
    
    subprocess.Popen('powershell.exe python main.py')