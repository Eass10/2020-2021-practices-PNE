import Seq0
File = "U5.txt"
FOLDER = "./Sequences/"
U5_seq = Seq0.seq_read_fasta(FOLDER + File)
print("---|EXERCISE 7|---")
print("Fragment: " + U5_seq[:21] + "\nReverse: " + Seq0.seq_complement(U5_seq[:21]))