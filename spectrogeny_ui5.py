# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectrogeny.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from main import System
from TreeDrawing import Phylogram
from databaseData import getFromGenbank

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1103, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.HacerFilogenia = QtWidgets.QPushButton(self.centralwidget)
        self.HacerFilogenia.setGeometry(QtCore.QRect(60, 520, 261, 41))
        self.HacerFilogenia.setObjectName("HacerFilogenia")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 249, 121, 16))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 280, 256, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(380, 10, 701, 501))
        self.graphicsView.setLineWidth(1)
        self.graphicsView.setObjectName("graphicsView")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 200, 261, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 170, 211, 21))
        self.label_2.setObjectName("label_2")
        self.toggleTreeDisplay = QtWidgets.QPushButton(self.centralwidget)
        self.toggleTreeDisplay.setGeometry(QtCore.QRect(970, 520, 111, 41))
        self.toggleTreeDisplay.setObjectName("toggleTreeDisplay")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 520, 131, 16))
        self.label_4.setObjectName("label_4")
        self.newickLabel = QtWidgets.QLabel(self.centralwidget)
        self.newickLabel.setGeometry(QtCore.QRect(390, 540, 561, 31))
        self.newickLabel.setObjectName("newickLabel")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(250, 170, 75, 23))
        self.addButton.setObjectName("addButton")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(40, 10, 291, 131))
        self.graphicsView_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView_2.setLineWidth(0)
        self.graphicsView_2.setInteractive(False)
        self.graphicsView_2.setObjectName("graphicsView_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1103, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Phylogeny = QtWidgets.QAction(MainWindow)
        self.actionNew_Phylogeny.setObjectName("actionNew_Phylogeny")
        self.actionSave_Genomes_in_File = QtWidgets.QAction(MainWindow)
        self.actionSave_Genomes_in_File.setObjectName("actionSave_Genomes_in_File")
        self.actionSave_Newick = QtWidgets.QAction(MainWindow)
        self.actionSave_Newick.setObjectName("actionSave_Newick")
        self.actionSave_Tree_Image = QtWidgets.QAction(MainWindow)
        self.actionSave_Tree_Image.setObjectName("actionSave_Tree_Image")
        self.actionOpen_Newick_Tree = QtWidgets.QAction(MainWindow)
        self.actionOpen_Newick_Tree.setObjectName("actionOpen_Newick_Tree")
        self.actionImport_File = QtWidgets.QAction(MainWindow)
        self.actionImport_File.setObjectName("actionImport_File")
        self.menuFile.addAction(self.actionNew_Phylogeny)
        self.menuFile.addAction(self.actionSave_Genomes_in_File)
        self.menuFile.addAction(self.actionSave_Newick)
        self.menuFile.addAction(self.actionSave_Tree_Image)
        self.menuFile.addAction(self.actionOpen_Newick_Tree)
        self.menuFile.addAction(self.actionImport_File)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ## Added
        pix = QtGui.QPixmap("SpectrogenyLogo-shrinked.png")
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)
        self.graphicsView_2.setScene(scene)
        self.system = System()
        self.img = None
        self.newickNotation = None
        self.HacerFilogenia.setDisabled(True)
        
        self.actionNew_Phylogeny.triggered.connect(self.cleanContent)
        self.actionSave_Genomes_in_File.triggered.connect(self.genomeToFile)
        self.actionSave_Newick.triggered.connect(self.saveNewickFile)
        self.actionSave_Tree_Image.triggered.connect(self.saveImageFile)
        self.actionOpen_Newick_Tree.triggered.connect(self.openNewick)
        self.actionImport_File.triggered.connect(self.getFile)

        self.HacerFilogenia.clicked.connect(self.hacerFilogenia)
        self.addButton.clicked.connect(self.addGene)

        self.display = "r"
        self.toggleTreeDisplay.clicked.connect(self.toggleDisplay)
        self.toggleTreeDisplay.setDisabled(True)

    def cleanContent(self):
        self.system.clear()
        self.textBrowser.clear()
        if self.graphicsView.scene() is not None:
            self.graphicsView.scene().clear()
            self.graphicsView.viewport().update()
        self.toggleTreeDisplay.setDisabled(True)
        self.newickLabel.clear()
        self.display = "r"
        self.toggleTreeDisplay.setText("Arbol Circular")

    def addGene(self):
        geneID = self.textEdit.toPlainText()
        if geneID != "":
            geneID = self.textEdit.toPlainText()
            newGenes:dict = getFromGenbank(geneID)
            self.system.sequences = {**self.system.sequences, **newGenes}
            self.textEdit.setPlainText("")
            self.showSpecies()

    def genomeToFile(self):
        self.system.saveSequencesToFile()
    
    def openNewick(self):
        self.cleanContent()
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(caption="Elije un archivo con formato newick (.dnd o .txt)")
        with open(fname,'r') as f:
            self.newickNotation = f.read()
        self.img = Phylogram(self.newickNotation)
        self.newickLabel.setText(self.newickNotation)
        self.showTrees()

    def getFile(self):
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(caption="Elije un archivo con genomas")
        self.system.parseFasta(fname).keys()
        self.showSpecies()
        #self.HacerFilogenia.setDisabled(False)

    def showSpecies(self):
        self.textBrowser.clear()
        i:int = 0
        for sp in self.system.sequences.keys():
            self.textBrowser.append(str(i)+" "+sp)
            i += 1
        if i>1:
            self.HacerFilogenia.setDisabled(False)  

    def saveImageFile(self):
        if self.img is None: return
        fname, _ = QtWidgets.QFileDialog.getSaveFileName(caption="Escoje donde guardar imagen")
        circular = True if self.display == "c" else False
        print(fname)
        self.img.save_tree(fname, circular=circular)

    def saveNewickFile(self):
        if self.newickNotation is None: return
        if self.img is None: pass
        fname, _ = QtWidgets.QFileDialog.getSaveFileName(caption="Escoje donde guardar arbol")
        if fname:
            with open(fname, 'w') as f:
                f.write(self.newickNotation)

    def hacerFilogenia(self):
        self.HacerFilogenia.setDisabled(True)
        # Calculation
        self.system.calculateVectors(saveToFile=True)
        self.system.calculateDistanceMatrix(saveToFile=True)
        self.tree = self.system.calculatePhylogeny(saveToFile=True)
        self.system.saveSequencesToFile()
        self.newickLabel.setText(self.tree.parse_Newick(distances=False))
        self.newickNotation = self.tree.parse_Newick(distances=True,SpeciesID=self.system.SpeciesID)
        self.img = self.system.visualOutput()
        self.showTrees()
    
    def showTrees(self):
        # Visual output
        self.img.save_tree("HorizontalTree.png", circular=False)
        self.img.save_tree("CircularTree.png", circular=True)
        # Display tree images
        pix = QtGui.QPixmap("HorizontalTree.png")
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)
        self.graphicsView.setScene(scene)
        self.toggleTreeDisplay.setDisabled(False)

    def toggleDisplay(self):
        self.display = "c" if self.display == "r" else "r"
        if self.display == "r":
            pix = QtGui.QPixmap("HorizontalTree.png")
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.graphicsView.setScene(scene)
            self.toggleTreeDisplay.setText("Arbol Circular")
        elif self.display == "c":
            pix = QtGui.QPixmap("CircularTree.png")
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene()
            scene.addItem(item)
            self.graphicsView.setScene(scene)
            self.toggleTreeDisplay.setText("Arbol Recto")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spectrogeny"))
        MainWindow.setWindowIcon(QtGui.QIcon('infinity.png'))
        self.HacerFilogenia.setText(_translate("MainWindow", "Filogenia"))
        self.label.setText(_translate("MainWindow", "Especies listadas"))
        self.label_2.setText(_translate("MainWindow", "Introducir especie"))
        self.toggleTreeDisplay.setText(_translate("MainWindow", "Arbol Circular"))
        self.label_4.setText(_translate("MainWindow", "Notacion de NEWICK:"))
        self.newickLabel.setText(_translate("MainWindow", " "))
        self.addButton.setText(_translate("MainWindow", "Agregar"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew_Phylogeny.setText(_translate("MainWindow", "New Phylogeny"))
        self.actionNew_Phylogeny.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave_Genomes_in_File.setText(_translate("MainWindow", "Save Genomes in File"))
        self.actionSave_Genomes_in_File.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionSave_Newick.setText(_translate("MainWindow", "Save Newick"))
        self.actionSave_Newick.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_Tree_Image.setText(_translate("MainWindow", "Save Tree Image"))
        self.actionSave_Tree_Image.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionOpen_Newick_Tree.setText(_translate("MainWindow", "Open Newick Tree"))
        self.actionOpen_Newick_Tree.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionImport_File.setText(_translate("MainWindow", "Import File"))
        self.actionImport_File.setShortcut(_translate("MainWindow", "Ctrl+I"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

