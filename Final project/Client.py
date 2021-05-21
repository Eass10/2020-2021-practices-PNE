import http.client
import Client_utils as cu
import json
from termcolor import colored, cprint
PORT = 8080
SERVER = '127.0.0.1'
list_function = ["listSpecies", "karyotype", "chromosomeLength"]
print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)
for path_name in list_function:
    if path_name == "listSpecies":
        cprint("---TESTING LIST SPECIES FUNCTION---", 'yellow')
        argument = "limit"

        cprint("1. Testing listSpecies for 10 as the limit...", 'yellow', end="\n")
        n_1 = "10"
        cu.connect(conn, path_name, argument, n_1)
        cu.list_species(conn)

        cprint("2. Testing listSpecies for no chosen limit...", 'yellow', end="\n")
        n_2 = ""
        cu.connect(conn, path_name, argument, n_2)
        cu.list_species(conn)

    elif path_name == "karyotype":
        cprint("\n---TESTING KARYOTYPE FUNCTION---", 'yellow')
        argument = "species"

        cprint("1. Testing karyotype for human as the species...", 'yellow', end="\n")
        species_1 = "human"
        cu.connect(conn, path_name, argument, species_1)
        cu.karyotype(conn)

        cprint("2. Testing karyotype for no chosen specie...", 'yellow', end="\n")
        species_2 = ""
        cu.connect(conn, path_name, argument, species_2)
        cu.karyotype(conn)

    elif path_name == "chromosomeLength":
        cprint("\n---TESTING CHROMOSOME LENGTH FUNCTION---", 'yellow')
        argument = "species"
        argument = "chromosome"

        cprint("1. Testing chromosomeLength for human as the species and 18 as the chromosome...", 'yellow', end="\n")
        value_1a = "human"
        value_1b = "18"
        cu.connect_2(conn, path_name, argument, value_1a, argument, value_1b)
        cu.chromosome_length(conn)

        cprint("2. Testing chromosomeLength for no chosen species nor chromosome...", 'yellow', end="\n")
        value_2a = ""
        value_2b = ""
        cu.connect_2(conn, path_name, argument, value_2a, argument, value_2b)
        cu.chromosome_length(conn)

        cprint("3. Testing chromosomeLength for no chosen chromosome...", 'yellow', end="\n")
        cu.connect_2(conn, path_name, argument, value_1a, argument, value_2b)
        cu.chromosome_length(conn)

        cprint("4. Testing chromosomeLength for no chosen species...", 'yellow', end="\n")
        cu.connect_2(conn, path_name, argument, value_2a, argument, value_1b)
        cu.chromosome_length(conn)
