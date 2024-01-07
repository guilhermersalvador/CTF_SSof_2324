# Challenge `I will take care of this site` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _SQL injection (SQLi)_

- Where: Where is the vulnerability present
  - _Login form (/login endpoint)_

- Impact: What results of exploiting this vulnerability
    - _Allows to bypass the login form and login as an admin user by injecting crafted payloads in the username and password fields, making it possible to access the admin dashboard and retrieve the flag_

## Steps to reproduce

1. Access the vulnerable application at `/login` endpoint.

2. Inject the following payload in the username field of the login form: 
```sql
admin' -- 
```
and insert a random password, forcing the server to ignore the password verification and login as the admin user.

3. Access the user profile page at `/profile` endpoint and retrieve the flag.

