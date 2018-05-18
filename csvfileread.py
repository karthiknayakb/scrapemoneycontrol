import csv
file = open("shareLinks.csv","rb")
reader = csv.reader(file)
c = 0
for r in reader:
	print r
	c+=1
	if c>=10:
		break