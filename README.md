# ContractScope

A command-line tool that tracks U.S. federal contract awards for a watchlist of
defense and intelligence contractors, stores them, and surfaces spending trends —
which agencies fund whom, how award volume moves over time, and what work dominates.

Built on the public USASpending.gov API.

## How it works

ContractScope queries the USASpending `spending_by_award` endpoint for a given
recipient and reshapes the raw federal award data into clean, typed `Award`
records that the rest of the tool operates on.

- **`contractscope.models`** — the `Award` domain model: a typed representation of
  a single federal contract award.
- **`contractscope.ingest.client`** — `USASpendingClient`, which fetches awards for
  a recipient (with pagination support) and returns them as `Award` objects.

## Status
In active development.