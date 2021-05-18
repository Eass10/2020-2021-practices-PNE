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
    path_name = "listSpecies"
    n = "10"
    conn.request("GET", "/" + path_name + "?limit=" + n + "&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
cu.list_species(conn)


try:
    path_name = "listSpecies"
    n = ""
    conn.request("GET", "/" + path_name + "?limit=" + n + "&json=1")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
cu.list_species(conn)