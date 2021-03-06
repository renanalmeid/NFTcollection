import os
import random
from typing import List
from layer import Layer 
from PIL import Image



class artGenerate:


    def __init__(self,designsPath: str):

        self.layers: List[Layer] = self.loadDesignsLayers(designsPath)
        self.backgroundColor =(255,255,255)

        #Background Raro
        self.rareBackgroundColor = (255,211,0)
        self.rareBackgroundChance= 0.05

        #Diretorio de saida para avatar gerados
        self.outputPath: str = "./output"
        os.makedirs(self.outputPath, exist_ok=True)

    # Ler a pasta de arquivos
    def loadDesignsLayers(self, designsPath: str):

        #Gerar arquivos e listar em ordem 
        subPaths = sorted(os.listdir(designsPath)) 
        #Debug   
        #print(subPaths)

        #Cria variavel para armazenar
        # Rarityvariable  
        layers: List[Layer] = []

        #iterar entre cada subpath para gerar as camadas
        for subPath in subPaths:

            layerPaths = os.path.join(designsPath, subPath)
            layer = Layer(layerPaths)
            layers.append(layer)

        layers[2].rarity = 0.80
        layers[5].rarity = 0.15
        return layers

    #Iterar pelas camadas 
    def genDesignSequence(self):
        designsPathSequence = []
        
        for layer in self.layers:
            if layer.definirVariedade():
                designPath = layer.getRandomDesignPath()
                designsPathSequence.append(designPath)
        
        return designsPathSequence

    #Criar o a imagem a partir dos atributos randomly chosen, carregar a imagem
    def renderArtDesign (self, designsPathSequence: List[str]):

        if random.random() < self.rareBackgroundChance:
            bgColor = self.rareBackgroundColor
        else:
            bgColor = self.backgroundColor

        #Backgroundimage
        design = Image.new("RGBA", (1620, 2160),bgColor)

        for designPath in designsPathSequence:
            layerDesign = Image.open(designPath)

            #overlay as imagens e reescreve as antigas
            design = Image.alpha_composite(design, layerDesign)
        return design
    

    #salva a imagem em um caminho
    def saveDesign(self, design: Image.Image, j: int =0):
        designIndex = str(j).zfill(4)
        designName = f"art_{designIndex}.png"
        deisgnSavePath = os.path.join(self.outputPath, designName)
        design.save(deisgnSavePath)

    def geneArt(self, n: int = 1):
        #Debug
        #print("artGenerate: Generating Art")

        for j in range(n):
            designsPathSequence = self.genDesignSequence()
            design = self.renderArtDesign(designsPathSequence)

            #Debug
            #image.show()
            self.saveDesign(design, j)

        
