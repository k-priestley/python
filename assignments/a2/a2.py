def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    if len(dna1) > len(dna2):
        return True    
    
def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    num_nucl = 0
    
    for char in dna:
        if char in nucleotide:
            num_nucl = num_nucl + 1

    return num_nucl

    

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """


    if dna2 in dna1:
        return True
    else:
        return False


def get_complement(nucl):

    '''
    (str) -> str

    Return the nucleotide's complement
    
    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'
    '''
    
    if nucl == 'A':
        return 'T'
    elif nucl == 'G':
        return 'C'

def get_complementary_sequence(sequence):

    '''
    (str) -> str

    Return complementary DNA sequence to given DNA sequence

    >>> get_complementary_sequence('AT')
        'TA'
    >>> get_complementary_sequence('GC')
        'CG'
    '''

    DNA = ''
    
    for char in sequence:
        if char in 'A':
            DNA = DNA + 'T'
        if char in 'T':
            DNA = DNA + 'A'
        if char in 'G':
            DNA = DNA + 'C'
        if char in 'C':
            DNA = DNA + 'G'
            
    return DNA
  


        
