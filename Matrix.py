# mejorar con numpy:

class Matrix:
    """ Numerical matrix thought in the light of the distance matrix for UPGMA algorithm """
    
    def __init__(self, rows, cols):
        self.mat = []
        for i in range(rows):
            self.mat.append([])
            for _ in range(cols):
                self.mat[i].append(0.0)
    
    def reshape(self, rows, cols):
        newMat = []
        for i in range(rows):
            newMat.append([])
            for j in range(cols):
                newValue = self.get_value(i,j) if i < self.get_rows() and j < self.get_cols() else 0
                newMat[i].append( newValue )
        self.mat = newMat
    
    def __getitem__(self, pair:tuple):
        return self.get_value(pair[0], pair[1]) if len(pair) == 2 else None
    
    def get_rows(self):
        return len(self.mat)

    def get_row(self, i):
        return self.mat[i]
    
    def get_cols(self):
        return len(self.mat[0])
    
    def get_value(self, i, j):
        return self.mat[i][j] if i>j else self.mat[j][i]
        
    def set_value(self, i, j, value):
        if i>j:
            self.mat[i][j] = value
        else:
            self.mat[j][i] = value
    
    def print_mat(self):
        for r in self.mat:
            print(r)
        print()
    
    def min_dist_indexes(self):
        ''' Devuelve fila y columna del casillero con el menor valor
        (ignora los ceros de la diagonal principal)'''
        m = self.mat[1][0]
        res = (1,0)
        for i in range(1, self.get_rows()):
            for j in range(i):
                if self.mat[i][j] < m:
                    m = self.mat[i][j]
                    res = (i,j)
        return res
    
    def add_row(self):
        """ Adds empty row to the bottom of the matrix """
        self.mat.append([0]*self.get_cols())
        
    def add_col(self):
        """ Adds empty column to right end of the matrix """
        for r in range(self.get_rows()):
            self.mat[r].append(0)

    def extend(self):
        self.add_row()
        self.add_col()
    
    def remove_row(self, index):
        """" Removes indicated row, and numeration changes
        to adapt to the remaining rows """
        del self.mat[index]
        
    def remove_col(self, index):
        """" Removes indicated column, and numeration changes
        to adapt to the remaining columns """
        for r in range(self.get_rows()):
            del self.mat[r][index]

    def remove(self, pos):
        self.remove_row(pos)
        self.remove_col(pos)
    
    def copy(self):
        ''' Devuelve una copia de si mismo '''
        newMat = Matrix(self.get_rows(), self.get_cols())
        for i in range(self.get_rows()):
            for j in range(self.get_cols()):
                newMat.mat[i][j] = self.mat[i][j]
        return newMat