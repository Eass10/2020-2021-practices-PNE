from Client0 import Client
from termcolor import cprint, colored
print("---|PRACTICE 2: EXERCISE 4|---")

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)
c.debug_talk("Message 1---")
c.debug_talk("Message 2: Testing !!!")