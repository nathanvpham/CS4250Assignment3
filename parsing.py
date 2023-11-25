from bs4 import BeautifulSoup
from pymongo import MongoClient
from urllib.request import urlopen
import re


def main():
    db = connectDataBase()
    collection = db.pages
    pipeline = [
    {
      "$match": {
        'url': 'https://www.cpp.edu/sci/computer-science/faculty-and-staff/permanent-faculty.shtml'
      }
    }
    ]
    query = collection.aggregate(pipeline)
    html = list(query)[0]["html"]
    collection = db.professors


    ## html = urlopen('https://www.cpp.edu/sci/computer-science/faculty-and-staff/permanent-faculty.shtml')
    ## bs = BeautifulSoup(html.read(), 'html.parser')
    
    bs = BeautifulSoup(html, 'html.parser')
    clearfix = bs.find_all('div', class_ = "clearfix")

    for div in clearfix:
        if div.h2:
            name = div.h2.text.strip()
        else:
            continue
        paragraph = re.sub('\s+',' ',div.p.text.strip()).split(": ")

        title = paragraph[1].replace(" Office", '').strip()
        office = paragraph[2].replace(" Phone", '').strip()
        email = paragraph[4].replace(" Web", '').strip()
        website = paragraph[5]        
        document = {
            "name": name,
            "title": title,
            "office": office,
            "email": email,
            "website": website
        }
        collection.insert_one(document)
    

    

def connectDataBase():
    # Create a database connection object using pymongo
    # --> add your Python code here
    DB_NAME = "facultydb"
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
