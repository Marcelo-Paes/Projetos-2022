import math
import time
import os
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = '\033[33m'


os.system('CLS')
def Menu():
    os.system('CLS')
    print("\n")
    print(RED+"#####################################")
    print("# CAIXAS / EMPILHAMENTO POR PALETES #")
    print("######################################"+RESET)
    print("\n")

    
    


    time.sleep(1)

    op=input("Inicar aplicação: \n SIM[1]\n NÃO[2] \n Escolha: ")
    if(op=='1'):
        Conta()
    else:
        print("Fechando aplicação")


def Conta():
    time.sleep(1)
    os.system('CLS')
    largura_palete=1000
    profundidade_palete=1200
    altura_palete=1300
    dica()

    nome_prod=(int(input("Digite o codigo do produto (pode ser sem o SKU): ")))
    print("\n")
    numero_pedido=(int(input("Digite a quantidade do pedido: ")))
    print("\n")
    caixas=int(input("Digite quantidade de peças que vai conter por cada caixa:"))
    print("\n")





    largura=int(input("\nDigite a Largura da caixa (mm): "))
    print("\n")
    altura=int(input("Digite a Altura da caixa (mm): "))
    print("\n")
    profundidade=int(input("Digite a Profundidade da caixa (mm): "))
    print("\n")

#primeiro modelo
    largura_base=math.floor(largura_palete/largura)

    altura_total=math.floor(altura_palete/altura)

    profundidade_base= math.floor(profundidade_palete/profundidade)

    total=math.floor(largura_base*profundidade_base)

    total_caixas=math.floor(total*altura_total)

    total_peças=math.floor(total_caixas*caixas)    

#segundo modelo
    largura_base1=math.floor(profundidade_palete/largura)

    profundidade_base1= math.floor(largura_palete/profundidade)

    total1=math.floor(largura_base1*profundidade_base1)

    total_caixas1=math.floor(total1*altura_total)

    total_peças1=math.floor(total_caixas1*caixas)  


#paletes de pedidos
    
    nosso_empilhamento = math.floor(numero_pedido/caixas)/(total)
    nosso_empilhamento = int(nosso_empilhamento)
    nossa_altura = math.floor(altura*nosso_empilhamento)+140
    tt_caixas_nosso = numero_pedido/caixas
#segundo palete
    







    os.system('CLS')
    Medida()
    print(RED+"\n# 1° MODELO - LARGURA x ALTURA x PROFUNDIDADE #\n"+RESET)
    print(RED+"▼ Composição do palete do ",nome_prod,": ▼\n"+RESET)
    print(BLUE+"Quantidade maxima de caixas empilhadas é de ",altura_total," caixas","(Com a Altura de ",(altura_total*altura)+140," mm incluindo o palete )","\n")


    print("Quantidade maxima de caixas no palete: ",total_caixas,"caixas","\n")

    
    print("Quantidade maxima peças no palete: ",total_peças," un","\n"+RESET)

    print(RED+"▲  Informações referentes a capacidade máxima do palete  ▲ "+RESET,"\n")
    input("Press Enter to continue...")
    print(GREEN+"____________________________________________________________________________________________________________________________________________________________________________________________________________________________"+RESET,"\n")
    #segundo modelo

    print(RED+"\n# 2° MODELO - PROFUNDIDADE x ALTURA x LARGURA #\n"+RESET)
    print(RED+"▼ Composição do palete do ",nome_prod,": ▼\n"+RESET)
    print(BLUE+"Quantidade maxima de caixas empilhadas é de ",altura_total," caixas","(Com a Altura de ",(altura_total*altura)+140," mm incluindo o palete )","\n")


    print("Quantidade maxima de caixas no palete: ",total_caixas1,"caixas","\n")

    
    print("Quantidade maxima peças no palete: ",total_peças1," un","\n"+RESET)

    print(RED+"▲  Informações referentes a capacidade máxima do palete  ▲ "+RESET,"\n")

    input("Press Enter to continue...")
    print(GREEN+"____________________________________________________________________________________________________________________________________________________________________________________________________________________________"+RESET,"\n")
    #terceiro modelo
    


    print(YELLOW+"\n# COMPOSIÇÃO DO PEDIDO #\n"+RESET)
    print(CYAN+"▼ Composição do palete do ",nome_prod,": ▼\n"+RESET)
    print(GREEN+"Quantidade de caixas empilhadas é de ",int(nosso_empilhamento)," caixas","(Com a Altura de ",nossa_altura," mm incluindo o palete)","\n")
    

    print("Total de caixas no palete: ",math.ceil(tt_caixas_nosso),"caixas","\n")

    
    print("Total de peças no palete: ",numero_pedido," un","\n"+RESET)

    print(CYAN+"▲  Informações da composição do palete do TOTAL com base no pedido  ▲ "+RESET,"\n")
    print(RED+"▲  ATENÇÃO: VERIFIQUE SE A QUANTIDADE DO PEDIDO NÃO EXCEDE A CAPACIDADE MÁXIMA DO PALETE!  ▲ "+RESET,"\n")
   





    print(GREEN+"____________________________________________________________________________________________________________________________________________________________________________________________________________________________"+RESET,"\n")

    

    time.sleep(3)
    input("Press Enter to continue...(ATENÇÂO TENHA CERTEZA QUE ANOTOU AS INFORMAÇÕES POIS SERÃO APAGADOS")
    os.system('CLS')
    op2=input("Execultar de novo? \n SIM[1]\n NÃO[2]\n Escolha: ")
    if (op2 =='1'):
        Conta()
    else:
        print("Finalizando aplicação.")
        time.sleep(2)



def dica():
    os.system('CLS')
    print("\n")
    print(BOLD+"###################")
    print("### MODO DE USO ###")
    print("###################"+RESET)
    print("\n")
    print(GREEN+"1° - Coloque as informações dimensionais das caixas em milímetros (mm).\n")
    print("2° - Preencha as informações utilizando apenas números.\n")
    
    print("3° - O sistema informará duas opções de carregamento do palete. Opte pelo maior carregamento.\n")
    
    print("4° - Anote as informações necessárias pois em seguida serão apagadas.\n"+RESET)
    

def Medida():
    print(CYAN+"MEDIDAS DO PALETE: \nLARGURA: 1000mm \nALTURA: 140mm \nPROFUNDIDADE: 1200mm\nALTURA MAXIMA PERMITIDA: 1300mm"+RESET)




Menu()