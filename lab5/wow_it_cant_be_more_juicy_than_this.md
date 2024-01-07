# Challenge `Wow, it cant be more juicy than this` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _SQL injection (SQLi)_

- Where: Where is the vulnerability present
  - _Blog post search form_

- Impact: What results of exploiting this vulnerability
    - _Allows to discover the name of the table containing the secret posts and query that table to obtain the flag_

NOTE: By inducing an error in the query, it is possible to obtain the full query string used to retrieve the blog posts. This query can be tampered with by injecting a UNION statement to query other tables in the database. More precisely, the UNION statement can be used to query the sqlite_master table, which contains the name of all the tables in the database. By querying this table, it is possible to discover the name of the table containing the secret posts and query that table to obtain the flag.

## Steps to reproduce

1. Access the vulnerable application homepage at `/` endpoint.

2. Inject the following payload in the search field of the blog search form: 
```sql
abc' UNION SELECT NULL, tbl_name, sql FROM sqlite_master -- 
```
obtaining the names of all the tables in the database as well as the query used to create them.

3. From the output of the previous query, it is can be extracted the name of the table containing the secret posts, which is `secret_blog_post`, and its structure, which is the same as the `blog_post` table. With this information, inject the following payload in the search field of the blog search form:
```sql
abc' UNION SELECT id, title, content FROM secret_blog_post --
```
obtaining the flag in the content field of the secret post.
