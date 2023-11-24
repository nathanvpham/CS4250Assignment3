from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
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

    while frontier:
        url = frontier.pop(0)
        visitedURL.append(url)
        html = urlopen(url)
        storePage(url, html)
        bs = BeautifulSoup(html.read(), 'html.parser')
        if bs.find_all('h1', text = re.compile('.*Permanent Faculty.*')):
            frontier = []
        currentURL = bs.find_all('a', href=True)
        print(currentURL)
        for link in currentURL:
            if link[0] == "/":
                link = "https://www.cpp.edu" + link
            elif link[0:4] != "https":
                link = "https://www.cpp.edu/sci/computer-science/" + link
            print(link)
            if link not in visitedURL or link not in frontier:
                frontier.append(link)

        
def storePage(url, html):
    return
        


if __name__ == "__main__":
    main()