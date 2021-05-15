import http.client
import json
import termcolor
PORT = 8080
SERVER = '127.0.0.1'
print(f"\nConnecting to server: {SERVER}:{PORT}\n")
# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)
# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    path_name = input("Introduce what endpoint do yoy want to see: ")
    if path_name.lower() == "listspecies":
        n = input("Introduce the number of species you want to see: ")
        conn.request("GET", "/" + path_name + "?limit=" + n + "&json=1")
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
# -- Read the response message from the server
r1 = conn.getresponse()
# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")
# -- Read the response's body
data1 = r1.read().decode("utf-8")
# -- Create a variable with the data,
# -- form the JSON received
information = json.loads(data1)
print(json.dumps(information, indent=4, sort_keys=True))
# print("Total people in database: " + str(len(information)) + "\nCONTENT: ")
"""for person in people:
    # Print the information in the object
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])
    # Get the phoneNumber list
    phoneNumbers = person['phoneNumber']
    # Print the number of elements int the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))
    # Print all the numbers
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(i), 'blue')
        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])"""