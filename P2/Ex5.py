from Client0 import Client
from pathlib import Path
print("---|PRACTICE 2: EXERCISE 5|---")

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)
c.debug_talk("Sending the U5 gene to the server...")
c.debug_talk(Path("./Sequences/U5.txt").read_text())