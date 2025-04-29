import requests
from bs4 import BeautifulSoup

url = 'https://lipsum.com'

risposta = requests.get(url)

parsed = BeautifulSoup(risposta.text, 'html.parser')

link_tags = parsed.find_all('a')

if risposta.status_code == 200:
    print("Link trovati nella pagina:")
    for tag in link_tags:
        if 'href' in tag.attrs: 
            print(tag['href'])
else:
    print("Errore nella richiesta:", risposta.status_code)
