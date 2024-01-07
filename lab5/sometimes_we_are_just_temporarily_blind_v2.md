# Challenge `Sometimes we are just temporarily blind v2` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _SQL injection (SQLi)_

- Where: Where is the vulnerability present
  - _Blog post search form_

- Impact: What results of exploiting this vulnerability
    - _Allows to discover the name of the table containing the secret posts and query that table to obtain the flag_

NOTE: This challenge is similar to the challenge `Sometimes we are just temporarily blind` but requires a case sensitive flag. Since our solution for the previous challenge was case sensitive, it is also valid for this challenge, so this writeup is essentially the same as the previous one.

## Steps to reproduce

1. Access the vulnerable application homepage at `/` endpoint.

2. Inject the following payload in the search field of the blog search form: 
```sql
' AND UNICODE(SUBSTR((select tbl_name from sqlite_master limit 1 offset {offset}),{index},1)) >= {char} --  
```
infering if the unicode of the character at position `index` of row at offset `offset` is greater than or equal to `char`. If the condition is true, the number of posts matching the search query is greater than zero, otherwise it is zero.

3. Repeat step 2 for all offsets and indexes performing a binary search in order to discover all the characters in the name of the table containing the secret posts, and, consequently, discovering the name of all the tables in the database by obtaining one character at a time.

4. From the output of the previous query, retrieve the name of the table containing the secret posts, which is `super_s_sof_secrets`. Following a similar procedure as in steps 2 and 3, discover the name of the columns in the table by injecting the following payload in the search field of the blog search form:
```sql
' AND UNICODE(SUBSTR((select sql from sqlite_master where tbl_name='super_s_sof_secrets'),{index},1)) >= {char} --  "
```
to obtain the name of the columns in the table.

5. Afterward, retrieve the name of the column containing the content of the secret posts, which is `secret`. Following a similar procedure as in step 2 and 3, discover the content of the secret posts by injecting the following payload in the search field of the blog search form:
```sql
' AND UNICODE(SUBSTR((select secret from super_s_sof_secrets),{index},1)) >= {char} --  
```
to obtain the content of the secret post containing the flag.

The script to reproduce the challenge is available at [sometimes_we_are_just_temporarily_blind.py](sometimes_we_are_just_temporarily_blind.py)