import requests
from bs4 import BeautifulSoup

d = requests.get('https://www.elcolombiano.com/')
soup = BeautifulSoup(d.text, "html.parser")

class_text = "noticia"

newL = [i.get_text() for i in soup.find_all(class_=class_text)]

print('\n'.join(newL))
