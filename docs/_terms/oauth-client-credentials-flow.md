---
title: "OAuth 2.0 Client Credentials Flow"
summary: "The OAuth grant type for service-to-service auth with no end user in the loop: a service authenticates directly with a client ID/secret (or a signed JWT assertion) to obtain an access token."
acronyms: []
aliases: ["Client credentials grant"]
tracks: [security]
domain: identity
cloud: neutral
level: practitioner
status: draft
---

## Explanation

The OAuth grant type for service-to-service auth with no end user in the
loop: a service authenticates directly with a client ID/secret (or a
signed JWT assertion) to obtain an access token. The usual choice for a
backend service calling another backend service or a third-party API.
