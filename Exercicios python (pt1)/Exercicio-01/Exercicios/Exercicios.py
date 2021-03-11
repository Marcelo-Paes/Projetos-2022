
#Faça um programa que peça as 4 notas bimestrais e mostre a média.

nota1=float(input("Digite a PRIMEIRA nota do aluno: \n"))
nota2=float(input("Digite a SEGUNDA nota do aluno: \n"))
nota3=float(input("Digite a TERCEIRA nota do aluno: \n"))
nota4=float(input("Digite a QUARTA nota do aluno: \n"))

nota=(nota1+nota2+nota3+nota4)/4

if nota>=6:
    print("MEDIA ",nota,"APROVADO!")
elif nota==10:
    print("MEDIA ",nota,"MUITO BEM, APROVADO!")

else:
    print("MEDIA ",nota,"REPROVADO!")