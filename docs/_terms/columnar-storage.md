---
title: "Columnar Storage"
summary: "Two ways to lay out a table on disk."
acronyms: []
aliases: ["Column-oriented storage", "Columnstore"]
tracks: [architect]
domain: databases
cloud: neutral
level: practitioner
status: draft
---

## Explanation

Two ways to lay out a table on disk. **Row-oriented** storage keeps all
columns of a record contiguous — fast for point lookups and writing/reading
whole rows (OLTP). **Columnar** storage keeps each column contiguous across
rows — fast for scanning/aggregating a few columns across many rows (OLAP),
and compresses better since values in a column are more similar to each
other than values in a row.

## Further reading

- [Row vs. Columnar Storage](../data/time-series/row-vs-columnar-storage.md)
