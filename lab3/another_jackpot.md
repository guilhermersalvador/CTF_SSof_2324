# Challenge `Another jackpot` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Race condition (Time of check to time of use)_
- Where: Where is the vulnerability present
  - _`/jackpot` and `/login` endpoints_
- Impact: What results of exploiting this vulnerability
  - _Allows to claim the jackpot as administrator without a proper login in the admin account_
- NOTE: During the login process at the `/login` endpoint, committing the current session right after the login request, associating the provided username to the current session without validating the password. It is only after committing the session to the database that the server verifies if the given password is correct and if it is not, the session is revoked nullifying the username associated with it, committing the change to the database.
However, it leaves open a window of time between the first session commit and the password verification where the session is still associated with the user, allowing an attacker to claim the jackpot as administrator.

## Steps to reproduce

1. Establish a session with the server visiting the `/` endpoint, getting session cookies
2. Perform a POST request to the `/login` endpoint with `admin` as username and some arbitrary password. In parallel, perform a GET request to the `/jackpot` endpoint to claim the jackpot.
3. Repeat step 2 until the request to the `/jackpot` endpoint is successful, hitting the desired time window (i.e. when the current committed session is associated with the `admin` username because the password has not been yet verified by the server), returning the flag.

The script to reproduce the challenge is available at [another_jackpot.py](another_jackpot.py).