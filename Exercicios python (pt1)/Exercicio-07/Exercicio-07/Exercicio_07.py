#Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temp=float(input("DIGITE A TEMPERATURA EM GRAUS CELSIUS: \n"))

grausf = (temp * 9/5)+32

print("\n",temp,"°C, FOI CONVERTIDO PARA, {:.1f}".format(grausf),"°F" )