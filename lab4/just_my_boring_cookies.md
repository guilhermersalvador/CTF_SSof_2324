# Challenge `Just my boring cookies` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Cross-site scripting (XSS)_
- Where: Where is the vulnerability present
  - _Blog post search bar/search query parameter_
- Impact: What results of exploiting this vulnerability
  - _Allows to run arbitrary JavaScript code in the victim's browser by injecting crafted payloads in the search bar, making it possible to display the victim's cookies in the browser_

NOTE: The presented exploit does not constitute a compromising attack, since the cookies are only displayed in the victim's browser and do not leave the victim's machine.

## Steps to reproduce

1. Access the vulnerable application homepage at `/` endpoint.
2. Inject the following payload in the search bar: 
```html
<script>alert(document.cookie)</script>
```
Analogously, it is also possible to inject the payload in the `search` query parameter at the root endpoint (i.e. `/?search=<script>alert(document.cookie)</script>`).

3. Submit the search request and the payload will be executed in the victim's browser, displaying the victim's cookies in an alert box, containing the flag available at the cookie value of the `SECRET` cookie.