from Seq1 import Seq
FOLDER = "./Sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
DNA_bases = ["A", "C", "T", "G"]
print("---|PRACTICE 1: EXERCISE 10|---")
for gene in gene_list:
    sequence = Seq.seq_read_fasta(FOLDER + gene + ".txt")
    gene_dict = sequence.count_base()
    base, n = Seq.processing(gene_dict)
    print("For gene " + gene + " the most frequent base is " + base + " with " + str(n) + " repetitions.")