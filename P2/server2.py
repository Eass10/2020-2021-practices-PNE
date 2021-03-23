import socket
from termcolor import colored
import colorama

# Configure the Server's IP and PORT
PORT = 12300
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        colorama.init(strip="False")
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(colored(msg, "red")))


        # Send the messag
        message = "Hello from the teacher's server"
        # We must write bytes, not a string
        clientsocket.send(message.encode())
        clientsocket.close()

except Exception as e:
    print(e)

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()
