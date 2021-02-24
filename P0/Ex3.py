import Seq0
FOLDER = "./Sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
print("---|EXERCISE 3|---")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(FOLDER + gene + ".txt")
    print("Gene " + gene + " ---> Length: " +  str(Seq0.seq_len(sequence)))