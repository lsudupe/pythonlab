import re

def buscar_motivo(a, b):
    index = [motif.start() for motif in re.finditer(b, a)]
    if index == []:
        return [-1]
    else:
        return index

t1 = 'AUGCUUCAGAAAGGUCUUACGUGCUUUA'
s1 = 'UGCU'
print(buscar_motivo(t1, s1))

t2 = 'AUGCUUCAGAAAGGUCUUACGU'
s2 = 'U'
print(buscar_motivo(t2, s2))

t3 = 'AUGCUUCAGAAAGGUCUUACGU'
s3 = 'UGCG'
print(buscar_motivo(t3, s3))

t4 = 'GCGTAGTAGGTTCGCCTAGTTCCGCCGAAAGACAAAGGAGAAGGGAATGCTCCT\
AGTAGTTTCAGTCTAGCAAACATGTTATAACGCTAACTGTGTGCTGCA'
s4 = 'AGA'
print(buscar_motivo(t4, s4))






'''p = 'CGAAGCAATTGAAACCCCCCCGGCCTGGGAGGCGCAAAAATCTGACCTCTTTGT\
GAGTTGACCACTTAATTTATGTCTGACCACGAGAAGGGCTACTGATTTGGTA'
q = 'GGTAGTAGGTTCGCGTACCTCGTTCCGGGGAAAACACAAAGGAGAAGGGAATGC\
TCCTAGTAGTTTCAGTCTAGCAAACATGTTATAACGCTAACTGTGTGCTGCA'

a = 'CCGTA'
b = 'ACGTC'
def hamming(p, q):
    count = 0
    for idx, (nuc1, nuc2) in enumerate(zip(p,q)):
        if nuc1 != nuc2:
            count += 1
    return count

print(hamming(p, q))
print(hamming(a, b))







seq = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCATTAC'

def Ecolisep(secuencia):
    index = secuencia.index('GAATTC') + 1
    seq1, seq2 = secuencia[:index], secuencia[index:]
    return "Nuestra secuencia se divide en dos subsecuencias que son {} y {}".format(seq1, seq2)

print(Ecolisep(seq))'''


'''from collections import Counter 

def representation(idx, counter):
    print("Secuencia {}:".format(idx))
    for nucleotide in 'ACGT':
        print("Número de {}'s: {}".format(nucleotide, counter[nucleotide]))

def nucleodite_num(fasta_file_name):
    with open(fasta_file_name) as secuences:
        idx = 0 
        counter = Counter()

        for line in secuences:
            lin = line.rstrip('\n')
            if lin.startswith(">"):
                if idx > 0:
                    representation(idx, counter) 
                idx += 1
                counter.clear()
            else:
                counter.update(lin)
    return representation(idx, counter)
        
print(nucleodite_num("assembledSeqs.fa"))'''