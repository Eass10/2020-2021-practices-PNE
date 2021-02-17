def DNA_count(dna_seq):
    l = len(dna_seq)
    A = dna_seq.count("A")
    G = dna_seq.count("G")
    T = dna_seq.count("T")
    C = dna_seq.count("C")
    return l, A, G, T, C

def DNA_count_2(dna_seq):
    l = len(dna_seq)
    a, g, t, c = 0, 0, 0, 0
    for base in dna_seq:
        if base == "A":
            a +=1
        elif base == "G":
            g += 1
        elif base == "T":
            t += 1
        elif base == "C":
            c += 1
    return l, a, g, t, c

dna_seq = "CATGTAGACTAG"
print("---FIRST FUNCTION---")
l, A, G, T, C = DNA_count(dna_seq)
print("Total length: " + str(l) + "\nA: " + str(A) + "\nG: " + str(G) + "\nT: " + str(T) + "\nC: " + str(C))
print("---SECOND FUNCTION---")
l, a, g, t, c = DNA_count_2(dna_seq)
print("Total length: " + str(l) + "\nA: " + str(a) + "\nG: " + str(g) + "\nT: " + str(t) + "\nC: " + str(c))
