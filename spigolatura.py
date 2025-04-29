#solo tag
import requests
from bs4 import BeautifulSoup
import bs4 

def scraping(tag, indentazione):
    print(indentazione + tag.name)  
    for i in tag.contents:
        if isinstance(i, bs4.element.Tag): 
            scraping(i, indentazione + '  ') 


url = 'https://lipsum.com'
risposta = requests.get(url)
soup = BeautifulSoup(risposta.text, 'html.parser')
scraping(soup, '')

#tutta la pagina
import requests
from bs4 import BeautifulSoup

url = 'https://lipsum.com'

risposta = requests.get(url)

soup = BeautifulSoup(risposta.text, 'html.parser')

print(soup.prettify())  
