class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

class Gene(Seq):
    """This is derived from the Seq Class
    All the objects of class Gene will inheritate
    the methods from the Seq class"""
    def __init__(self, strbases, name=""):
        # call first the Seq initializer and the the gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the gene name along with the sequence"""
        return self.name + "-" + self.strbases


#Main program
#Create an object of the class Seq
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f" Length: {s1.len()}")
print(f"Gene: {g}")
print(f" Length: {g.len()}")
print("Testing...")