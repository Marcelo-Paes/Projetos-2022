with open("codigos.txt","r") as arquivo:
    codigos = arquivo.read()
codigos = codigos.split("\n")

print(codigos)