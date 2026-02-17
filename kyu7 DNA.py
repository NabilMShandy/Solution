def DNA_strand(dna):
    emptyLs = []
    for i in range(len(dna)):
        if dna[i] == 'A': emptyLs.append(dna[i].replace('A', 'T'))
        elif dna[i] == 'T': emptyLs.append(dna[i].replace('T', 'A'))
        elif dna[i] == 'C': emptyLs.append(dna[i].replace('C', 'G'))
        elif dna[i] == 'G': emptyLs.append(dna[i].replace('G', 'C'))
    return "".join(emptyLs)

print(DNA_strand("ATTGC"))