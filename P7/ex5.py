import http.client
import json
from Seq7 import Seq
from termcolor import colored

def print_colored(message, data, color):
    print(colored(message, color), end="")
    print(data)

DICT_GENES = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000226906",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
PARAMS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)
try:
    for key, id in DICT_GENES.items():
        connection.request("GET", ENDPOINT + id + PARAMS)
        response = connection.getresponse()
        print("\nSERVER: ", SERVER)
        print("URL: ", SERVER + ENDPOINT + id + PARAMS)
        print("Response received:", response.status, response.reason, "\n")
        if response.status == 200:
            response_dict = json.loads(response.read().decode())
            # print(json.dumps(response_dict, indent=4, sort_keys=True))
            print_colored("GENE: ", key, "yellow")
            print_colored("Description ", response_dict["desc"], "yellow")
            sequence = Seq(response_dict["seq"])
            seq_length = sequence.len()
            count_dict, info = sequence.count_base_2()
            most_frequent_base = sequence.frequent_base(count_dict)
            print(colored("Total length:", "yellow"), seq_length, info, "\n", colored("Most frequent base:", "yellow"), most_frequent_base, "\n")
except KeyError:
    print("The gene is not inside our database. Choose one of the following", list(DICT_GENES.keys()))
