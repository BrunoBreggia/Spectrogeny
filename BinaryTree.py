class BinaryTree:
    """ Estructura de datos donde cada nodo incluye dos ramificaciones """
    
    def __init__(self, val, dist=0, left=None, right=None):
        ''' Si es nodo interno, val= -1 '''
        self.value = val
        self.distance = dist
        self.left = left
        self.right = right
        self.newick = ""
    
    def __repr__(self):
        """ Devuelve arbol en formato string """
        return self.__recursive_print(0, 'root')
        
    def __recursive_print(self, level, side) ->str:
        ''' Metodo de uso interno, para mostrar por pantalla
        el contenido del arbol de manera recursiva'''
        tabs = ""
        for _ in range(level):
            tabs += '\t'
        if self.value >= 0:
            #print(tabs, side, "- value:", self.value)
            tabs += f" {side} - value: '{self.value}'\n"
        else:
            #print(tabs, side, "- Dist.:", self.distance)
            tabs += f" {side} -Dist.: {self.distance}\n"
            if self.left is not None:
                tabs += self.left.__recursive_print(level+1, 'Left')
            if self.right is not None:
                tabs += self.right.__recursive_print(level+1, 'Right')
        return tabs
    
    def get_cluster(self):
        ''' Devuelve el valor de los nodos hojas '''
        res = []
        if self.value >= 0:
            res.append(self.value)
        else:
            if self.left is not None:
                res.extend(self.left.get_cluster())
            if self.right is not None:
                res.extend(self.right.get_cluster())
        return res

    def save_to_file(self, fileName:str, distances=True, SpeciesID:dict=None):
        """ Saves tree structure in file with Newick notation. SpeciesID is optional 
        dictionary with species_name:matrix_ID_number to save file with original species names """
        self.parse_Newick(distances=distances, SpeciesID=SpeciesID)
        with open(fileName, 'w') as output:
            output.write(self.newick)
        
    def parse_Newick(self, distances=True, SpeciesID:dict=None):
        self.newick = self._recursive_Newick(distances=distances, dist=0)
        if SpeciesID is not None:
            for name,ID in SpeciesID.items():
                self.newick = self.newick.replace(f"'{str(ID)}'", name)
        return self.newick
    
    def _recursive_Newick(self, distances, dist):
        newick = ""
        if self.left is None and self.right is None:
            if distances:
                return f"'{str(self.value)}':{str(dist)}"
            else:
                return f"'{str(self.value)}'"
        newick += "("
        if self.left is not None:
            newick += self.left._recursive_Newick(distances, self.distance)
            if newick[-1]==";": newick=newick[:-1]
        if self.right != None:
            if self.left is not None:
                newick += ","
            newick += self.right._recursive_Newick(distances, self.distance)
            if newick[-1]==";": newick=newick[:-1]
        if distances:
            newick += f"):{dist};"
        else:
            newick += ");"
        return newick
        
