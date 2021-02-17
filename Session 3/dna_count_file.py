def read_from_file(filename):
    with open(filename, "r") as f:
        dna_seq = f.read()
        dna_seq = dna_seq.replace("\n", "")
        return dna_seq

def correct_seq(dna_seq):
    for base in dna_seq:
        if base != "A" and base != "G" and base != "T" and base != "C":
            return False
        else:
            return True

def DNA_count(dna_seq):
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

filename = "dna.txt"
dna_seq = read_from_file(filename)
print(dna_seq)
if correct_seq(dna_seq):
    dif_bases, a, g, t, c = DNA_count(dna_seq)
    print("Number of different bases: " + str(dif_bases) + "\nTotal A: " + str(a) + "\nTotal G: " + str(g) + "\nTotal T: " + str(t) + "\nTotal C: " + str(c))
else:
    print("Not valid sequence. The DNA sequence is incorrect.")




