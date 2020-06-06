# WebScraper para o site do Hacker News
import requests
from bs4 import BeautifulSoup
import pprint

res     = requests.get('https://news.ycombinator.com/news')
soup    = BeautifulSoup(res.text, 'html.parser')
links   = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href  = item.get('href', None)
        vote  = subtext[idx].select('.score')
        # Se não existir o vote, o site não vai criar a classe chamada .score
        # Assim é testado se ele não está None com o IF abaixo
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title,
                            'link': href,
                           'votes': points
                          }
                        )
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))
