import random

class Timer:
    def __init__(self, seuil, reponse):
        self.seuil = seuil - 1
        self.reponse = reponse
        self.compte = 0
    
    def reset(self):
        self.compte = 0

    async def verif(self, message):
        if self.compte == self.seuil:
            await message.channel.send(self.reponse)
            self.reset()
        else:
            self.compte+=1