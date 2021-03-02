class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        return len(self.strbases)

def generate_seqs(pattern, number):
    seq = ""
    seq_list = []
    for i in range(0, number):
        seq += pattern
        seq_list.append(Seq(seq))
    return seq_list

def print_seqs(seq_list):
    for seq in seq_list:
        print(f"Sequence {seq_list.index(seq)}: (Length: {Seq.len(seq)}) {seq}")

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)
print("---LIST 1---")
print_seqs(seq_list1)

print("---LIST 2---")
print_seqs(seq_list2)