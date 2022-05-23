import os
import random


class Layer:

    def __init__(self, path: str) :
        self.path = path
        #gerar raridade
        self.rarity: float = 1.0

    def getRandomDesignPath(self):
        designsFileNames = os.listdir(self.path)
        randomDesignFName = random.choice(designsFileNames)
        
        #Dar diferentes raridades?
        return os.path.join(self.path, randomDesignFName)  
    
    def definirVariedade(self) -> bool:
        return random.random() < self.rarity