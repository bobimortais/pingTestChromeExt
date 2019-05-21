import os
import json

def printPingTime(data, listPing):
	for linha in data:
		if("TTL" in linha):
			linhaParts = linha.split("time=")[1].split(" ")
			listPing.append(str(linhaParts[0]))
		elif("Request timed out" in linha):
			listPing.append("LP")
		elif("General failure" in linha):
			listPing.append("CC")

def getPing():		

	if(os.path.exists('ping.txt')):
		os.remove('ping.txt')
		
	os.system("ping google.com >> ping.txt")
	data = open('ping.txt')
	return data
	
def pingInfo():
	listFinalPing = []	
	for x in range(1, 2):
		data = getPing()	
		listFinalPing.append(printPingTime(data, listFinalPing))
		data.close()
		os.remove('ping.txt')
	response = str(listFinalPing).replace('ms', '')
	response = response.replace('[','')
	response = response.replace(']','')
	response = response.replace("'","")
	response = response.replace('None', '')
	response = response.replace(' ', '')
	print(response)
	return response
