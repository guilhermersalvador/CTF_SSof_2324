import requests, re

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23053"

s = requests.Session()
s.get(link)

while True:
	response = s.get(link + "/more")
	target = int(response.text.split('<br>')[1].split()[-1])
	current = int(response.text.split('<br>')[2].split()[-1])
	if current == target:
		response = s.get(link + "/finish")
		print(re.findall("SSof{.*}", response.text)[0])
		exit(0)

