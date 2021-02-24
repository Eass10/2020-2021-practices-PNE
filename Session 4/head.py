from pathlib import Path
#"RNU6_269P.txt"; "FRAT1.txt"; "U5.txt"; "ADA.txt"; "FXN.txt"
#with split could also be done
try:
    Filename = input("Introduce the name of your file: ")
    file_contents = Path(Filename).read_text()
    head = file_contents[:file_contents.index("\n")]
    head = head.replace("\n", "")
    print(head)
except FileNotFoundError:
    print("The file you have introduce cannot be found.")
