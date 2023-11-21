import requests

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:22052"

# Create a session to persist the cookies between requests
s = requests.Session()

# Access the first link to set the user cookie
s.get(link)

ub = 100000
lb = 0
while ub > lb:
    i = (lb + ub)//2
    response = s.get(link + "/number/" + str(i))

    if ("Higher!" in response.text):
        lb = i
    elif ("Lower!" in response.text):
        ub = i
    else:
        print(response.text)
        break

