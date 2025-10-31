---
title: Why OIDC when there's OAuth?
date: Oct 31, 2025
tags:
    - web
    - standards
location: Bhaisepati, Lalitpur
---

One fine morning I was looking into how github actions can assume AWS roles to
be able to publish built images to ECS. Turns out AWS roles can use an
authentication mechanism called
[OIDC](https://openid.net/developers/how-connect-works/) to verify who is
assuming the role. I was curious and looked into OIDC to find out that it is an
"interoperable authentication protocol based on OAuth".
<br/>
<br/>
It shook my mental model about authentication and authorization.
OAuth, by name, is an authorization protocol and authorization
happens after authentication. Then came the question: *So why need a
authentication protocol when we already have an open authorization protocol?* I
too have used OAuth countless times to log-in user to applications.
<br/>
<br/>
After some digging and some conversations with Claude, I realized that the key
lies in each of the protocol was originally designed to solve.
<br/>
<br/>
I had overlooked the "interoperable" part of the OIDC definition and what
problems OAuth exists to solve. What's happening with all those OAuth based
logins was that, OAuth was being used for something it was not intended to. The
purpose of OAuth was to allow third-party apps limited access for limited time
to user's resources without actually sharing the password. Take for example,
`draw.io` accessing your Google Drive to store sketches. This misuse of access
token created security vulnerabilities and huge inconsistency across identity
providers because OAuth doesn't have standardized way to get user info. Even
the token is just an opaque string, subject to be interpreted in many ways by
many consumers.
<br/>
<br/>
With OIDC(the full form is Open ID Connect by the way ;)), authentication
finally became standardized and interoperable and OAuth could go back to do
what it was designed for: authorization.
