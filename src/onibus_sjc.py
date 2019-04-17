# primeira aula
import requests
#import webbrowser
from bs4 import BeautifulSoup

url = 'http://servicos2.sjc.sp.gov.br/servicos/horario-e-itinerario.aspx?acao=p&opcao=0&txt=307'
#webbrowser.open(url)

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

lista_intinerarios = soup.findAll('table', class_='textosm')

url = 'http://servicos2.sjc.sp.gov.br'
for lista_td in lista_intinerarios:
    lista = lista_td.findAll('td')
    for lista_dados in lista:
        if lista_dados.next_element.name == 'a':
            url_it = '{0}{1}'.format(
                url, lista_dados.next_element.get('href'))
            print(url_it)
        else:
            print(lista_dados.next_element)
