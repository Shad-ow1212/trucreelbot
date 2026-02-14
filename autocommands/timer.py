import random
from utils.embeds import make_embed

class Timer:
    def __init__(self, seuil, reponse):
        self.seuil = seuil - 1
        self.reponse = reponse
        self.compte = 0

    def __repr__(self):
        return f"Seuil : {self.seuil+1}, reponse : {self.reponse}"
    
    def reset(self):
        self.compte = 0

    async def verif(self, message):
        if self.compte == self.seuil:
            await message.channel.send(embed=make_embed(title=self.reponse))
            self.reset()
        else:
            self.compte+=1