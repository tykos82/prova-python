import sys
sys.path.insert(0, 'lib')
import urllib
#import HTMLParser

from bs4 import BeautifulSoup
url = 'https://www.frenf.it/earlyadopters/rss/AsiaOverland2002'
res = urllib.urlopen(url)
html = res.read()

soup = BeautifulSoup(html, 'xml')

giornata = soup.findAll('item')
#PROVE ENCODING un = HTMLParser.HTMLParser().unescape(soup)
#PROVE ENCODING print un
#PROVE ENCODING print('----------------------------------------------PAUSA---------------------------------')
#print(soup.prettify())

for ognigiornata in giornata:
  if ognigiornata.creator.string == 'orizzontintorno':
   # titolo = ognigiornata.string('title')
    print ognigiornata.title.string
    link = ognigiornata('link')
    print link
    timestamp = ognigiornata('date')
    print timestamp
