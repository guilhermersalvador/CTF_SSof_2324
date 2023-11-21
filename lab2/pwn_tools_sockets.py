from pwn import *
import re

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23055

s = remote(SERVER, PORT, timeout=9999)
s.recvline()
target = s.recvline().decode().split()[-1][:-1]

while True:
	current = s.recvuntil(b"H)?\n").decode().split()[2][:-1]
	if current == target:
		s.sendline(b"FINISH")
		response = s.recvline().decode()
		print(re.findall("SSof{.*}", response)[0])
		exit(0)
	else:
		s.sendline(b"MORE")
		s.recvline()

