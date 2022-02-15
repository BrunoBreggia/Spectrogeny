from structures import *

# Seq types:
def PROTEIN():
    return 'protein'
def RNA():
    return 'rna'
def DNA():
    return 'dna'

class BioSequence:
    """ Class for Biological sequences: DNA, RNA or protein """

    def __init__(self, seq, typeFunc):
        self.seq = seq.upper()
        self.type = typeFunc()
        assert self.validate(), f"Invalid {self.type} sequence!"
        return None
    
    def  __len__(self):
        return len(self.seq)

    def __getitem__(self, n):
        return self.seq[n]

    def __getslice__(self, i, j):
        return self.seq[i:j]

    def __str__(self):
        return self.seq
    
    def get_type(self):
        return self.type
    
    def show_info_seq(self):
        print("Sequence: " + self.seq + " biotype: " + self.type)
        return None
    
    def alphabet(self):
        if self.type == DNA():
            return 'ACGT'
        elif self.type == RNA():
            return 'ACUG'
        elif self.type == PROTEIN():
            return 'ACDEFGHIKLMNPQRSTVWY'
        return None

    def validate(self):
        alpha = self.alphabet()
        res = True
        i = 0
        while i < len(self.seq) and res:
            if self.seq[i] in alpha:
                i += 1 
            else:
                res = False 
        return res


class DnaSeq(BioSequence):
    """ Represents DNA strand """

    def __init__(self, seq):
        super().__init__(seq, DNA)
        return None

    def transcription(self):
        return RnaSeq( self.seq.replace('T', 'U') )
    
    def reverse_complement(self):
        comp = ''
        for nuc in self.seq:
            comp = DNA_complement[nuc] + comp
        return DnaSeq(comp)


class RnaSeq(BioSequence):
    """ Represents RNA strand """

    def __init__(self, seq):
        super().__init__(seq, RNA)
        return None

    def translate(self, iniPos=0):
        seq_aa = ""
        for pos in range(iniPos, len(self.seq)-2,3):
            cod = self.seq[pos:pos+3]
            seq_aa += GeneticCode[cod]
        return ProtSeq(seq_aa)


class ProtSeq(BioSequence):
    """ Represents amino acid strand (protein) """

    def __init__(self, seq):
        super().__init__(seq, PROTEIN)
        return None

