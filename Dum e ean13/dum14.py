from barcode import EAN14
import os

#1° Coloque o numeros (com 13 digitos) num arquivo .txt
#2° Use a Função do outro aquivo com o nome split para gerar uma lista no terminal.
#3° Copie a Lista do terminal e cole na Variavel codigos. 
#4° Rode o programa dum14, os digitos verificados foram colocados num arquivo .txt.
codigos=['1789645999038', '1789645999039', '1789645999040', '1789645999041', '1789645999042', '1789645999043', '1789645999044', '1789645999045', '1789645999046', '1789645999047', '1789645999048', '1789645999049', '1789645999050', '1789645999051']

os.system('cls')
for codigo in codigos:    
    ean=EAN14(codigo)
    ean2= str(ean)
    ler=print(ean2[0:13]+"-"+ean2[13])
    

    with open("codigos.txt","r+") as arquivo:
        codigos = arquivo.read()    
        
        arquivo.write((ean2[0:13] +"-" + ean2[13:15])+"\n")