from Seq1 import Seq

def print_result(seq):
    print("Sequence: (Length: " + str(seq.len()) + ") " + str(seq))
    print("  Bases:", seq.count_base())
    print("  Rev:", seq.seq_reverse())
    print("  Comp:", seq.seq_complement())

print("---|PRACTICE 1: EXERCISE 9|---")
FOLDER = "./Sequences/"
File = "U5.txt"
s1 = Seq()
s1.seq_read_fasta(FOLDER + File)
print_result(s1)