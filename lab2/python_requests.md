# Challenge `Python requests` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Endpoint is vulnerable to brute-force attack_
- Where: Where is the vulnerability present
  - _`/more` endpoint_
- Impact: What results of exploiting this vulnerability
  - _Allows to match the game's target number by brute-force, solving the game and obtaining the flag_

## Steps to reproduce

1. Establish a session with the server visiting the `/hello` endpoint, getting session cookies
2. Request the `/more` endpoint until the current number matches the target number
3. Request the `/finish` endpoint to end the game and obtain the flag

The script to reproduce the challenge is available at
[python_requests.py](python_requests.py).
