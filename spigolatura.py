import requests
from bs4 import BeautifulSoup
import bs4 

def scraping(tag, indentazione):
    print(indentazione + tag.name)  
    for i in tag.contents:
        if isinstance(i, bs4.element.Tag): 
            scraping(i, indentazione + '  ') 


url = 'https://lipsum.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
scraping(soup, '')

