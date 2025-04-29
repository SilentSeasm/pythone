import requests
from bs4 import BeautifulSoup

url = 'https://lipsum.com'  

risposta = requests.get(url)

soup = BeautifulSoup(risposta.text, 'html.parser')

link_tags = soup.find_all('a')

if risposta.status_code==200:
    print("Link trovati nella pagina:")
    for tag in link_tags:
        print(tag['href'])
else:
    print("Errore nella richiesta:", risposta.status_code)

