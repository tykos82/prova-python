from bs4 import BeautifulSoup
url = 'https://www.frenf.it/earlyadopters/rss/AsiaOverland2002'
soup = Beautifulsoup(url, 'xml')

giornata = soup.findAll('item')

for ognigiornata in giornata:
	titolo = item.title.text.strip()
	print titolo
	link = item.link.text.strip()