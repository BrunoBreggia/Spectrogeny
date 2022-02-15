from Bio import Phylo
import matplotlib.pyplot as plt
import ete3

class Phylogram:
    def __init__(self, newick_str:str):
        self.newcik = newick_str
        self.treeStyle = ete3.TreeStyle()

    def setNewick(self, newick_str:str):
        self.newcik = newick_str
    
    def show_tree(self, leaf_name=True, branch_length=True, circular=False):
        tree = ete3.Tree(self.newcik)
        self.treeStyle.show_leaf_name = leaf_name
        self.treeStyle.show_branch_length = branch_length
        if circular:
            self.treeStyle.mode = 'c'
            #ts.arc_start = 0 # 0 degrees = 3 o'clock
            #ts.arc_span = 180
        else:
            self.treeStyle.mode = 'r'
        tree.show(tree_style=self.treeStyle)
    
    def save_tree(self, fileName:str, leaf_name=True, branch_length=True, circular=False):
        """ FileName recommended be png """
        tree = ete3.Tree(self.newcik)
        self.treeStyle.show_leaf_name = leaf_name
        self.treeStyle.show_branch_length = branch_length
        if circular:
            self.treeStyle.mode = 'c'
            #ts.arc_start = 0 # 0 degrees = 3 o'clock
            #ts.arc_span = 180
        else:
            self.treeStyle.mode = 'r'
        tree.render(fileName, w=183, units="mm", tree_style=self.treeStyle)


## How to do it with Biopython:
#
#tree = Phylo.read('spectrogeny.dnd', 'newick')
#tree = Phylo.PhyloXML.Phylogeny.from_tree(tree)
#Phylo.draw(tree, do_show=False)
#plt.savefig('tree.png')
