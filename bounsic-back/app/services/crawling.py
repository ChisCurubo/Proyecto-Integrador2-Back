import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def crawler(url, visited=set()):
    if url in visited:
        return
    visited.add(url)

    try:
        # Descargar el contenido de la página
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraer y seguir enlaces
        for link in soup.find_all('a', href=True):
            full_url = urljoin(url, link['href'])
            print("Encontrado:", full_url)
            crawler(full_url, visited)  # Llamada recursiva
    except Exception as e:
        print(f"Error al acceder a {url}: {e}")


crawler("https://listado.mercadolibre.com.co/auriculares#D[A:auriculares]")