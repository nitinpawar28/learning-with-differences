---
title: "Transactional Outbox"
summary: "A reliability pattern that writes a domain state change and the event describing it in the *same local database transaction* (an 'outbox' table), then relays that event to the message broker asynchronously (via polling or CDC)."
acronyms: []
aliases: ["Outbox pattern"]
tracks: [architect]
domain: messaging
cloud: neutral
level: practitioner
status: draft
---

## Explanation

A reliability pattern that writes a domain state change and the event
describing it in the *same local database transaction* (an "outbox" table),
then relays that event to the message broker asynchronously (via polling or
CDC). This avoids the dual-write problem, where writing to the database and
publishing to the broker as two separate operations can partially fail and
leave state and events inconsistent.

## Further reading

- [Outbox Pattern](../messaging/eventing/outbox-pattern.md)
