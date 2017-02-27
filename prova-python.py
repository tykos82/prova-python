import sys
sys.path.insert(0, 'lib')
import urllib

from bs4 import BeautifulSoup
url = 'https://www.frenf.it/earlyadopters/rss/AsiaOverland2002'
res = urllib.urlopen(url)
html = res.read()

soup = BeautifulSoup(html, 'lxml')

giornata = soup.findAll('item')

for ognigiornata in giornata:
	titolo = item.title.text.strip()
	print titolo
	link = item.link.text.strip()
