import os
import random


class Layer:

    def __init__(self, layerPath: str) :
        self.layerPath = layerPath

    def getRandomDesignPath(self):
        designsFileNames = os.listdir(self.path)
        print(designsFileNames)
        return ""     