# -*- coding: utf-8 -*-
"""
CS150 Example with a dictionary and nested loops
"""

CODONS = {
"GCT" : "A", "GCC" : "A", "GCA" : "A", "GCG" : "A",
"CGT" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R", "AGA" : "R", "AGG" : "R",
"AAT" : "N", "AAC" : "N",
"GAT" : "D", "GAC" : "D",
"TGT" : "C", "TGC" : "C",
"CAA" : "Q", "CAG" : "Q",
"GAA" : "E", "GAG" : "E",
"GGT" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G",
"CAT" : "H", "CAC" : "H",
"ATT" : "I", "ATC" : "I", "ATA" : "I",
"TTA" : "L", "TTG" : "L", "CTT" : "L", "CTC" : "L", "CTA" : "L", "CTG" : "L",
"AAA" : "K", "AAG" : "K",
"ATG" : "M",
"TTT" : "F", "TTC" : "F",
"CCT" : "P", "CCC" : "P", "CCA" : "P", "CCG" : "P",
"TCT" : "S", "TCC" : "S", "TCA" : "S", "TCG" : "S", "AGT" : "S", "AGC" : "S",
"ACT" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T",
"TGG" : "W",
"TAT" : "Y", "TAC" : "Y",
"GTT" : "V", "GTC" : "V", "GTA" : "V", "GTG" : "V",
"TAA" : "X", "TGA" : "X", "TAG" : "X"
}

def translate(orfs):
    """
    Translate a list of ORFs into a list amino acid sequences
    
    Args:
        orfs: List of ORFs starting with start codon
    
    Returns:
        List of potential protein translations
    """
    proteins = []    
    for orf in orfs:
        protein = ""
        # An alternative loop could be range(0, len(orf) - len(orf)%3, 3), or
        # iterate by codon, i.e. range(len(orf) // 3) and then orf[i*3:i*3+3]
        for i in range(0, len(orf), 3):
            codon = orf[i:i+3]
            # Use get to ignore incomplete codons (at the end the sequence)
            amino = CODONS.get(codon, "")
            protein += amino
        proteins.append(protein)
    
    return proteins

# Should be 64 (4*4*4)
print(len(CODONS))

# Should be a single protein ['M']    
print(translate(["ATG"]))

# Should be 4 proteins ['M', 'MPCE', 'MA', 'MA']
print(translate(["ATG", "ATGCCATGTGAA", "ATGGCAT", "ATGGCATT"]))

#import tp1_genes
#print(translate(tp1_genes.gene_finder("AATGCCATGTGAA")))
