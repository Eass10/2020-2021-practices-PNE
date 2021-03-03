class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        if self.is_valid_sequence2(strbases):
            print("New sequence created!")
            self.strbases = strbases
        else:
            self.strbases = "ERROR!!"
            print("Incorrect sequence detected")

    @staticmethod
    def is_valid_sequence2(bases):
        for base in bases:
            if base != "A" and base != "T" and base != "C" and base != "G":
                return False
        return True

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

    @staticmethod
    def print_seqs(seq_list):
        for i in range(0, len(seq_list)):
            print("Sequence", i, "(Length:", seq_list[i].len(), ")", seq_list[i])
