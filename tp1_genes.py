"""
CSCI150 Test Project 1

Name: Sujay Banerjee
Section: A
"""

codon_length = 3


def is_stop(codon):
    """Determines if codon is a stop codon or not

        Args:
            codon: codon as a string
            
        Returns:
            True or False depending on if codon is a stop codon
    """
    return codon == "TGA" or codon == "TAG" or codon == "TAA"


def orf_sequence(string):
    """Extracts the open reading frame from DNA string

        Args:
            string: string of DNA
            
        Returns:
            ORF from DNA string
    """
    orf = ''
    for i in range(0, len(string), codon_length): 
        if is_stop(string[i:i+codon_length]) == True:
            return orf
        else:
            orf += string[i:i+codon_length]
    return orf
    

def find_orfs(string):
    """List of ORFs in a DNA string assuming a single reading frame

        Args:
            string: string of DNA
            
        Returns:
            list of ORFs
    """
    orfs = []
    i = 0
    while i <= len(string):
        if string[i:i+codon_length] == "ATG":
            orfs.append(orf_sequence(string[i:]))
            i += len(orf_sequence(string[i:]))
        else:
            i += codon_length            
    return orfs
            
    
    
def reverse_complement(string):
    """Reverses the order of and finds complementing bases in the original DNA string

        Args:
            string: string of DNA
            
        Returns:
            Reverse complement string
    """
    comp = ''
    for base in string[::-1]:
        if base == "A":
            comp += "T"
        elif base == "T":
            comp += "A"
        elif base == "G":
            comp += "C"
        elif base == "C":
            comp += "G"
    return comp


def gene_finder(string):
    """Identifies all ORFs for all three valid reading frames on both strands.

        Args:
            string: string of DNA
            
        Returns:
            A list of all ORFs for both strands
    """
    allorf = []
    comp = reverse_complement(string)
    allorf.extend(find_orfs(string))
    allorf.extend(find_orfs(string[1:]))
    allorf.extend(find_orfs(string[2:]))
    allorf.extend(find_orfs(comp))
    allorf.extend(find_orfs(comp[1:]))
    allorf.extend(find_orfs(comp[2:]))
    return allorf


    
def read_fasta(filename):
    """
    Read a single DNA sequence from a FASTA-formatted file
    
    For example, to read the sequence from a file named "X73525.fasta.txt"
    >>> sequence = read_fasta("X73525.fasta.txt")
    
    Args:
        filename: Filename as a string
        
    Returns: Upper case DNA sequence as a string
    """
    with open(filename, "r") as file:
        # Read (and ignore) header line
        header = file.readline()
        # Read sequence lines
        sequence = ""
        for line in file:
            sequence += line.strip()
        return sequence.upper()


def filter_orfs(orfs, min_length):
    """
    Filter ORFs to have a minimum length
    
    Args:
        orfs: List of candidate ORF sequences
        min_length: Minimum length for an ORF
    
    Returns:
        A new list containing only ORF strings longer than min_length bases
    """
    filtered_orfs = []
    for orf in orfs:
        if len(orf) > min_length:
            filtered_orfs.append(orf)
    return filtered_orfs


def write_fasta(filename, orfs):
    """
    Write list of ORFs to a FASTA formatted text file.
    
    For example, to save a list of orfs assigned to the variable my_orfs to a
    file named "genes.txt"
    >>> write_fasta("genes.txt", my_orfs)
    
    Args:
        filename: Filename as a string. Note that any existing file with this name
            will be overwritten.
        orfs: List of ORF sequences to write to the file
    """
    with open(filename, "w") as file:
        for i in range(len(orfs)):
            # A FASTA entry is a header line that begins with a '>', and then the sequence on the next line(s)
            print(">seq" + str(i), file=file)
            print(orfs[i], file=file)

           
if __name__ == "__main__":
    # If you want perform the steps for creating genes.txt as part of your
    # program, implement that code here. It will run every time you click the
    # green arrow, but will be ignored by Gradescope.
    pass
   
