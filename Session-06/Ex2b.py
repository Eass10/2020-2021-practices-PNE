from Seq1_ex import Seq

def print_seqs(seq_list):
    for i in range(0, len(seq_list)):
        print("Sequence", i, "(Length:",  Seq.len(seq_list[i]), ")", seq_list[i])

def print_seqs2(seq_list):
    for seq in seq_list:
        print(f"Sequence {seq_list.index(seq)}: (Length: {Seq.len(seq)}) {seq}")

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)