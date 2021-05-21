import json
from termcolor import colored, cprint


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


def list_species(conn):
    r1 = conn.getresponse()
    # print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    information = json.loads(data1)
    # print(json.dumps(information, indent=4, sort_keys=True))
    if information["limit"] == "ERROR":
        cprint("ERROR. No limit selected", "red")
    else:
        cprint("Amount of species: ", 'green', end="")
        print(information['amount_species'])
        cprint("The limit you have chosen: ", 'green', end="")
        print(information['limit'])
        cprint("List of species: ", 'blue')
        for species in information['names']:
            print("   " + species)


def karyotype(conn):
    r1 = conn.getresponse()
    # print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    information = json.loads(data1)
    # print(json.dumps(information, indent=4, sort_keys=True))
    if information["karyotype"] == "ERROR":
        cprint("ERROR. No species selected", "red")
    else:
        cprint("The karyotype for ", 'green', end="")
        print(information['species'], end=" ")
        cprint("is: ", 'green')
        for chromosome in information["karyotype"]:
            print("   " + chromosome)

def chromosome_length(conn):
    r1 = conn.getresponse()
    # print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    information = json.loads(data1)
    # print(json.dumps(information, indent=4, sort_keys=True))
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

