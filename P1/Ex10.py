from Seq1 import Seq
FOLDER = "./Sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
DNA_bases = ["A", "C", "T", "G"]
print("---|PRACTICE 1: EXERCISE 10|---")
list_Seq = []
for gene in gene_list:
    sequence = Seq(Seq.seq_read_fasta_2(FOLDER + gene + ".txt"))
    list_Seq.append(sequence)
for seq in list_Seq:
    gene_dict = seq.count_base()
    base, n = Seq.processing(gene_dict)
    print("For gene " + gene + " the most frequent base is " + base + " with " + str(n) + " repetitions.")