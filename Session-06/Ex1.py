class Seq:
    # it could be done calling a module
    def __init__(self, strbases):
        self.strbases = strbases
        if self.is_valid_sequence():
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "ERROR!!"
            print("Incorrect sequence detected")

    def is_valid_sequence(self):
        for base in self.strbases:
            if base != "A" and base != "T" and base != "C" and base != "G":
                return False
        return True

s1 = Seq("AGTACACTGGT")
s2 = Seq("CGXAAC")
#print(f"Sequence 1: {s1}")
#print(f"Sequence 2: {s2}")
"""when using staticmethod we use the name of the class
when using a method of the class we use self
when using a module we use his name"""