# Review Journal

The review surface for `watch-tool-watch-mark` is deliberately narrow: one fixture, one scoring rule, and one local check.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its cli tools focus without claiming live deployment or external usage.

## Cases

- `baseline`: `file span`, score 123, lane `watch`
- `stress`: `terminal width`, score 136, lane `watch`
- `edge`: `argument risk`, score 114, lane `watch`
- `recovery`: `report density`, score 177, lane `ship`
- `stale`: `file span`, score 241, lane `ship`

## Note

The repository should be understandable without pretending it is larger than it is.
