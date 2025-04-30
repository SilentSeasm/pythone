import urllib.request
url = "https://www.comuni-italiani.it/province.html"
response = urllib.request.urlopen(url)
theBytes = response.read()
text = theBytes.decode(encoding="iso-8859-1")

import bs4
doc = bs4.BeautifulSoup(text, features="html.parser")  
elems = doc.find_all("table")
table = elems[3]

province_data = []

for tr in table.contents[2:-2]:
    if type(tr) == bs4.element.Tag:
        tds = tr.contents
        sigl = tds[7].get_text()
        prov = tds[1].get_text()
        abitanti = int(tds[4].get_text().replace(".", ""))
        kmq_text = tds[5].get_text().replace(".", "").replace(",", ".")
        kmq = float(kmq_text)
        densita_tabella = float(tds[6].get_text().replace(".", "").replace(",", "."))
        densita_calcolata = abitanti / kmq 
        
        province_data.append((sigl, prov, abitanti, kmq, densita_calcolata))

province_data.sort(key=lambda x: (x[0], x[1], x[2], x[3]))

for sigl, prov, abitanti, kmq, densita in province_data:
    print(f"{sigl:3s} {prov:25s} {abitanti:10d} {kmq:10.2f} {densita:10.2f}")

if round(densita_calcolata, 2) != round(densita_tabella, 2):
            print(f"Discrepanza per {prov}: densità calcolata {densita_calcolata:.2f}, densità tabella {densita_tabella:.2f}")
          