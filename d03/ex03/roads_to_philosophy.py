import sys
import requests
from bs4 import BeautifulSoup

def wiki_request():
    if len(sys.argv) != 2:
        return print('wrong argument')
    title = '/wiki/' + sys.argv[1]
    road = ['/wiki/' + sys.argv[1]]
    while title != '/wiki/Philosophy':
        response = requests.get("http://en.wikipedia.org" + title)
        if not response or response.status_code != 200:
            return print("It's a dead end !")
        soup = BeautifulSoup(response.text, 'html.parser')
        req = None
        for p in soup.find_all('p'):
            for h in p.find_all('a', href=True):
                if '/wiki/' in h['href'] and not '/Help:' in h['href'] and not '/File:' in h['href']:
                    req = requests.get("http://en.wikipedia.org" + h['href'])
                    if req and req.status_code == 200:
                        title = h['href']
                        if title in road:
                            return print('It leads to an infinite loop !')
                        road.append(title)
                        break
            if req and req.status_code == 200:
                break
        if not req or req.status_code != 200:
            return print("It's a dead end !")
    for r in road:
        print(r.split('/wiki/')[1])
    print(f'{len(road)} roads from {sys.argv[1]} to philosophy !')

if __name__ == '__main__':
    wiki_request()