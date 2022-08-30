from barcode import EAN14
import os
from numpy import loadtxt
from pathlib import Path
#Versão 1.0.3 - criando a propria pasta
#C:\Users\marce\OneDrive\Documentos\Arquivos teste
#C:\Users\marce\OneDrive\Área de Trabalho\Curso havard/
#1° Coloque o numeros (com 13 digitos) num arquivo .txt
#2° Rode o programa EAN13, os digitos verificados foram colocados POR HORA NO TERMINAL num arquivo .txt.

local_arq=input("Digite o nome do arquivo de coleta de dados: ")
local_arq_saida=input("Digite o nome do arquivo que vai salvar esses dados: ")

myfile = Path(f'Dum e ean13/{local_arq_saida}.txt')
myfile.touch(exist_ok=True)
f = open(myfile)


with open(f"{local_arq}.txt", "r") as tf:
    lines = tf.read().split(',')
    
os.system('cls')
lines = loadtxt(f"{local_arq}.txt", delimiter="-")
lines2=[str(line) for line in lines]
codigos=[]
for codigo in lines2:
    
    codigos.append(codigo)
    
  
    ean=EAN14(codigo)
    ean2= str(ean)
    print(ean2[0:13]+"-"+ean2[13])
    codigos.append(str(codigo))
    ean3= str(ean2)

    with open(f"Dum e ean13/{local_arq_saida}.txt","r+") as arquivo:
        lines2 = arquivo.read()    
            
        arquivo.write((ean3[0:13] +"-" + ean3[13:15])+"\n")
print("\n================================")
print(f"Arquivo criado: {local_arq_saida}.txt\n")

