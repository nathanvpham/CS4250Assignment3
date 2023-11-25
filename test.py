from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import re

html = urlopen('https://www.cpp.edu/sci/computer-science/')
bs = BeautifulSoup(html.read(), 'html.parser')
currentURL = bs.find_all('a', href=True)

for link in currentURL:
    link = link.get('href')
    if link[0] == "/" or link[0:4] == "http":
        if link [0] == "/":
            link = "https://www.cpp.edu" + link
        print(link)
