import Seq0
FOLDER = "./Sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
DNA_bases = ["A", "C", "T", "G"]
print("---|EXERCISE 5|---")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(FOLDER + gene + ".txt")
    print("Gene " + gene + ": ", Seq0.seq_count(sequence))
