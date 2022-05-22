from artGene import artGenerate

def geneArt():
    print("Generating Art")
    generate = artGenerate("./designs") 
    generate.geneArt()


if __name__== "__main__":
    geneArt()