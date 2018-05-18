import json

file = open("finalOut.json","r")
mydict = json.loads(file.read())
for i in mydict:
	print i
file.close()