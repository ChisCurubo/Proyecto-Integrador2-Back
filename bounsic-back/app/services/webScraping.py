import requests
from bs4 import BeautifulSoup

url = "https://listado.mercadolibre.com.co/auriculares#D[A:auriculares]"
response = requests.get(url)

response

soup = BeautifulSoup(response.text, 'html.parser')

soup


titulo = soup.title.text
print("Título de la página:", titulo)


enlaces = soup.find_all('a')
for enlace in enlaces:
    print(enlace.get('href'))