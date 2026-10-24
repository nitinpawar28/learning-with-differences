# Frontend & Real-Time UI

*Frontend Architecture & Real-Time UI*

## Domain Overview & Architectural Context

The frontend is where every backend decision either pays off or gets
exposed. A backend that streams ticks at high frequency is only as useful as
the UI's ability to render them without dropping frames, leaking
subscriptions, or falling behind the producer — this is the layer where
[backpressure](../glossary.md#backpressure) stops being a backend concern
and becomes a rendering one.

Angular 20 is the current stack: standalone components by default, and a
Signals-based reactivity model that's rapidly replacing Zone.js as the
mechanism deciding when the view actually needs to re-render. This category
tracks that transition deliberately — Signals vs. Zone.js/RxJS-heavy state
isn't a settled question yet across the ecosystem, and getting it wrong
either means fighting the framework or shipping change-detection overhead
that shows up as jank exactly when the data rate is highest.

## Key Terminology & Concepts

Full definitions in the [Master Glossary](../glossary.md); the ones specific
to this category:

- [Change Detection (Zone.js vs. Signals)](../glossary.md#change-detection-zonejs-vs-signals) —
  how Angular decides a view is stale
- [Backpressure](../glossary.md#backpressure) — handling a producer that
  outpaces the consumer's render loop
- [Cold vs. Hot Observable](../glossary.md#cold-vs-hot-observable) — whether
  subscribing late means missing data
- [Virtual Scrolling / Windowing](../glossary.md#virtual-scrolling-windowing) —
  keeping DOM node count bounded under a large, fast-changing list
- [Optimistic UI Update](../glossary.md#optimistic-ui-update) — updating
  before the server confirms, and what "undo" means when it's wrong
- [Hydration](../glossary.md#hydration) — attaching interactivity to
  already-rendered HTML

## Intended Knowledge Summary

By the time the articles in this folder are filled in, the reader should be
able to:

1. Choose Signals vs. Zone.js-driven change detection for a given component
   tree, and explain the actual re-render cost difference, not just cite
   "Signals are faster."
2. Pick the right RxJS operator (`switchMap` / `mergeMap` / `concatMap` /
   `exhaustMap`) for a given async interaction, and explain what goes wrong
   with each of the other three in that same scenario.
3. Decide when shared state belongs in a store (NgRx/Signals-based) vs. when
   component-local state is the more honest boundary.
4. Design a rendering strategy for high-frequency streamed data (throttling,
   virtual scrolling, `OnPush` + immutable updates) that stays responsive
   under a tick-rate spike instead of degrading gracefully into a frozen tab.
5. Reason in terms of TypeScript's structural type system deliberately,
   instead of accidentally relying on it.

## Planned Topic Matrix

| Topic | Current Stack | Candidate / Alternative | Key Trade-off | Article |
|---|---|---|---|---|
| Component architecture | Standalone components | NgModules | Simpler composition vs. established module boundaries | [Angular](angular-fundamentals.md) |
| Change detection & state | Signals | Zone.js + NgRx | Fine-grained reactivity vs. mature, battle-tested store ecosystem | [RxJS & State Management](rxjs-state-management.md) |
| Type system usage | Strict TypeScript, discriminated unions | Loosely-typed / `any`-heavy | Compile-time safety vs. short-term velocity | [TypeScript](typescript.md) |
| High-frequency rendering | Throttled streams + virtual scrolling + `OnPush` | Naive direct binding to a raw stream | Sustained responsiveness vs. simplicity of implementation | [Real-Time UI Streaming](real-time-ui-streaming.md) |
