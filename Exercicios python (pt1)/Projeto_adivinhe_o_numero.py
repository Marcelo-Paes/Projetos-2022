import random


def menu():

    print("\nTente adivinha o numero entre 0 á 10: ")
    num=int(input(""))

    num2=random.randint(0,10)


    if num==num2:
   
        print("\n ACERTOU, o numero que eu estava pensado era: ",num2)
       
        
    else:
        print("\n\nTente novamente!")
        
        menu()
    
menu()



