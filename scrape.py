import requests
from bs4 import BeautifulSoup
import pprint

from requests.sessions import merge_cookies

response = requests.get("https://news.ycombinator.com/news")
response2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(response.text, "html.parser")
soup2 = BeautifulSoup(response2.text, "html.parser")

links = (soup.select('.titlelink'))
links2 = (soup.select('.titlelink'))
subtext = soup.select('.subtext')
subtext2 = soup.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


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


pprint.pprint(custom_hn(mega_links, mega_subtext))