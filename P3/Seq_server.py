import socket
import Server_utils
from Seq3 import Seq
list_sequences = ["AAAA", "CCCC", "TTTT", "GGGG", "ACTG"]
# gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
PORT = 8080
IP = "127.0.0.1"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("Seq server is configured!")
client_addres_list = []
count_connections = 0
while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        print("A client has connected to the server!")
        count_connections += 1
        client_addres_list.append((cs, client_ip_port))
        print("CONNECTION " + str(count_connections) + ". Client IP, PORT: " + str(client_ip_port))
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    msg_raw = cs.recv(2048)
    msg = msg_raw.decode()
    formatted_msg = Server_utils.format_command(msg)
    formatted_msg = formatted_msg.split(" ")
    if len(formatted_msg) == 1:
        command = formatted_msg[0]
    else:
        command = formatted_msg[0] + '"'
        argument = '"' + formatted_msg[1]
    if command == '"PING"':
        Server_utils.ping(cs)

    elif command == '"GET"':
        Server_utils.Get(list_sequences, cs, argument)

    elif command == '"INFO"':
        Server_utils.info(argument, cs)

    elif command == '"COMP"':
        Server_utils.comp(argument, cs)

    elif command == '"REV"':
        Server_utils.rev(argument, cs)

    elif command == '"GENE"':
        Server_utils.gene(argument, cs)

    else:
        response = "Not available command"
        cs.send(response.encode())
    cs.close()
