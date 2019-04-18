import requests
from bs4 import BeautifulSoup
import time

r = requests.post("https://station.rocketseat.com.br/api/sessions",
                  data={"email": "erik_senac@hotmail.com", "password": "0p9o8i7u"})
token = r.json()['token']
headers = {
    'Authorization': 'Bearer '+token
}

requests.get('https://station.rocketseat.com.br/api/account', headers=headers)

r_page_main = requests.get('https://station.rocketseat.com.br/dashboard')

time.sleep(5)
print(r_page_main.text)
