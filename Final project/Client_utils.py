import json
from termcolor import colored, cprint


def list_species(conn):
    print("Testing listSpecies for 10 as the limit...\n")
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    information = json.loads(data1)
    # print(json.dumps(information, indent=4, sort_keys=True))
    if "ERROR" in information.values():
        cprint("ERROR. No limit selected", "red")
    else:
        cprint("Amount of species: ", 'green', end="")
        print(information['amount_species'])
        cprint("The limit you have chosen: ", 'green', end="")
        print(information['limit'])
        cprint("List of species: ", 'blue')
        for species in information['names']:
            print("   " + species)