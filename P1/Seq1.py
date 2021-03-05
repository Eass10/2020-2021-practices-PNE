class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases="NULL"):
        if strbases == "NULL":
            print("NULL seq created")
            self.strbases = strbases
        else:
            if self.is_valid_sequence(strbases):
                print("New sequence created!")
                self.strbases = strbases
            else:
                self.strbases = "ERROR"
                print("Incorrect sequence detected")

    @staticmethod
    def is_valid_sequence(bases):
        for base in bases:
            if base != "A" and base != "T" and base != "C" and base != "G":
                return False
        return True

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

    def count_base(self):
        gene_dict = {"A": 0, "C": 0, "T": 0, "G": 0}
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return gene_dict
        else:
            for base in self.strbases:
                gene_dict[base] += 1
            return gene_dict

    @staticmethod
    def processing(gene_dict):
        list_values = gene_dict.values()
        most_common_base = max(list_values)
        for base, n in gene_dict.items():
            if n == most_common_base:
                return base, n

    def seq_reverse(self):
        if self.strbases == "NULL":
            return "NULL"
        elif self.strbases == "ERROR":
            return "ERROR"
        else:
            return self.strbases[::-1]

    def seq_complement(self):
        comp_dict = {"A": "T", "C": "G", "T": "A", "G": "C"}
        string = ""
        if self.strbases == "NULL":
            return "NULL"
        elif self.strbases == "ERROR":
            return "ERROR"
        else:
            for base in self.strbases:
                base = comp_dict[base]
                string += base
            return string

    @staticmethod
    def seq_read_fasta(Filename):
        from pathlib import Path
        seq = Path(Filename).read_text()
        seq = Seq(seq[seq.index("\n"):].replace("\n", ""))
        return seq