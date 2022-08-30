from cmath import pi
from ctypes.wintypes import FLOAT
import keyboard, time, sys
from threading import Thread
import os




#Parando a aplicação
a = {"value": 0}
def monitorKey():
    while True:
        if keyboard.is_pressed('esc'):
            os.system('cls')
            print('\nVocê pressionou a tecla para sair')
            a['value'] += 1 
            break  

def menu():
    os.system('cls')
    print("ESCOLHA UMA FUNÇÃO MATEMATICA A SER EXCULTADA:")
    print("[1] - ÁREA DE FIGURAS PLANAS")
    print("[2] - ADIÇÃO - SUBTRAÇÃO - MULTIPLICAÇÃO - DIVISÃO ")
    print("[3] - EQUAÇÃO DE PRIMEIRO GRAU")
    print("[ESC] - PARA SAIR","\n")
    op=input("DIGITE A OPÇÃO DESEJADA: ")
    match op:
        case '1':
            return area()
        case '2':
            return basica()
        case '3':
            return primeiro_grau()

#ÁREA DE FIGURAS PLANAS 
def area():
    os.system('cls')
    print("ÁREA DE FIGURAS PLANAS \n")
    print("ESCOLHA UMA FUNÇÃO MATEMATICA A SER EXCULTADA:")
    print("[1] - ÁREA DO RETÂNGULO")
    print("[2] - ÁREA DO QUADRADO")
    print("[3] - ÁREA DO LOSANGO")
    print("[4] - ÁREA DO TRAPÉZIO")
    print("[5] - ÁREA DO TRIAGULO")
    print("[6] - ÁREA DO CÍCULO")
    print("[ESC] - PARA SAIR","\n")
    op_area=input("DIGITE A OPÇÃO DESEJADA: ")
    match op_area:
        case '1':
            os.system("cls")  
            print("ÁREA DO RETÂNGULO")
            a =  int(input("VALOR DA BASE:"))
            h = int(input("VALOR DA ALTURA:"))
            total= a*h
            print("ÁREA DO RETÂNGULO = ",total)
            time.sleep(2)
            print("\n[1] - ENCONTRAR OUTRA ÁREA\n[2] - VOLTAR AO MENU \n[ESC] - PARA SAIR")
            op1=input("DIGITE A OPÇÃO DESEJADA: ")
            match op1:
                case '1':
                    area()
                case '2':
                    menu()
        case '2':
            os.system("cls")  
            print("ÁREA DO QUADRADO")
            l1 =  int(input("VALOR DO PRIMEIRO LADO:"))
            l2 = int(input("VALOR DO SEGUNDO LADO:"))
            total= l1*l2
            print("ÁREA DO QUADRADO = ",total)
            time.sleep(2)
            print("\n[1] - ENCONTRAR OUTRA ÁREA\n[2] - VOLTAR AO MENU \n[ESC] - PARA SAIR")
            op1=input("DIGITE A OPÇÃO DESEJADA: ")
            match op1:
                case '1':
                    area()
                case '2':
                    menu()
        case '3':
            os.system("cls")  
            print("ÁREA DO LOSANGO")
            l1 =  int(input("VALOR DA DIAGONAL MAIOR:"))
            l2 = int(input("VALOR DA DIAGONAL MENOR:"))
            total= (l1*l2)/2
            print("ÁREA DO LOSANGO = ",total)
            time.sleep(2)
            print("\n[1] - ENCONTRAR OUTRA ÁREA\n[2] - VOLTAR AO MENU \n[ESC] - PARA SAIR")
            op1=input("DIGITE A OPÇÃO DESEJADA: ")
            match op1:
                case '1':
                    area()
                case '2':
                    menu()
        case '4':
            os.system("cls")  
            print("ÁREA DO TRAPÉZIO")
            l1 =  int(input("VALOR DA DIAGONAL MAIOR:"))
            l2 = int(input("VALOR DA DIAGONAL MENOR:"))
            h= int(input("VALOR DA ALTURA:"))
            total= ((l1+l2)*h)/2
            print("ÁREA DO TRAPÉZIO = ",total)
            time.sleep(2)
            print("\n[1] - ENCONTRAR OUTRA ÁREA\n[2] - VOLTAR AO MENU \n[ESC] - PARA SAIR")
            op1=input("DIGITE A OPÇÃO DESEJADA: ")
            match op1:
                case '1':
                    area()
                case '2':
                    menu()

        case '5':
            os.system("cls")  
            print("ÁREA DO TRIAGULO")
            b =  int(input("VALOR DA BASE:"))
            h= int(input("VALOR DA ALTURA:"))
            total= (b*h)/2
            print("ÁREA DO TRIAGULO = ",total)
            time.sleep(2)
            print("\n[1] - ENCONTRAR OUTRA ÁREA\n[2] - VOLTAR AO MENU \n[ESC] - PARA SAIR")
            op1=input("DIGITE A OPÇÃO DESEJADA: ")
            match op1:
                case '1':
                    area()
                case '2':
                    menu()
        
        case '6':
            pi=3.14
            os.system("cls")  
            print("ÁREA DO CÍCULO")
            r =  int(input("VALOR Do RAIO:"))
            total= pi*(r**2)
            print(f'MONTAGEM DA FORMULA: {pi:.2f}*(%d^%d)'%(r,2))
            print("ÁREA DO CÍCULO = ",total)
            time.sleep(2)
            print("\n[1] - ENCONTRAR OUTRA ÁREA\n[2] - VOLTAR AO MENU \n[ESC] - PARA SAIR")
            op1=input("DIGITE A OPÇÃO DESEJADA: ")
            match op1:
                case '1':
                    area()
                case '2':
                    menu()




