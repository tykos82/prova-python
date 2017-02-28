import sys
sys.path.insert(0, 'lib')
import urllib

from bs4 import BeautifulSoup
url = 'https://www.frenf.it/earlyadopters/rss/AsiaOverland2002'
res = urllib.urlopen(url)
html = res.read().decode('utf-8')

soup = BeautifulSoup(html, 'xml')

giornata = soup.findAll('item')

for ognigiornata in giornata:
	titolo = ognigiornata('title')
	print titolo
	link = ognigiornata('link')
	print link
