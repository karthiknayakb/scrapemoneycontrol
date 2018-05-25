import urllib2
from bs4 import BeautifulSoup
#link1 = "http://www.moneycontrol.com/india/stockpricequote/cementmajor/acc/ACC06"
import time
import json
import csv

#headers
bseHead = ['bselow52','bsehigh52','bseCurrPrice','bseVolume','bseTdayLow','bseTdayHig','buyPercent','companyName']
nseHead = ['nselow52','nsehigh52','nseCurrPrice','nseVolume','nseTdayLow','nseTdayHig','buyPercent','companyName']

def getCurrBseNseDetails(link):
	#data
	bse = []
	nse = []
	page = urllib2.urlopen(link)
	soup = BeautifulSoup(page,"html.parser")
	#bse data
	#bselow52 = 
	bse.append(str(soup.find("span",{"id":"b_52low"}).find(text=True)))
	#bsehigh52 = 
	bse.append(str(soup.find("span",{"id":"b_52high"}).find(text=True)))
	#bseCuPr = 
	bse.append(str(soup.find("span",{"id":"Bse_Prc_tick"}).find(text=True)))
	#bseVolume = 
	bse.append(str(soup.find("span",{"id":"bse_volume"}).find(text=True)))
	#bseTdayLow = 
	bse.append(str(soup.find("span",{"id":"b_low_sh"}).find(text=True)))
	#bseTdayHig = 
	bse.append(str(soup.find("span",{"id":"b_high_sh"}).find(text=True)))

	#print bselow52,bsehigh52,bseCuPr,bseVolume,bseTdayLow,bseTdayHig

	#nse data
	#nselow52 = 
	nse.append(str(soup.find("span",{"id":"n_52low"}).find(text=True)))
	#nsehigh52 = 
	nse.append(str(soup.find("span",{"id":"n_52high"}).find(text=True)))
	#nseCuPr = 
	nse.append(str(soup.find("span",{"id":"Nse_Prc_tick"}).find(text=True)))
	#nseVolume = 
	nse.append(str(soup.find("span",{"id":"nse_volume"}).find(text=True)))
	#nseTdayLow = 
	nse.append(str(soup.find("span",{"id":"n_low_sh"}).find(text=True)))
	#nseTdayHig = 
	nse.append(str(soup.find("span",{"id":"n_high_sh"}).find(text=True)))

	#buyPercent = str(soup.find("span",{"class":"grnb_20"}).find(text=True).replace("%",""))
	buyPercent = soup.find("span",{"class":"grnb_20"})
	if buyPercent:
		buyPercent = str(buyPercent.find(text=True).replace("%",""))
	else:
		buyPercent = '0'
	#print nselow52,nsehigh52,nseCuPr,nseVolume,nseTdayLow,nseTdayHig
	bse.append(buyPercent)
	nse.append(buyPercent)

	companyName = str(soup.find("h1",{"class":"b_42 company_name"}).find(text=True)).replace(".","")
	bse.append(companyName)
	nse.append(companyName)
	return [bse,nse]

'''
code to get the links of all shares from csv goes here.
has to be stored in "shares" variable
'''
shares = []
csvfile = open("shareLinks.csv","rb")
reader = csv.reader(csvfile)
c = 0
for r in reader:
	shares.append(r[1])
	c+=1
	#if c>=10:
		#break
csvfile.close()

#print shares

# shares = ['http://www.moneycontrol.com/india/stockpricequote/diversified/3mindia/MI42',
# 'http://www.moneycontrol.com/india/stockpricequote/computerssoftware/8kmilessoftwareservices/PMS01',
# 'http://www.moneycontrol.com/india/stockpricequote/chemicals/aartiindustries/AI45',
# 'http://www.moneycontrol.com/india/stockpricequote/oildrillingandexploration/abanoffshore/AO04',
# 'http://www.moneycontrol.com/india/stockpricequote/infrastructuregeneral/abbindia/ABB',
# 'http://www.moneycontrol.com/india/stockpricequote/pharmaceuticals/abbottindia/AI51',
# 'http://www.moneycontrol.com/india/stockpricequote/cementmajor/acc/ACC06',
# 'http://www.moneycontrol.com/india/stockpricequote/trading/adanienterprises/AE13',
# 'http://www.moneycontrol.com/india/stockpricequote/infrastructuregeneral/adaniportsspecialeconomiczone/MPS',
# 'http://www.moneycontrol.com/india/stockpricequote/powergenerationdistribution/adanipower/AP11']

##############################
'''
retrives the data of individual share (BSE and NSE), stores in dictionary, stores in json file.
'''
import datetime
filename = str(datetime.datetime.now()).split()[0].replace("-","")+".json"
start_time = time.clock()
finalOut = {}
file = open(filename,"wb")
for i in shares:
	print i
	try:
		res = getCurrBseNseDetails(i)
		bseDic = {bseHead[0]:res[0][0],bseHead[1]:res[0][1],bseHead[2]:res[0][2],bseHead[3]:res[0][3],bseHead[4]:res[0][4],bseHead[5]:res[0][5],bseHead[6]:res[0][6],bseHead[7]:res[0][7]}
		nseDic = {nseHead[0]:res[1][0],nseHead[1]:res[1][1],nseHead[2]:res[1][2],nseHead[3]:res[1][3],nseHead[4]:res[1][4],nseHead[5]:res[1][5],nseHead[6]:res[1][6],nseHead[7]:res[1][7]}
		finalOut[res[0][7]] = [bseDic,nseDic]
	except:
		errorlog = open("errorlog.log","a")
		errorlog.write("exception occured for link "+i)
		errorlog.close()
json.dump(finalOut,file)
file.close()
print time.clock() - start_time, "seconds"

#print getCurrBseNseDetails('http://www.moneycontrol.com/india/stockpricequote/chemicals/aartiindustries/AI45')
# res = [['810.00', '1358.95', '1292.40', '565', '1292.05', '1307.00', '100', 'Aarti Industries Ltd.'], 
# ['810.00', '1360.00', '1291.05', '4,139', '1290.05', '1310.90','100', 'Aarti Industries Ltd.']]

# bseDic = {bseHead[0]:res[0][0],bseHead[1]:res[0][1],bseHead[2]:res[0][2],bseHead[3]:res[0][3],bseHead[4]:res[0][4],bseHead[5]:res[0][5],bseHead[6]:res[0][6],bseHead[7]:res[0][7]}
# nseDic = {nseHead[0]:res[1][0],nseHead[1]:res[1][1],nseHead[2]:res[1][2],nseHead[3]:res[1][3],nseHead[4]:res[1][4],nseHead[5]:res[1][5],nseHead[6]:res[1][6],nseHead[7]:res[1][7]}

# finalOut[res[0][7]] = [bseDic,nseDic]
# json.dump(finalOut,open("finalOut.json","wb"))
# print finalOut