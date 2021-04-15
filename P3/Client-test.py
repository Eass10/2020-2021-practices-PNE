import Client3

c = Client3.Client("127.0.0.1", 8080)
command_list = ['"PING"', '"GET"', '"INFO"', '"COMP"', '"REV"', '"GENE"']

print("Testing Ping...")
c.talk('"PING"')

print("Testing Get...")
for i in range(0, 5):
    msg = "GET " + str(i)
    c.talk('"' + msg + '"')

print("\nTesting Info...")
c.talk('"INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"')

print("\nTesting Comp")
c.talk('"COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"')

print("\nTesting Rev...")
c.talk('"REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"')

print("\nTesting Gene...")
gene_list = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
for gene in gene_list:
    msg = "GENE " + gene
    c.talk('"' + msg + '"')
