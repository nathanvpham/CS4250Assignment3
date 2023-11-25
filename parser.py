from bs4 import BeautifulSoup
from pymongo import MongoClient
from urllib.request import urlopen
import re

html = urlopen('https://www.cpp.edu/sci/computer-science/faculty-and-staff/permanent-faculty.shtml')
bs = BeautifulSoup(html.read(), 'html.parser')
clearfix = bs.find_all('div', class_ = "clearfix")

print(clearfix)
