import http.client
import json
import Client_utils as cu
from termcolor import cprint
PORT = 8080
SERVER = '127.0.0.1'
list_function = ["/", "listSpecies", "karyotype", "chromosomeLength", "geneSeq", "geneInfo", "geneCalc"]
print("\nAdvance level services")
print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)
for path_name in list_function:
    if path_name == "/":
        cprint("\n---TESTING INDEX---", 'yellow')
        cu.connect(conn, path_name, argument=None, value=None, value_2=None)
        cu.index(cu.get_response(conn))

    elif path_name == "listSpecies":
        cprint("\n---TESTING LIST SPECIES FUNCTION---", 'yellow')
        argument = "limit"

        cprint("1. Testing listSpecies for 10 as the limit...", 'yellow', end="\n")
        n_1 = "10"
        cu.connect(conn, path_name, argument, n_1, value_2=None)
        cu.list_species(cu.get_response(conn))

        cprint("2. Testing listSpecies for no chosen limit...", 'yellow', end="\n")
        n_2 = ""
        cu.connect(conn, path_name, argument, n_2, value_2=None)
        cu.list_species(cu.get_response(conn))

    elif path_name == "karyotype":
        cprint("\n---TESTING KARYOTYPE FUNCTION---", 'yellow')
        argument = "species"

        cprint("1. Testing karyotype for human as the species...", 'yellow', end="\n")
        species_1 = "human"
        cu.connect(conn, path_name, argument, species_1, value_2=None)
        cu.karyotype(cu.get_response(conn))

        cprint("2. Testing karyotype for no chosen specie...", 'yellow', end="\n")
        species_2 = ""
        cu.connect(conn, path_name, argument, species_2, value_2=None)
        cu.karyotype(cu.get_response(conn))

    elif path_name == "chromosomeLength":
        cprint("\n---TESTING CHROMOSOME LENGTH FUNCTION---", 'yellow')

        cprint("1. Testing chromosomeLength for human as the species and 18 as the chromosome...", 'yellow', end="\n")
        value_1a = "human"
        value_1b = "18"
        cu.connect(conn, path_name, argument, value_1a, value_1b)
        cu.chromosome_length(cu.get_response(conn))

        cprint("2. Testing chromosomeLength for no chosen species nor chromosome...", 'yellow', end="\n")
        value_2a = ""
        value_2b = ""
        cu.connect(conn, path_name, argument, value_2a, value_2b)
        cu.chromosome_length(cu.get_response(conn))

        cprint("3. Testing chromosomeLength for no chosen chromosome...", 'yellow', end="\n")
        cu.connect(conn, path_name, argument, value_1a, value_2b)
        cu.chromosome_length(cu.get_response(conn))

        cprint("4. Testing chromosomeLength for no chosen species...", 'yellow', end="\n")
        cu.connect(conn, path_name, argument, value_2a, value_1b)
        cu.chromosome_length(cu.get_response(conn))

    elif path_name == "geneSeq":
        cprint("\n---TESTING GENE SEQUENCE FUNCTION---", 'yellow')
        argument = "gene"

        cprint("1. Testing geneSeq for ADA as the gene...", 'yellow', end="\n")
        gene_1 = "ADA"
        cu.connect(conn, path_name, argument, gene_1, value_2=None)
        cu.geneSeq(cu.get_response(conn))

        cprint("2. Testing geneSeq for no chosen gene...", 'yellow', end="\n")
        gene_2 = ""
        cu.connect(conn, path_name, argument, gene_2, value_2=None)
        cu.geneSeq(cu.get_response(conn))

    elif path_name == "geneInfo":
        cprint("\n---TESTING GENE INFORMATION FUNCTION---", 'yellow')
        argument = "gene"

        cprint("1. Testing geneInfo for ADA as the gene...", 'yellow', end="\n")
        gene_1 = "ADA"
        cu.connect(conn, path_name, argument, gene_1, value_2=None)
        cu.geneInfo(cu.get_response(conn))

        cprint("2. Testing geneInfo for no chosen gene...", 'yellow', end="\n")
        gene_2 = ""
        cu.connect(conn, path_name, argument, gene_2, value_2=None)
        cu.geneInfo(cu.get_response(conn))

    elif path_name == "geneCalc":
        cprint("\n---TESTING GENE CALCULATION FUNCTION---", 'yellow')
        argument = "gene"

        cprint("1. Testing geneCalc for ADA as the gene...", 'yellow', end="\n")
        gene_1 = "ADA"
        cu.connect(conn, path_name, argument, gene_1, value_2=None)
        cu.geneCalc(cu.get_response(conn))

        cprint("2. Testing geneCalc for no chosen gene...", 'yellow', end="\n")
        gene_2 = ""
        cu.connect(conn, path_name, argument, gene_2, value_2=None)
        cu.geneCalc(cu.get_response(conn))
