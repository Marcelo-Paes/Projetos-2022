#Faça um programa que pergunte quanto você ganha por hora e o número de 
#horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para
# o sindicato, faça um programa que nos dê:

#- Salário Bruto : 
#- IR (11%) : 
#- INSS (8%) :
#- Sindicato (5%) : 
#- Salário Líquido : 
#Obs.: Salário Bruto - Descontos = Salário Líquido.


horat=float(input("GANHO POR HORA TRABALHADA: "))
horasTM=float(input("\nTOTAL DE HORAS TRABALHADAS NO MÊS: "))

salarioB=horat*horasTM

descontos=salarioB-(salarioB*0.11)

descontos=descontos-(descontos*0.08)

descontos=descontos-(descontos*0.05)

salarioL=salarioB-descontos

print("\nO SALARIO LÍQUIDO É DE: {:.2f}".format(descontos),"$\n TOTAL DE DESCONTOS É DE {:.2f}".format(salarioL),"$\n")







