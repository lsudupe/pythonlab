from collections import Counter 

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
        

print(nucleodite_num("assembledSeqs.fa"))