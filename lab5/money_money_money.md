# Challenge `Money, money, money` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _SQL injection (SQLi)_

- Where: Where is the vulnerability present
  - _Profile update form - bio field (/profile endpoint)_

- Impact: What results of exploiting this vulnerability
    - _Allows to change the user's number of tokens by injecting crafted payloads in the bio field of the profile update form, making it possible to match the jackpot number and obtain the flag_

## Steps to reproduce

1. Register a random new user in the vulnerable application homepage at `/register` endpoint.

2. Login with the newly created user at `/login` endpoint.

3. Access the user profile page at `/profile` endpoint.

4. Inject the following payload in the bio field of the profile update form: 
```sql
', tokens='48841 
```
modifying the UPDATE query to set the user's number of tokens to the desired value. In this example, the number of tokens owned by the user is set to 48841.

5. Submit the form and obtain the flag provided by the jackpot.
