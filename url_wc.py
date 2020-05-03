import requests
import argparse
from bs4 import BeautifulSoup

myparser = argparse.ArgumentParser(description='web_W.C.')
myparser.add_argument("web", help="název stánky")
myparser.add_argument("--radky", help="výpis počtu řádků:", action="store_true")
myparser.add_argument("--slova", help="výpis počtu slov:", action="store_true")
myparser.add_argument("--znaky", help="výpis počtu znaků:", action="store_true")
arguments = myparser.parse_args()

url = arguments.web

r = requests.get("http://" + url)

data = r.text

soup = BeautifulSoup(data)

text = soup.text

try:
    if arguments.radky:
        text = text.read()
        pocet_radku = len(text.split('\n'))
        print(f"Počat řádků v textu: {pocet_radku}")
        flag = true

    if arguments.slova:
        text = text.read()
        pocet_slov = f.count(' ') + len(text.split('\n'))
        print(f"Počat slov v textu: {pocet_slov}")
        flag = true

    if arguments.znaky:
        text = text.read()
        pocet_znaku = len(text)
        print(f"Počat znaků v textu: {pocet_znaku}")
        flag = true

    if flag not true:
        print(f"Něco se pokazilo!")