# Challenge `Pwn tools sockets` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Server is vulnerable to brute-force attack_
- Where: Where is the vulnerability present
  - _`MORE` command_
- Impact: What results of exploiting this vulnerability
  - _Allows to match the game's target number by brute-forcing the command, solving the game and obtaining the flag_

## Steps to reproduce

1. Establish a socket connection with the server
2. Repeat the `MORE` command until the current number matches the target number
3. Use the `FINISH` command to obtain the flag

The script to reproduce the challenge is available at
[pwn_tools_sockets.py](pwn_tools_sockets.py).
