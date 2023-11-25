from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from pymongo import MongoClient  
import re


def main():
    # try:
    #     html = urlopen('https://www.cpp.edu/sci/computer-science/')
    # except HTTPError as e:
    #     print(e)
    # except URLError as e:
    #     print('The server could not be found!')
    # else:
    #     print('It Worked!')

    # bs = BeautifulSoup(html.read(), 'html.parser')
    # print(bs)

    frontier = ['https://www.cpp.edu/sci/computer-science/']
    visitedURL = []
    db = connectDataBase()
    collection = db.documents

    while frontier:
        url = frontier.pop(0)
        visitedURL.append(url)
        try:
            html = urlopen(url)
        except:
            continue
        bs = BeautifulSoup(html.read(), 'html.parser')
        storePage(collection, url, bs.prettify())
        if bs.find_all('h1', text = re.compile('.*Permanent Faculty.*')):
            break
        currentURL = bs.find_all('a', href=True)
        if currentURL:
            for link in currentURL:
                link = link.get('href')
                if link[0] == "/" or link[0:4] == "http":
                    if link [0] == "/":
                        link = "https://www.cpp.edu" + link
                    if link not in visitedURL and link not in frontier:
                        frontier.append(link)

        
def storePage(collection, url, html):

    document = {
        "url": url,
        "html": html
    }
    
    collection.insert_one(document)
    return

def connectDataBase():

    # Create a database connection object using pymongo
    # --> add your Python code here
    DB_NAME = "pages"
    DB_HOST = "localhost"
    DB_PORT = 27017

    try:

        client = MongoClient(host=DB_HOST, port=DB_PORT)
        db = client[DB_NAME]
        print("Connected to MongoDB")

        return db

    except:
        print("Database not connected successfully")

        


if __name__ == "__main__":
    main()