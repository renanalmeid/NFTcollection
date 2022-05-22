from artGene import artGenerate

def geneArt():
    print("Generating Art")
    generate = artGenerate("./designs") 
    generate.genArt()


if __name__== "__main__":
    geneArt()