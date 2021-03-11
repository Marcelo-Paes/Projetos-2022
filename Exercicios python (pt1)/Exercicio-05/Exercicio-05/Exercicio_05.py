#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salarioH=float(input("QUAL É O VALOR RECEBIDO POR HORA TRABALHADA:  "))
horasT=float(input("\nQUANTAS HORAS SÂO TRABALHADAS AO MÊS: "))

saldo=salarioH*horasT

print("SEU SALÀRIO É: {:.2f}".format(saldo),"$")


