import os 

with open("codigos.txt", "r") as arquitvo:
    codigos = arquitvo.read()
codigos = str(codigos.split ("\n"))
os.system('cls')
print (codigos)

