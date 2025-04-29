import requests
from bs4 import BeautifulSoup
import re

def trova_email(url):
    try:
        # Effettua la richiesta alla pagina web
        risposta = requests.get(url)
        if risposta.status_code != 200:
            print(f"❌ Errore HTTP {risposta.status_code} per {url}")
            return

        # Analizza il contenuto HTML
        soup = BeautifulSoup(risposta.text, 'html.parser')
        testo = soup.get_text()

        # Trova tutte le email nel testo con una regex
        email_trovate = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", testo)

        # Rimuove duplicati
        email_uniche = set(email_trovate)

        # Stampa il risultato
        if email_uniche:
            print("📧 Email trovate nella pagina:")
            for email in email_uniche:
                print("-", email)
        else:
            print("😕 Nessuna email trovata nella pagina.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Errore nella richiesta: {e}")

# === ESECUZIONE ===
url = input("Inserisci l'URL della pagina web (es. https://example.com): ")
trova_email(url)
