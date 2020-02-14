"""
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.nytimes.com/')
cont = page.content

soup = BeautifulSoup(cont, "html.parser")

list1 = soup.find_all(class_="esl82me1")

for i in list1:
    print(i.text)
    print(len(list1))
"""
import requests
from bs4 import BeautifulSoup

d = requests.get('https://www.elcolombiano.com/')
soup = BeautifulSoup(d.text, "html.parser")

class_text = "noticia"

newL = [i.get_text() for i in soup.find_all(class_=class_text)]

print('\n'.join(newL))
