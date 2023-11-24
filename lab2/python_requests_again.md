# Challenge `Python requests again` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Cookie poisoning_
- Where: Where is the vulnerability present
  - _`remaining_tries` cookie_
- Impact: What results of exploiting this vulnerability
  - _Allows to get unlimited tries to match the game's target number, allowing a brute-force attack to match the target number and obtain the flag_

## Steps to reproduce

1. Establish a session with the server visiting the `/hello` getting session cookies, including the `remaining_tries` cookie with a value of `1`
2. Request the `/more` endpoint poisoning the `remaining_tries` cookie with a value of `1`, since after the first request the cookie would be set to `0` by the server. Repeat the request until the current number matches the target number, always poisoning the `remaining_tries` cookie with a value of `1` to get unlimited tries
3. Request the `/finish` endpoint to end the game and obtain the flag

The script to reproduce the challenge is available at
[python_requests_again.py](python_requests_again.py).
