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

s1 = Seq("AGTACACTGGT")
s2 = Seq("CGXAAC")
#print(f"Sequence 1: {s1}")
#print(f"Sequence 2: {s2}")