import Seq0
FOLDER = "./Sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
DNA_bases = ["A", "C", "T", "G"]
print("---|EXERCISE 8|---")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(FOLDER + gene + ".txt")
    print("For gene " + gene + " the most frequent base is: ", Seq0.processing(sequence))
