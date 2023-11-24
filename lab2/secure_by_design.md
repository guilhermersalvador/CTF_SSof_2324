# Challenge `Secure by design` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Cookie posioning_
- Where: Where is the vulnerability present
  - _`user` cookie_
- Impact: What results of exploiting this vulnerability
  - _Allows the login as administrator and the consequent access to the admin page_
- NOTE: the server uses POST requests sent using the login form to set the `user` cookie with the provided username enconded in base 64. However, it is important to note that the server has a protection that prevents logins with `admin` username since, if it is the case, the returned cookie corresponds to `fake-admin` encoded in base 64. Consequently, that cookie does not allow the access to the admin page.

## Steps to reproduce

1. Establish a connection with the server by requesting the `/` endpoint, getting session cookies
2. Poison the `user` cookie with the value `YWRtaW4K`, corresponding to the base 64 encoded value of `admin`
3. Request the `/` endpoint using the poisoned cookie to have direct access to the admin page

The script to reproduce the challenge is available at
[secure_by_design.py](secure_by_design.py)
