import urllib2
from bs4 import BeautifulSoup
link = "http://www.moneycontrol.com/india/stockpricequote/"
import json

page = urllib2.urlopen(link)
soup = BeautifulSoup(page,"lxml")
table = soup.find("table",{"class":"pcq_tbl"})
rows = table.findAll('tr')
m = 0;
#shareLinks = []
file = open("shareLinks.csv","w")
for tr in rows:
	cols = tr.findAll('td')
	for td in cols:
		a = td.find('a',href=True)
		file.write(str(a.find(text=True))+","+str(a['href'])+"\n")
		m+=1
#print shareLinks
print "shareLinks = ",m
