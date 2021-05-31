import json
from termcolor import cprint


def connect(conn, path_name, argument, value):
    try:
        conn.request("GET", "/" + path_name + "?" + argument + "=" + value + "&json=1")
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()


def connect_2(conn, path_name, argument_1, value_1, argument_2, value_2):
    try:
        conn.request("GET", "/" + path_name + "?" + argument_1 + "=" + value_1 + "&" + argument_2 + "=" + value_2 + "&json=1")
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()


def get_response(conn):
    r1 = conn.getresponse()
    # print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    information = json.loads(data1)
    # print(json.dumps(information, indent=4, sort_keys=True))
    return information


def list_species(information):
    if information["limit"] == "ERROR":
        cprint("ERROR. No limit selected.", "red")
    else:
        cprint("Amount of species:", 'green', end=" ")
        print(information['amount_species'])
        cprint("The limit you have chosen:", 'green', end=" ")
        print(information['limit'])
        cprint("List of species: ", 'green')
        for species in information['names']:
            print(" · " + species)


def karyotype(information):
    if information["karyotype"] == "ERROR":
        cprint("ERROR. No species selected.", "red")
    else:
        cprint("The karyotype for", 'green', end=" ")
        print(information['species'], end=" ")
        cprint("is: ", 'green')
        for chromosome in information["karyotype"]:
            print(" · " + chromosome)


def chromosome_length(information):
    if information["length"] == "ERROR":
        cprint("ERROR. Not species, nor chromosome selected.", 'red')
    elif information["length"] == "ERROR 1":
        cprint("ERROR. No chromosome selected.", 'red')
    elif information["length"] == "ERROR 2":
        cprint("ERROR. No species selected.", 'red')
    else:
        cprint("The lenght of the", 'green', end=" ")
        print(information["species"], end=" ")
        cprint("chromosome", 'green', end=" ")
        print(information["chromosome"], end=" ")
        cprint("is:", 'green', end=" ")
        print(information["length"])


def geneSeq(information):
    if information["seq"] == "ERROR":
        cprint("ERROR. No gene selected.", "red")
    else:
        cprint("The sequence for the gene", 'green', end=" ")
        print(information["gene"], end=" ")
        cprint("is: ", 'green')
        print(information["seq"])


def geneInfo(information):
    if information["dict_info"] == "ERROR":
        cprint("ERROR. No gene selected.", "red")
    else:
        cprint("Information for the gene", 'green', end=" ")
        print(information["gene"], end=":\n")
        for key, value in information["dict_info"].items():
            print(" · " + key + ": " + str(value))


def geneCalc(information):
    if information["bases"] == "ERROR":
        cprint("ERROR. No gene selected.", "red")
    else:
        cprint("Bases calculations for the gene", 'green', end=" ")
        print(information["gene"], end=":\n")
        for key, value in information["bases"].items():
            print(" · " + key + ": " + str(value))
