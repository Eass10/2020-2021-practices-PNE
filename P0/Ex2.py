import Seq0
FOLDER = "./Sequences/"
File = "U5.txt"
U5_seq = Seq0.seq_read_fasta(FOLDER + File)
print("DNA file: " + File + "\nThe first 20 bases are: ", U5_seq[:21])
