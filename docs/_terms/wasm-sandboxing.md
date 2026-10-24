---
title: "WebAssembly Sandboxing"
summary: "Running untrusted code inside a WebAssembly runtime, which enforces memory safety and a deny-by-default capability model (via WASI) at the language-VM level rather than the OS-process level."
acronyms: []
aliases: ["Wasm sandboxing"]
tracks: [security, agentic-ai]
domain: appsec
cloud: neutral
level: expert
status: draft
---

## Explanation

Running untrusted code inside a WebAssembly runtime, which enforces memory
safety and a deny-by-default capability model (via WASI) at the language-VM
level rather than the OS-process level. Offers much faster cold starts and a
narrower escape surface than a container, at the cost of needing code that
targets a Wasm-compatible runtime.

## Further reading

- [Wasm Sandboxing vs. Container Isolation](../security/appsec/wasm-sandboxing.md)
