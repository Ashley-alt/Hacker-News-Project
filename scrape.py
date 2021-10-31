import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")
links = (soup.select('.titlelink'))
votes = soup.select('.score')

def custom_hn(links, votes):
    hn = []
    for inx, item in enumerate(links):
        title = links[inx].getText()
        hn.append(title)
    return hn


print(custom_hn(links, votes)) 