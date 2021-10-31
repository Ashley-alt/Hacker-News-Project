import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")
links = (soup.select('.titlelink'))
subtext = soup.select('.subtext')

def sort_stories(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)




def custom_hn(links, subtext):
    hn = []
    for inx, item in enumerate(links):
        title = links[inx].getText()
        href = links[inx].get("href", None)
        vote = subtext[inx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points',""))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories(hn)


pprint.pprint(custom_hn(links, subtext))