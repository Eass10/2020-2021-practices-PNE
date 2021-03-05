from Seq1 import Seq
print("---|PRACTICE 1: EXERCISE 6|---")
DNA_bases = ["A", "C", "T", "G"]
s1 = Seq("ACTGA")
s2 = Seq()
s3 = Seq("ACTXG")
print("Sequence" + str(1) + ": (Length: " + str(s1.len()) + ") " + str(s1))
print(s1.count_base())
print("Sequence" + str(2) + ": (Length: " + str(s2.len()) + ") " + str(s2))
print(s2.count_base())
print("Sequence" + str(3) + ": (Length: " + str(s3.len()) + ") " + str(s3))
print(s3.count_base())