import Client3

c = Client3.Client("127.0.0.1", 8080)
command_list = ['"PING"', '"GET"', '"INFO"', '"COMP"', '"REV"', '"GENE"']
com = True
while com:
    for command in command_list:
        if command == '"PING"':
            print("\nTesting Ping...")
            c.talk('"PING"')

        elif command == '"GET"':
            print("\nTesting Get...")
            for i in range(0, 5):
                msg = "GET " + str(i)
                c.talk('"' + msg + '"')

        elif command == '"INFO"':
            print("\nTesting Info...")
            c.talk('"INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"')

        elif command == '"COMP"':
            print("\nTesting Comp")
            c.talk('"COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"')

        elif command == '"REV"':
            print("\nTesting Rev...")
            c.talk('"REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"')

        elif command == '"GENE"':
            print("\nTesting Gene...")
            gene_list = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
            for gene in gene_list:
                msg = "GENE " + gene
                print(msg)
                c.talk('"' + msg + '"')
                com = False
