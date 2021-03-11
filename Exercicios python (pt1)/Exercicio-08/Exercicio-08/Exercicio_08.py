#Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo.
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

num1=int(input("DIGITE O PRIMEIRO NUMERO INTEIRO:"))
num2=int(input("DIGITE O SEGUNDO NUMERO INTEIRO:"))

num3=float(input("\nDIGITE UM NUMERO REAL:"))

produto= (num1 * 2)+ (num2/2)

soma= (num1*3) + num3

cubo=pow(num3,3)

print("\nO PRODUTO DO DOBRO DO PRIMEIRO COM METADE DO SEGUNDO NUMERO É: ",produto)
print("\nA SOMA DO TRIPLO DO PRIMEIRO COM O TERCEIRO NUMERO É: ",soma)
print("\nO TERCEIRO NUMERO ELEVADO AO CUBO É: {:.2f}".format(cubo))