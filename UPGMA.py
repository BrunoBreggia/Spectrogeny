from Matrix import Matrix
from BinaryTree import BinaryTree

## Future improvement: create superclass Algorithm for other clustering algorithms

class UPGMA:
    """ Aplica el algoritmo de agrupamiento UPGMA a una matriz de 
    distancias, devuelve arbol binario """

    def __init__(self):
        self.distances:Matrix = Matrix(1,1)
        self.nodes:list = []
    
    def __call__(self, DistMat:Matrix):
        self.distances = DistMat
        self.nodes = []
        for i in range(self.distances.get_rows()):
            self.nodes.append( BinaryTree(i) )
        return self.applyUPGMA()
        #return self.apply()
    
    def applyUPGMA(self):
    #def apply(self) -> BinaryTree:
        while len(self.nodes) > 1:
            # Get indexes of minimum distance
            i, j = self.distances.min_dist_indexes()
            newNode = BinaryTree(-1, self.distances[i,j]/2, self.nodes[i], self.nodes[j])
            self.nodes.append(newNode)
            self.distances.extend()
            last_index = len(self.nodes)-1
            for z in range(last_index):
                self.distances.set_value(last_index, z, (self.distances[i,z] + self.distances[j,z]) /2)
            self.distances.remove(i)
            self.distances.remove(j)
            self.nodes.pop(i)
            self.nodes.pop(j)
        return self.nodes[0]

