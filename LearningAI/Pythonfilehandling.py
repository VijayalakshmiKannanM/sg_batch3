file = open("notebook.txt", "r")
content=file.read()
print(content)

file=open("notes1.txt","w")
file.write("\n new lines added\n")
file.write("\n second line is added\n")
file.close()

# Pythonfilehandling.py

# Open the file notebook.txt for reading
with open("notebook.txt", "r") as file:
    content1 = file.read()
    print(content1)
