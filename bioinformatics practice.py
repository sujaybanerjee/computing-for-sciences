# load package
import Bio

#methods and attributes
dir(Bio)


#working with sequences

from Bio.Seq import Seq


#create a simple sequence
seq1 = Seq('ATGATCTCGTAA')



#checking for the type of sequence
#seq1.alphabet


#create a generic DNA
from Bio.Alphabet import generic_dna, generic_rna, generic_protein

# create our DNA

dna = Seq('ATGATCTCGTAA', generic_dna)


