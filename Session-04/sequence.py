from pathlib import Path
Filename = "ADA.txt"
file_contents = Path(Filename).read_text()
body = file_contents[file_contents.index("\n") :].replace("\n", "")
print(len(body))