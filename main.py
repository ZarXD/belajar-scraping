from bs4 import BeautifulSoup as bs
import requests

res = requests.get("https://news.detik.com/index")
res.raise_for_status()
data = res.text

result = bs(data, "html.parser")

artikel = result.select(".container article h3 > a")
for artikelnya in artikel:
    print(artikelnya.text)
    print(artikelnya["href"])
    print("==================\n")
