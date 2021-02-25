def seq_ping():
    print("OK")

def delete_first_line(seq):
    return seq[seq.index("\n"):].replace("\n", "")

def seq_read_fasta(Filename):
    from pathlib import Path
    seq = delete_first_line(Path(Filename).read_text())
    return seq

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    gene_dict = {"A": 0, "C": 0, "T": 0, "G": 0}
    for base in seq:
        gene_dict[base] += 1
    return gene_dict

def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):
    comp_dict = {"A": "T", "C": "G", "T": "A", "G": "C"}
    string = ""
    for base in seq:
        base = comp_dict[base]
        string += base
    return string

def processing(seq):
    from collections import Counter
    base_list = []
    for base in seq:
        base_list.append(base)
    count = Counter(base_list)
    most_common_base = count.most_common()[0][0]
    return most_common_base



