from Seq1 import Seq
print("---|PRACTICE 1: EXERCISE 9|---")
FOLDER = "./Sequences/"
File = "U5.txt"
U5_seq = Seq.seq_read_fasta(FOLDER + File)
print("Sequence: (Length: " + str(U5_seq.len()) + ") " + str(U5_seq))
print("  Bases:", U5_seq.count_base())
print("  Rev:", U5_seq.seq_reverse())
print("  Comp:", U5_seq.seq_complement())