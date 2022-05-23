

from artGene import artGenerate

def geneArt():
    generate = artGenerate("./designs") 
    generate.geneArt(1000)


if __name__== "__main__":
    geneArt()