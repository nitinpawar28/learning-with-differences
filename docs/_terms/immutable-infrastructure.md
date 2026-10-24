---
title: "Immutable Infrastructure"
summary: "Provisioning servers/containers as artifacts that are never patched in place — a change means building and deploying a new image/instance, then discarding the old one, rather than SSH-ing in and running `apt upgrade`."
acronyms: []
aliases: []
tracks: [architect, cloud]
domain: devops
cloud: neutral
level: practitioner
status: draft
---

## Explanation

Provisioning servers/containers as artifacts that are never patched in
place — a change means building and deploying a new image/instance, then
discarding the old one, rather than SSH-ing in and running `apt upgrade`.
Removes an entire class of "works on my server, drifted from every other
server" bugs.
