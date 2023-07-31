import re

def read_dna(dna_file):
    dnaPair = []
    with open(dna_file) as f:
        for line in f:
            if m := re.search("(.*) <-> (.*)", line):
                pair1 = m.group(1)
                pair2 = m.group(2)
                # if not pair1:
                #     dnaPair.append((pair1, pair2))
                # elif not pair2:
                #     dnaPair.append((pair1, pair2))
                dnaPair.append((pair1, pair2))
    return dnaPair
    """
    Read a DNA string from a file.
    the file contains data in the following format:
    A <-> T
    G <-> C
    G <-> C
    C <-> G
    G <-> C
    T <-> A
    Output a list of touples:
    [
        ('A', 'T'),
        ('G', 'C'),
        ('G', 'C'),
        ('C', 'G'),
        ('G', 'C'),
        ('T', 'A'),
    ]
    Where either (or both) elements in the string might be missing:
    <-> T
    G <->
    G <-> C
    <->
    <-> C
    T <-> A
    Output:
    [
        ('', 'T'),
        ('G', ''),
        ('G', 'C'),
        ('', ''),
        ('', 'C'),
        ('T', 'A'),
    ]
    """


def is_rna(dna):
    total = 0
    # DNAPairs = ['A','T','G','C']
    # RNAPairs = ['A','U','G', 'C']
    DNAPairs = []
    RNAPairs = []
    for (pair1, pair2) in dna:
            if not pair1 or not pair2:
                total += 1
            elif not pair1 and not pair2:
                total += 0
            else:
                total += 2
            if pair1 == 'T':
                DNAPairs.append(pair1)
                DNAPairs.append(pair2)
            elif pair1 == 'U':
                RNAPairs.append(pair1)
                RNAPairs.append(pair2)
            elif pair2 == 'T':
                DNAPairs.append(pair2)
                DNAPairs.append(pair1)
            elif pair2 == 'U':
                RNAPairs.append(pair2)
                RNAPairs.append(pair1)
            else:
                DNAPairs.append(pair1)
                RNAPairs.append(pair1)
                DNAPairs.append(pair2)
                RNAPairs.append(pair2)
    DNAPairs = list(filter(None, DNAPairs))
    RNAPairs = list(filter(None, RNAPairs))

    # print(len(DNAPairs)/total)
    if (len(DNAPairs)/total > 0.9):
        return "DNA"
    elif (len(RNAPairs)/total > 0.9):
        return "RNA"
    else:
        return "Invalid"
    """
    Given DNA in the aforementioned format,
    return the string "DNA" if the data is DNA,
    return the string "RNA" if the data is RNA,
    return the string "Invalid" if the data is neither DNA nor RNA.
    DNA consists of the following bases:
    Adenine  ('A'),
    Thymine  ('T'),
    Guanine  ('G'),
    Cytosine ('C'),
    RNA consists of the following bases:
    Adenine  ('A'),
    Uracil   ('U'),
    Guanine  ('G'),
    Cytosine ('C'),
    The data is DNA if at least 90% of the bases are one of the DNA bases.
    The data is RNA if at least 90% of the bases are one of the RNA bases.
    The data is invalid if more than 10% of the bases are not one of the DNA or RNA bases.
    Empty bases should be ignored.
    """
    pass


def clean_dna(dna):
    resultDNA = []
    if is_rna(dna) == 'DNA':
        is_DNA = True
    else:
        is_DNA = False

    for (pair1, pair2) in dna:
        if not pair1:
            if pair2 == 'G':
                pair1 = 'C'
            if pair2 == 'C':
                pair1 = 'G'
            if pair2 == 'T':
                pair1 == 'A'
            if pair2 == 'U':
                pair1 == 'A'
            if pair2 == 'A':
                if is_DNA:
                    pair1 = 'T'
                else:
                    pair1 = 'U'
        if not pair2:
            if pair1 == 'G':
                pair2 = 'C'
            if pair1 == 'C':
                pair2 = 'G'
            if pair1 == 'T':
                pair2 == 'A'
            if pair1 == 'U':
                pair2 == 'A'
            if pair1 == 'A':
                if is_DNA:
                    pair2 = 'T'
                else:
                    pair2 = 'U' 
        resultDNA.append((pair1,pair2))
    return resultDNA
    
    """
    Given DNA in the aforementioned format,
    If the pair is incomplete, ('A', '') or ('', 'G'), ect
    Fill in the missing base with the match base.
    In DNA 'A' matches with 'T', 'G' matches with 'C'
    In RNA 'A' matches with 'U', 'G' matches with 'C'
    If a pair contains an invalid base the pair should be removed.
    Pairs of empty bases should be ignored.
    """
    pass

def mast_common_base(dna):
    count = {'A': 0, 'T': 0, 'U': 0, 'C': 0, 'G': 0}
    for (pair1,pair2) in dna:
        if not pair1:
            continue
        count[pair1] += 1

    return max(count, key=count.get)
    """
    Given DNA in the aforementioned format,
    return the most common first base:
    eg. given:
    A <-> T
    G <-> C
    G <-> C
    C <-> G
    G <-> C
    T <-> A
    The most common first base is 'G'.
    Empty bases should be ignored.
    """
    pass

def base_to_name(base):
    if base == 'A':
        return "Adenine"
    elif base == 'T':
        return "Thymine"
    elif base == "G":
        return "Guanine"
    elif base == "C":
        return "Cytosine"
    elif base == "U":
        return "Uracil"
    else:
        return "Unknown"    
    """
    Given a base, return the name of the base.
    The base names are:
    Adenine  ('A'),
    Thymine  ('T'),
    Guanine  ('G'),
    Cytosine ('C'),
    Uracil   ('U'),
    return the string "Unknown" if the base isn't one of the above.
    """
    pass