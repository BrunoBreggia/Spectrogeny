from BioSequence import DnaSeq
import numpy as np
from Matrix import Matrix
from BinaryTree import BinaryTree
from CFPPSmethod import CFPPS
from UPGMA import UPGMA
from TreeDrawing import Phylogram

###################################################
## Spectrogeny
###################################################

class System():
    def __init__(self):
        self.sequences:dict = {}
        self.vectors:dict = {}
        self.SpeciesID:dict = {}
        self.Dist:Matrix = Matrix(1,1)
        self.tree:BinaryTree = BinaryTree(0)
        self.graph:Phylogram = Phylogram("")
        pass

    def addSpecies(self, name:str, dna:DnaSeq):
        self.sequences[name] = dna
    
    def clear(self):
        self.sequences = {}
        self.vectors = {}
        self.SpeciesID = {}
        self.Dist = Matrix(1,1)
        self.graph = Phylogram("")

    def parseFasta(self, fname:str) -> dict:
        with open(fname, 'r') as inFile:
            species = inFile.readline()
            while len(species) > 0 and species[0] == '>':
                name = species[1:-1]
                self.sequences[name] = ""
                line = inFile.readline()
                while len(line)>0 and line[0] != '>':
                    self.sequences[name] += line[:-1]
                    line = inFile.readline()
                species = line

        # Transform the DNA strings into DNA objects
        for k, v in self.sequences.items():
            if type(v) is not DnaSeq:
                # Ignores ambiguous nucleotides
                self.sequences[k] = DnaSeq("".join([nuc if nuc in "ACGTacgt" else "" for nuc in str(v)]))
        return self.sequences

    def calculateVectors(self, saveToFile=False) -> dict:
        # Dictionary for the 28-dim vectors
        self.vectors = {}
        for species, dna in self.sequences.items():
            self.vectors[species] = CFPPS(dna)
        if saveToFile: self._saveToFile(self.vectors)
        return self.vectors

    def calculateDistanceMatrix(self, saveToFile=False) -> Matrix:
        """ Uso distancia Euclidea en espacio 28-dimensional """
        self.Dist = Matrix(len(self.vectors), len(self.vectors))
        self.SpeciesID = {}
        i:int = 0
        for species in self.vectors.keys():
            self.SpeciesID[species] = i
            i += 1
        for sp1 in self.SpeciesID.keys():
            for sp2 in self.SpeciesID.keys():
                difference = self.vectors[sp1] - self.vectors[sp2]
                self.Dist.set_value(self.SpeciesID[sp1], self.SpeciesID[sp2], np.linalg.norm(difference, ord=2))
        if saveToFile: self._saveToFile(self.Dist)
        return self.Dist

    def calculatePhylogeny(self, algorithm=UPGMA(), saveToFile=False) -> BinaryTree:
        """ Obtencion de filogenia con algoritmo UPGMA """
        self.tree:BinaryTree = algorithm(DistMat=self.Dist)
        if saveToFile: self._saveToFile(self.tree)
        return self.tree

    def visualOutput(self) -> Phylogram:
        self.graph.setNewick(self.tree.parse_Newick(SpeciesID=self.SpeciesID))
        return self.graph

    def saveSequencesToFile(self):
        with open("sequences.fasta",'w') as output:
            for sp,dna in self.sequences.items():
                output.write(f">{sp}\n{dna}\n")

    def _saveToFile(self, TAD):
        if type(TAD) == dict:
            with open('Vectores.txt','w') as f:
                for k,v in TAD.items():
                    f.write(f"{k}: {v}\n")
        elif type(TAD) == Matrix:
            with open('MtrizDistancia.txt','w') as f:
                f.write('Matriz de Distancias,')
                f.write(",".join(self.SpeciesID.keys()))
                f.write('\n')
                for sp,num in self.SpeciesID.items():
                    f.write(f"{sp}: {TAD.get_row(num)}\n")
        elif type(TAD) == BinaryTree:
            with open('Arbol.txt','w') as f:
                tree_str = str(TAD)
                for sp,num in self.SpeciesID.items():
                    tree_str = tree_str.replace(f"'{num}'", sp)
                f.write(tree_str)


if __name__ == '__main__':
    # Reading Cytochrome C genes from file
    sequences = {}
    with open('taller_secuencias_renombradas.fasta') as file:
        species = file.readline()
        while len(species) > 0 and species[0] == '>':
            name = species[1:-1]
            sequences[name] = ""
            line = file.readline()
            while len(line)>0 and line[0] != '>':
                sequences[name] += line[:-1]
                line = file.readline()
            species = line

    # Transform the DNA strings into DNA objects
    for k, v in sequences.items():
        sequences[k] = DnaSeq(v)

    # Dictionary for the 28-dim vectors
    vectors = {}
    for species, dna in sequences.items():
        vectors[species] = CFPPS(dna)

    # Llenado de la matriz de distancias
    Dist = Matrix(len(vectors), len(vectors))
    SpeciesID = {}
    i=0
    for species in vectors.keys():
        SpeciesID[species] = i
        i += 1

    for sp1 in SpeciesID.keys():
        for sp2 in SpeciesID.keys():
            difference = vectors[sp1] - vectors[sp2]
            Dist.set_value(SpeciesID[sp1], SpeciesID[sp2], np.linalg.norm(difference, ord=2)) # Uso Distancia Euclidea en 28 dimensiones

    print(SpeciesID)
    #Dist.print_mat()

    # Obtencion de filogenia con algoritmo UPGMA
    algorithm = UPGMA()
    phylogeny:BinaryTree = algorithm(Dist)
    print(phylogeny)

    # Archivo con arbol en formato Newick
    fileName = "spectrogeny.dnd"
    phylogeny.save_to_file(fileName, SpeciesID=SpeciesID)

    # Salida grafica (guardo png)
    img = Phylogram(phylogeny.parse_Newick(SpeciesID=SpeciesID))
    img.save_tree("Horizontal_Phylogram.png")
    img.save_tree("Circular_Phylogram.png", circular=True)
    img.show_tree()
    img.show_tree(circular=True)
