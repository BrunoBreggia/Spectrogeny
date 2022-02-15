from Bio import Entrez
from Bio import SeqIO
from BioSequence import DnaSeq

# example_ids = "6273291,6273290,6273289,KM262031"

def getFromGenbank(geneID:str) -> dict:
    """ Gene id can be more than one, all separated by commas, not spaces """
    Entrez.email = "A.N.Other@example.com"
    speciesID:dict = {}
    with Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id=geneID) as handle:
        for seq_record in SeqIO.parse(handle, "gb"):
            preDNA = ""
            for nuc in str(seq_record.seq):
                # Ignores ambiguous nucleotides
                preDNA += nuc if nuc in "ACGT" else ""
            name = seq_record.annotations["source"].replace(" ", "_")
            if preDNA: speciesID[ name ] = DnaSeq( preDNA )
    return speciesID

#insulinGenes = getFromGenbank("NC_006600.3") # Canis lupus familiaris
#print(len(insulinGenes))