class Seq:
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"

    def __init__(self, strbases=NULL_SEQUENCE):
        if strbases == Seq.NULL_SEQUENCE:
            print("NULL seq created")
            self.strbases = strbases
        else:
            if self.is_valid_sequence(strbases):
                print("New sequence created!")
                self.strbases = strbases
            else:
                self.strbases = Seq.INVALID_SEQUENCE
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
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_base(self):
        gene_dict = {"A": 0, "C": 0, "T": 0, "G": 0}
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
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
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            return self.strbases[::-1]

    def seq_complement(self):
        comp_dict = {"A": "T", "C": "G", "T": "A", "G": "C"}
        string = ""
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            for base in self.strbases:
                base = comp_dict[base]
                string += base
            return string

    def seq_read_fasta(self, Filename):
        from pathlib import Path
        sequence = Path(Filename).read_text()
        self.strbases = sequence[sequence.index("\n"):].replace("\n", "")
        return self.strbases

def test_sequence():
    s1 = Seq("ACTGA")
    s2 = Seq()
    s3 = Seq("ACTXG")
    return s1, s2, s3