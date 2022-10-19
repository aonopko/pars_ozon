import requests
from bs4 import BeautifulSoup

url = ""

headers ={
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0"
}

req = requests.get(url, headers=headers)
src = req.text


with open("index.html", 'w') as file:
    file.write(src)


