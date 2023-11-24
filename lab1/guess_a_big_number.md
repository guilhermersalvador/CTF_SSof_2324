# Challenge `Guess a big number` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Endpoint is vulnerable to brute-force attack_
- Where: Where is the vulnerability present
  - _`/number` endpoint_
- Impact: What results of exploiting this vulnerability
  - _Allows to find the server's guess by performing a binary search on the possible values_

## Steps to reproduce

1. Establish a connection with the server by requesting the `/` endpoint, getting session cookies;
2. Define an initial range of possible values for the server's guess (0-100000);
3. Request the `/number/{value}` endpoint using the middle value of the current range;
4. If the server's response contains `Higher!`, meaning that the server's guess is higher than the current value, update the lower bound of the range to the current value and go step 2. If the server's response contains `Lower!`, meaning that the server's guess is lower than the current value, update the upper bound of the range to the current value and go step 2. Otherwise, the server's guess is the current value and the flag is returned in the server's response.

The script to reproduce the challenge is available at
[guess_a_big_number.py](guess_a_big_number.py).
