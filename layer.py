import os
import random


class Layer:

    def __init__(self, path: str) :
        self.path = path

    def getRandomDesignPath(self):
        designsFileNames = os.listdir(self.path)
        randomDesignFName = random.choice(designsFileNames)
        
        #Dar diferentes raridades?
        return os.path.join(self.path, randomDesignFName)  