import requests
import time
from bs4 import BeautifulSoup

with requests.Session() as c:
    url = 'urlLoginPOST'
    USERNAME = 'admin'
    PASSWORD = '123'
    c.get(url)
    __RequestVerificationToken = c.cookies['__RequestVerificationToken']

    login_data = dict(__RequestVerificationToken=__RequestVerificationToken,
                      Ususario=USERNAME, Password=PASSWORD, next='/')

    c.post(url, data=login_data, headers={
           'Referer': 'URL_RAIZ',})

    page = c.get('URL_DE_ACESSO_AO_INDEX')

    soup = BeautifulSoup(page.text, 'lxml')
    titulo = soup.find('div', class_='nome-usuario').text
    c.close()
    print('Título da página é:', titulo)
    print('URL Atual é: ', page.url)
