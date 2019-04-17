import requests
from bs4 import BeautifulSoup

g = requests.get('urlget')
print(g.cookies)
soup = BeautifulSoup(g.text, 'lxml')

token = soup.find("input", {"name": "__RequestVerificationToken"})["value"]

print(token)

r = requests.post("urlpost",
                  data={"__RequestVerificationToken": token, "Usuario": "desenv", "Password": "dev2017"})
print(r.cookies)
