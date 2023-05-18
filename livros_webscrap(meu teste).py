import csv
from requests import *
from bs4 import BeautifulSoup

def trocar_caracter(nome):

    acentos = {'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i', 'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o', 'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u', 'ç': 'c'}
    texto_sem_acentos = ''

    for caracter in nome:
        if caracter.lower() in acentos:
            texto_sem_acentos += acentos[caracter]

        else:
            texto_sem_acentos += caracter

    nome = texto_sem_acentos

    return nome

def verificação(nome):
    if nome_do_livro not in trocar_caracter(nome).lower():
        return AttributeError
    
def tratar_erro_nome(nome_erro):
    pass

def trocar_numero(numero):
    numero = numero.replace(',', '.')
    return numero

#input do nome do livro
nome_do_livro = input('Nome do livro: ')
nome_do_livro.lower()
lista_nome_do_livro = nome_do_livro.split(' ')
ler = len(lista_nome_do_livro)

url_porcentagem = ''
url_mais = ''

#Transformação do nome do livro nos padrões da url
for index in lista_nome_do_livro:
    if index == lista_nome_do_livro[ler - 1]:
        url_porcentagem += index
    else:
        url_porcentagem += index + '%20'

for index in lista_nome_do_livro:
    if index == lista_nome_do_livro[ler - 1]:
        url_mais += index
    else:
        url_mais += index + '+'

#URL

url = {
    'estante_virtual' :  f'https://www.estantevirtual.com.br/busca?q={url_porcentagem}',

    'livraria_cultura' : f'https://www3.livrariacultura.com.br/busca/?ft={url_porcentagem}&originalText={url_porcentagem}',

    'livraria_leitura' : f'https://leitura.com.br/index.php?route=product/search&search={url_porcentagem}',

    'livraria_da_vila' : f'https://www.livrariadavila.com.br/{url_porcentagem}'
}


'''ESTANTE VIRTUAL'''

pagina_estante_virtual = get(url['estante_virtual'])

sopa_estante_virtual = BeautifulSoup(pagina_estante_virtual.content, 'html.parser')

#TESTAR ERRO
try:
    
    try:

        nome_estante_virtual = sopa_estante_virtual.find('h2', {'itemprop' : 'name'}).get_text()

        preço_estante_virtual = sopa_estante_virtual.find('span', {'class': 'preco'}).get_text()

        link_estante_virtual = sopa_estante_virtual.find('div', {'class': 'ver-livros'})

        carrinho_estante_virtual = link_estante_virtual.find('a')

        #PRINTAR

        print('__________________________________________________________________________')


        print(f'\n___ESTANTE VIRUTAL___ \n')

        print(f'--nome-- \n{nome_estante_virtual.strip()} \n \n--preço-- \n{preço_estante_virtual} \n')

        print('url:', 'www.estantevirtual.com.br' + carrinho_estante_virtual.get('href'))


    except AttributeError:

        
        print('__________________________________________________________________________')

        print(f'Não se encontrou {nome_do_livro} na estante virtual.')

except NameError as nome_erro:
    tratar_erro_nome(nome_erro)


'''LIVRARIA CULTURA'''

pagina_livraria_cultura = get(url['livraria_cultura'])

sopa_livraria_cultura = BeautifulSoup(pagina_livraria_cultura.content, 'html.parser')

#TESTAR ERRO

try:

    try:

        nomes_livraria_cultura = sopa_livraria_cultura.find_all('h2')

        nome_livraria_cultura_2 = nomes_livraria_cultura[2]

        text_nome_livraria_cultura_2 = nome_livraria_cultura_2.get_text()

        verificação(text_nome_livraria_cultura_2)

        preço_livraria_cultura = sopa_livraria_cultura.find_all('span').get_text()

        preço_livraria_cultura_2 = preço_livraria_cultura[2].get_text()

        link_livraria_cultura = sopa_livraria_cultura.find('h2', {'class': 'prateleiraProduto__informacao__nome'})

        link_livraria_cultura = link_livraria_cultura

        carrinho_livraria_cultura = link_livraria_cultura.find('a')

        carrinho_livraria_cultura = carrinho_livraria_cultura

        #PRINTAR
        
        print('__________________________________________________________________________')

        print('\n___LIVRARIA CULTURA ___ \n')

        print(f'---Nome--- \n{nome_livraria_cultura_2.strip()} \n \n---Preço--- \n{preço_livraria_cultura_2} \n')
        
        print('url:', carrinho_livraria_cultura.get('href'))


    except AttributeError:

        print('__________________________________________________________________________')

        print('\n___LIVRARIA CULTURA ___ \n')

        print('--NÃO ENCONTRADO--')

