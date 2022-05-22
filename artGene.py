import os

from layer import Layer 

class artGenerate:
    def __init__(self,designsPath: str):
        self.layers: List[Layer] = self.load_designs_layers(designsPath)
        pass

    # Ler a pasta de arquivos
    def load_designs_layers(self, designsPath: str):

        #Gerar arquivos e listar em ordem 
        subPaths = sorted(os.listdir(designsPath)) 
        #Debug   
        print(subPaths)

        layers = []

        #iterar entre cada subpath para gerar as camadas
        for subPath in subPaths:

            layerPaths = os.layerPath.join(designsPath, subPath)
            layer = Layer(layerPaths)
            layers.append(layer)
            print(layerPaths)
        return layers

    #Debug
    def genArt(self):
        print("artGenerate: Generating Art")

        designsPathSequence = []
        #Iterar pelas camadas 
        for layer in self.layers:
            designPath = layer.getRandomDesignPath()
            designsPathSequence.append(designPath)
        
        print(designsPathSequence)
           