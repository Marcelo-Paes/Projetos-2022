import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

'''Estudo de Webscraping, neste estudo estarei utilizando a plataforma glassdoor para a consulta de 20 salarios com a url de busca do cargo 
sugerido'''

def buscar_salarios_glassdoor(url_glassdoor):
    #Simulando que a requisição esta sendo feita por um navegador
    cabecalho = {'user-agent':'Mozilla/5.0'}

    #add o retorno de um url para a consulta
    resposta = requests.get(url_glassdoor, headers = cabecalho)
    #tranformando o html em txt para começar a selecionar onde fazer as buscas
    sopao_macarronico = resposta.text

    #Separar os elementos html mais ordenados
    sopa_bonita = BeautifulSoup(sopao_macarronico, 'html.parser')

    #Começando a buscar as requesições apartir de um find no elemento do html (procure sempre encotrar elesmentos com o mesmo padrão)
    lista_empresas = sopa_bonita.find_all('h3',
    {'data-test': re.compile('salaries-list-item-.*-employer-name')})
    #Começando a buscar as requesições apartir de um find no elemento do html (procure sempre encotrar elesmentos com o mesmo padrão)
    lista_salarios = sopa_bonita.find_all('div', {'data-test':re.compile('salaries-list-item-.*-salary-info')})

    #lista onde vai armazenar meus dados [nome:salario]
    lista_todos_salarios = []

    #compilando as informações com o zip e adicionando os elementos na lista 
    for empresa , salario in zip(lista_empresas, lista_salarios):
        nome_empresa = empresa.find('a').text

        str_salario = salario.contents[0].text
        str_salario = str_salario.replace('R$','').replace('\xa0','').replace('.','')

        lista_todos_salarios.append((nome_empresa, str_salario))

    
    #criando meu data frame no pandas colunas etc...
    df_salarios = pd.DataFrame(lista_todos_salarios, columns=['Empresa', 'Salario'])
    #convertendo meus valores numericos de STRING PARA FLOAT
    df_salarios['Salario'] = df_salarios['Salario'].astype(np.float32)

    #Armazena as informações num return
    return df_salarios


#chama a funação passando a URL desejada do glassdoor para a consulta de salarios e empresa
df_1 = buscar_salarios_glassdoor('https://www.glassdoor.com.br/Sal%C3%A1rios/analista-de-sistemas-sal%C3%A1rio-SRCH_KO0,20.htm')
print (df_1)