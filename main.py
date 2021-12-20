from bs4 import BeautifulSoup
import notify2
import requests
from requests import get
import time
import webbrowser

link = 'https://jkanime.net/'
anime = ''
notify2.init('A-notifier')
ep = ''
def linkObtainer(anime):
    lonk = anime.replace(' ', '-')
    lonk = lonk.replace('(', '')
    lonk = lonk.replace(')', '')
    lonk = lonk.lower()
    return lonk
def isItUp(anime):
    on = 0
    webp = requests.get('https://jkanime.net/')
    soup = BeautifulSoup(webp.text, 'html.parser')

    recent_ani = soup.find_all('div', class_ = 'anime__sidebar__comment__item__text')
    for div in recent_ani:
       if div.h5.text == anime:
            on = 1
    return on


while True:
    online = isItUp(anime)
    if online == 1:
        n = notify2.Notification("Hiii" ,
            anime + " is up on JKanime"
            )
        n.show()
        link = link + linkObtainer(anime)+'/'+ep+'/'
        webbrowser.open(link)
        break
    else:
        time.sleep(300)
