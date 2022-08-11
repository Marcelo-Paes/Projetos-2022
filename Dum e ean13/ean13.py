from barcode import EAN13
import os

#1° Coloque o numeros (com 12 digitos) num arquivo .txt
#2° Use a Função do outro aquivo com o nome split para gerar uma lista no terminal.
#3° Copie a Lista do terminal e cole na Variavel codigos. 
#4° Rode o programa dum14, os digitos verificados foram colocados num arquivo .txt.
codigos=['178964599903', '178964599904', '178964599905']

os.system('cls')
for codigo in codigos:    
    ean=EAN13(codigo)
    ean2= str(ean)
    ler=print(ean2[0:11]+"-"+ean2[12])
    

    with open("codigos.txt","r+") as arquivo:
        codigos = arquivo.read()    
        
        arquivo.write((ean2[0:12] +"-" + ean2[12:14])+"\n")