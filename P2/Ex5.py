from Client0 import Client
from pathlib import Path
print("---|PRACTICE 2: EXERCISE 5|---")

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)
print(c.talk("Sending the U5 gene to the server..."))
print(c.talk(Path("./Sequences/U5.txt").read_text()))