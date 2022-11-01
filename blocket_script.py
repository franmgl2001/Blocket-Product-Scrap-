from bs4 import BeautifulSoup
import requests

url = "https://www.blocket.se/annonser/hela_sverige/personligt/accessoarer_klockor/klockor?q=Gal"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.text)