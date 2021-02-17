def DNA_count_file(filename):
    with open(filename, "r") as f:
        bases = []
        a, g, t, c = 0, 0, 0, 0
        for line in f:
            line = line.replace("\n", "")
            for base in line:
                bases.append(base)
                dif_bases = len(set(bases))
                if base == "A":
                    a += 1
                elif base == "G":
                    g += 1
                elif base == "T":
                    t += 1
                elif base == "C":
                    c += 1
        return dif_bases, a, g, t, c


filename = "dna.txt"
dif_bases, a, g, t, c = DNA_count_file(filename)
print("Number of different bases: " + str(dif_bases) + "\nTotal A: " + str(a) + "\nTotal G: " + str(g) + "\nTotal T: " + str(t) + "\nTotal C: " + str(c))



