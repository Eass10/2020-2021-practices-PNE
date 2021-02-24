import Seq0
FOLDER = "./Sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
DNA_bases = ["A", "C", "T", "G"]
print("---|EXERCISE 4|---")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(FOLDER + gene + ".txt")
    print("Gene: " + gene)
    for base in DNA_bases:
        print(base + ": ", Seq0.seq_count_base(sequence, base))
