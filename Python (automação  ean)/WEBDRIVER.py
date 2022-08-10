
from selenium import webdriver
import time
from barcode import EAN14
import os


codigos=['1789645999069', '1789645999070'] 
new_cod=[]
os.system('cls')
for codigo in codigos:    
    ean=EAN14(codigo)
    print(ean,"\n")
    new_cod.append(ean)
    print(str(codigo[12]))
    print(str(codigo[12]))

    #with open("codigos.txt","r+") as arquivo:
        #codigos = arquivo.read()    
        #arquivo.write(str(ean[13],"-"))  
        #arquivo.write(str(ean)+"\n")
print(str(codigo[12]))








#navegador = webdriver.Chrome()
#time.sleep(4)
#navegador.get("https://www.gs1.org/services/check-digit-calculator")
#time.sleep(30)

#navegador.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()



#with open("codigos.txt","r") as arquivo:
    #codigos = arquivo.read()
#codigos = codigos.split("\n")

#print(codigos)

#num='1789645999035'

#numero = EAN14(num)
#print(numero)