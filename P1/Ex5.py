import Seq1

def print_result(n, seq):
    print("Sequence" + str(n) + ": (Length: " + str(seq.len()) + ") " + str(seq))
    gene_dict = seq.count_base()
    print("A:", gene_dict["A"], "; C:", gene_dict["C"], "; T:", gene_dict["T"], "; G:", gene_dict["G"], )

print("---|PRACTICE 1: EXERCISE 5|---")
list_seq = list(Seq1.test_sequence())
for n in range(1, len(list_seq) + 1):
    print_result(n, list_seq[n - 1])