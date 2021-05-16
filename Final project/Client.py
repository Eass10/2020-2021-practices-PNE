import http.client
import Client_utils as cu
import json
from termcolor import colored, cprint
PORT = 8080
SERVER = '127.0.0.1'
print(f"\nConnecting to server: {SERVER}:{PORT}\n")
# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)
# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    path_name = input("Introduce what endpoint do you want to see: ")
    if path_name.lower() == "listspecies":
        cu.list_species(conn, path_name)
    elif path_name == "/karyotype":
        specie = input("Introduce the specie you want to see: ")
        conn.request("GET", "/" + path_name + "?species=" + specie + "&json=1")
    elif path_name == "/chromosomeLength":
        specie = input("Introduce the specie you want to see: ")
        chromosome = input("Introduce the chromosome you want to see: ")
        conn.request("GET", "/" + path_name + "?species=" + specie + "&chromosome=" + chromosome + "&json=1")
    elif path_name == "/geneSeq":
        gene = input("Introduce the gene you want to see: ")
        conn.request("GET", "/" + path_name + "?gene=" + gene + "&json=1")
    elif path_name == "/geneInfo":
        gene = input("Introduce the gene you want to see: ")
        conn.request("GET", "/" + path_name + "?gene=" + gene + "&json=1")
    elif path_name == "/geneCalc":
        gene = input("Introduce the gene you want to see: ")
        conn.request("GET", "/" + path_name + "?gene=" + gene + "&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# print("Total people in database: " + str(len(information)) + "\nCONTENT: ")