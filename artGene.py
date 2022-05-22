import os 

class artGenerate:
    def __init__(self,designs_path: str):
        self.layers = self.load_designs_layers(designs_path)
        pass

    def load_designs_layers(self, designs_path: str):
        subPaths = os.listdir(designs_path)
        print(subPaths)
        layers = []
        return layers

    def genArt(self):
        print("artGenerate: Generating Art")