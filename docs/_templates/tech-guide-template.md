---
title: "<Topic>: <Option A> vs <Option B>"
description: One-sentence summary of the trade-off this article covers.
tags:
  - template
  - <domain>
---

# \<Topic Name\>

!!! abstract "TL;DR"
    One or two sentences: what is being compared, and the short answer for
    "which should I use." A reader skimming only this box should walk away
    with the core takeaway.

## Conceptual Overview

What is this topic, and why does the difference matter in practice? Cover:

- The problem this concept/pattern exists to solve
- The core mental model (diagram, analogy, or minimal example)
- Where this shows up in a real system (link to related pages with `[[wikilinks]]`
  or standard Markdown links, e.g. see [Async & Threading](../messaging/async-threading.md))

## Key Architectural Differences

Break down *how* the options actually differ under the hood — not just "what
they're called." Aim for the differences that change your design decisions.

- **Difference 1** — what changes, and why it matters
- **Difference 2** — what changes, and why it matters
- **Difference 3** — what changes, and why it matters

!!! info "Underlying mechanism"
    Use this callout for a deeper implementation detail (e.g. how the runtime,
    protocol, or engine actually behaves) that explains *why* the trade-off exists.

## Comparative Matrix

| Dimension            | Option A            | Option B            |
|-----------------------|----------------------|----------------------|
| Latency                | e.g. Low             | e.g. Higher          |
| Throughput             |                      |                      |
| Complexity to operate  |                      |                      |
| Consistency guarantees |                      |                      |
| Scaling model          |                      |                      |
| Failure behavior       |                      |                      |
| Tooling / ecosystem    |                      |                      |
| Cost profile           |                      |                      |

## When to Use vs. When NOT to Use

=== "Use Option A when..."

    - Condition or requirement #1
    - Condition or requirement #2
    - Condition or requirement #3

=== "Use Option B when..."

    - Condition or requirement #1
    - Condition or requirement #2
    - Condition or requirement #3

!!! warning "Anti-pattern"
    Call out the most common *wrong* choice you've seen made here, and what it
    costs the team later (e.g. "reaching for microservices before you have a
    scaling or team-boundary problem to solve").

## Code / Implementation Examples

Use content tabs to show the same concept across the stack.

=== ".NET / C#"

    ```csharp title="Example.cs" linenums="1"
    public class Example
    {
        public async Task<int> DoWorkAsync(CancellationToken ct)
        {
            // Replace with a minimal, focused example of the concept above.
            await Task.Delay(100, ct);
            return 42;
        }
    }
    ```

=== "Angular / TypeScript"

    ```typescript title="example.component.ts" linenums="1"
    import { Component, OnInit } from '@angular/core';

    @Component({
      selector: 'app-example',
      template: `<p>{{ value$ | async }}</p>`,
    })
    export class ExampleComponent implements OnInit {
      // Replace with a minimal, focused example of the concept above.
      ngOnInit(): void {}
    }
    ```

=== "SQL"

    ```sql title="example.sql" linenums="1"
    -- Replace with a minimal, focused example of the concept above.
    SELECT column_a, column_b
    FROM example_table
    WHERE condition = 1;
    ```

## Performance Considerations

- **Throughput / latency impact** — measured or expected effect, with numbers
  where possible (benchmarks, load-test results, back-of-envelope math)
- **Resource cost** — CPU, memory, connection/thread pool pressure, I/O
- **Failure modes at scale** — what breaks first, and how it degrades
- **Benchmarking notes** — how to reproduce any numbers cited above

!!! tip "Rule of thumb"
    A short, memorable heuristic the reader can apply without re-reading the
    whole article next time this decision comes up.

## Further Reading

- Link to related internal pages
- Link to primary sources (official docs, RFCs, papers) — avoid blog-only sources
