from barcode import EAN13
import os
from numpy import loadtxt
#Versão 1.0.2

#1° Coloque o numeros (com 13 digitos) num arquivo .txt
#2° Rode o programa EAN13, os digitos verificados foram colocados POR HORA NO TERMINAL num arquivo .txt.


with open("lista.txt", "r") as tf:
    lines = tf.read().split(',')
    
os.system('cls')
lines = loadtxt("lista.txt", delimiter="-")
lines2=[str(line) for line in lines]
codigos=[]
for codigo in lines2:
    codigos.append(codigo)
    
  
    ean=EAN13(codigo)
    ean2= str(ean)
    print(ean2[0:12]+"-"+ean2[12])






    

