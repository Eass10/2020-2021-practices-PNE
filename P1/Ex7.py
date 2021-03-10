import Seq1

def print_result(n, seq):
    print("Sequence" + str(n) + ": (Length: " + str(seq.len()) + ") " + str(seq))
    print("  Bases:", seq.count_base())
    print("  Rev:", seq.seq_reverse())

print("---|PRACTICE 1: EXERCISE 7|---")
list_seq = list(Seq1.test_sequence())
for n in range(1, len(list_seq) + 1):
    print_result(n, list_seq[n - 1])