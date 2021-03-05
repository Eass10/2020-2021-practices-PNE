from Seq1 import Seq
print("---|PRACTICE 1: EXERCISE 5|---")
DNA_bases = ["A", "C", "T", "G"]
s1 = Seq("ACTGA")
s2 = Seq()
s3 = Seq("ACTXG")
print("Sequence" + str(1) + ": (Length: " + str(s1.len()) + ") " + str(s1))
print("A:", s1.count_base()["A"], "; C:", s1.count_base()["C"], "; T:", s1.count_base()["T"], "; G:", s1.count_base()["G"], )
print("Sequence" + str(2) + ": (Length: " + str(s2.len()) + ") " + str(s2))
print("A:", s2.count_base()["A"], "; C:", s2.count_base()["C"], "; T:", s2.count_base()["T"], "; G:", s2.count_base()["G"], )
print("Sequence" + str(3) + ": (Length: " + str(s3.len()) + ") " + str(s3))
print("A:", s3.count_base()["A"], "; C:", s3.count_base()["C"], "; T:", s3.count_base()["T"], "; G:", s3.count_base()["G"], )
