#Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.C = 5 * ((F-32) / 9).

temp=float(input("DIGITE A TEMPERATURA EM GRAUS FAHRENHEIT: \n"))

grausc = (5 * (temp - 32)/9 )

print("\n",temp,"°F, FOI CONVERTIDO PARA, {:.2f}".format(grausc),"°C" )
