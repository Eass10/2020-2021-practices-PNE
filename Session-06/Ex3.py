from Seq1_ex import Seq

def generate_seqs(pattern, number):
    seq_list = []
    for i in range(0, number):
        seq_list.append(Seq(pattern * (i + 1)))
    return seq_list

def print_seqs(seq_list):
    for i in range(0, len(seq_list)):
        print("Sequence", i, "(Length:",  Seq.len(seq_list[i]), ")", seq_list[i])

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)
print("---LIST 1---")
print_seqs(seq_list1)

print("---LIST 2---")
print_seqs(seq_list2)