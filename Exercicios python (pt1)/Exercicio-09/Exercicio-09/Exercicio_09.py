#Tendo como dado de entrada a altura (h) de uma pessoa e o seu sexo, 
#construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7


sexo=str(input('QUAL É O SEU SEXO: \n MASCULINO [M] | FEMININO [F]:\n '))
   

if sexo =='m':
    print("MASCULINO SELECIONADO...\n")
    altura=float(input("\nDIGITE SUA ALTURA: "))
    altura=altura*0.01
    masc=(72.7*altura)-58

    print("\nO PESO IDEAL PARA A ALTURA DE {:.2f}".format(altura),"m, É DE: {:.2f} ".format(masc),"KL, PARA O SEXO MASCULINO.")

elif sexo ==('f') : 
    print("FEMININO SELECIONADO...\n")
    altura=float(input("\nDIGITE SUA ALTURA: "))
    altura=altura*0.01
    fem=(62.1*altura) - 44.7 

    print("\nO PESO IDEAL PARA A ALTURA DE {:.2f}".format(altura),"m, É DE: {:.2f} ".format(fem),"KL, PARA O SEXO FEMININO.")

else:
    print("\nOpção invalida!!! \n Encerrando......")
    
