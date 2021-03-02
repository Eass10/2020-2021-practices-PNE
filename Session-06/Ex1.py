class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases
        correct = True
        for base in strbases:
            if base != "A" and base != "T" and base != "C" and base != "G":
                correct = False
        if not correct:
            print("ERROR!! Incorrect sequence detected")
        else:
            print("New sequence created!")

s1 = Seq("AGTACACTGGT")
s2 = Seq("CGXAAC")
#print(f"Sequence 1: {s1}")
#print(f"Sequence 2: {s2}")