except NameError as nome_erro:
    tratar_erro_nome(nome_erro)

'''LIVRARIA LEITURA'''

pagina_livraria_leitura = get(url['livraria_leitura'])

sopa_livraria_leitura = BeautifulSoup(pagina_livraria_leitura.content, 'html.parser')

try:

    try:

        nome_livraria_leitura = sopa_livraria_leitura.find('h4').get_text()

        #nome_livraria_leitura = verificação(nome_livraria_leitura)

        preço_livraria_leitura = sopa_livraria_leitura.find('span', {'class' : 'price-new'}).get_text()

        link_livraria_leitura = sopa_livraria_leitura.find('div', {'class' : 'caption'})

        carrinho_livraria_leitura = link_livraria_leitura.find('a')

        #SEPARADOR
        print('__________________________________________________________________________')

        #OUTPUT LIVRARIA LEITURA
        print('\n___LIVRARIA LEITURA___ \n')

        print(f'---Nome--- \n{nome_livraria_leitura} \n \n---Preço--- \n{preço_livraria_leitura} \n')

        print('url:', carrinho_livraria_leitura.get('href'))

    except AttributeError:

        print('__________________________________________________________________________')

        print('\n___LIVRARIA LEITURA___ \n')

        print('--NÃO ENCONTRADO--')

except NameError as nome_erro:
    tratar_erro_nome(nome_erro)

'''lIVRARIA DA VILA'''

pagina_livraria_da_vila = get(url['livraria_da_vila'])

sopa_livraria_da_vila = BeautifulSoup(pagina_livraria_da_vila.content, 'html.parser')

#TESTAR ERRO

try:

    try:

        nome_livraria_da_vila = sopa_livraria_da_vila.find('div', {'class':'prod-nome'}).get_text()

        verificação(nome_livraria_da_vila)

        preço_livraria_da_vila = sopa_livraria_da_vila.find('div', {'class':'price'}).get_text()

        link_livraria_da_vila = sopa_livraria_da_vila.find('div', {'class':'prod-nome'})

        carrinho_livraria_da_vila = link_livraria_da_vila.find('a')

        print('__________________________________________________________________________')

        #OUTPUT LIVRARIA DA VILA
        print('\n___LIVRARIA DA VILA___ \n')

        print(f'---Nome--- \n{nome_livraria_da_vila.strip()} \n \n---Preço--- \n{preço_livraria_da_vila.strip()} \n')

        print('url:', carrinho_livraria_da_vila.get('href'))

        print('__________________________________________________________________________')

    except AttributeError:

        print('__________________________________________________________________________')

        print('\n___LIVRARIA DA VILA___ \n')

        print('--NÃO ENCONTRADO--')

        print('__________________________________________________________________________')

except NameError as nome_erro:
    tratar_erro_nome(nome_erro)

'''PARTE CSV'''

#AJUSTE PREÇO

try:

    preço_estante_virtual = trocar_numero(preço_estante_virtual).strip()
    preço_livraria_cultura_2 = trocar_numero(preço_livraria_cultura_2).strip()
    preço_livraria_leitura = trocar_numero(preço_livraria_leitura).strip()
    preço_livraria_da_vila = trocar_numero(preço_livraria_da_vila).strip()

except NameError as nome_erro:
    tratar_erro_nome(nome_erro)

#AJUSTE NOME

try:

    nome_estante_virtual = trocar_caracter(nome_estante_virtual).strip().lower()
    text_nome_livraria_cultura_2 = trocar_caracter(text_nome_livraria_cultura_2).strip().lower()
    nome_livraria_leitura = trocar_caracter(nome_livraria_leitura).strip().lower()
    nome_livraria_da_vila = trocar_caracter(nome_livraria_da_vila).strip().lower()

except NameError as nome_erro:
    tratar_erro_nome(nome_erro)

try:
    with open('banco_csv.csv', 'a', newline='') as arquivo:
        escrever = csv.writer(arquivo)
        escrever.writerow([nome_estante_virtual, preço_estante_virtual, nome_livraria_cultura_2, preço_livraria_cultura_2, nome_livraria_leitura, preço_livraria_leitura, nome_livraria_da_vila, preço_livraria_da_vila])

except NameError as nome_erro:
    tratar_erro_nome(nome_erro)