#ADIÇÃO - SUBTRAÇÃO - MULTIPLICAÇÃO - DIVISÃO
def basica():
    os.system('cls')
    print("ADIÇÃO - SUBTRAÇÃO - MULTIPLICAÇÃO - DIVISÃO\n")
    print("ESCOLHA UMA FUNÇÃO MATEMATICA A SER EXCULTADA:")
    print("[1] - ADIÇÃO")
    print("[2] - SUBTRAÇÃO")
    print("[3] - MULTIPLICAÇÃO")
    print("[4] - DIVISÃO")
    print("[ESC] - PARA SAIR","\n")
    op_area=input("DIGITE A OPÇÃO DESEJADA: ")
    match op_area:
        case '1':
            os.system("cls")  
            print("ADIÇÃO")
            qtd=  int(input("QUANTOS NUMEROS INTEIROS QUER SOMAR:"))
            tt_num = []
            total=0
            for count in range (qtd):
                os.system("cls")  
                num= int(input("%d° NUMERO: "%(count+1))) 
                tt_num.append(num)
                total= sum(tt_num)
            op2=int(input("VER TODOS OS NUMEROS DIGITADOS: [1] - SIM  [2] - NÃO: "))
            if op2==1:
                print("ESTES SÃO OS NUMEROS DIGITADOS: ",tt_num)
                time.sleep(3)
                print("A SOMA TOTAL = ",total)
            else:
                print("A SOMA TOTAL = ",total)                   
            
            time.sleep(2)
            print("\n[1] - FAZER OUTRA CONTA\n[2] - VOLTAR AO MENU \n[ESC] - PARA SAIR")
            op1=input("DIGITE A OPÇÃO DESEJADA: ")
            match op1:
                case '1':
                    basica()
                case '2':
                    menu()

#EQUAÇÃO DE PRIMEIRO GRAU
def primeiro_grau():
    os.system('cls')
    print("EQUAÇÃO DE PRIMEIRO GRAU")
    




        


                     
























Thread(target = monitorKey).start()     
menu()