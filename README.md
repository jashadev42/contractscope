# ContractScope

A command-line tool that tracks U.S. federal contract awards for a watchlist of
defense and intelligence contractors, stores them, and surfaces spending trends —
which agencies fund whom, how award volume moves over time, and what work dominates.

Built on the public USASpending.gov API.

## How it works

ContractScope ingests federal contract awards for a configurable watchlist of
contractors, reshapes the raw API data into clean typed records, and persists them
to a local database for querying and analysis.

- **Concurrent ingestion** — fetches the entire watchlist in parallel using `asyncio`
  and `aiohttp`, so total fetch time stays close to a single request regardless of how
  many contractors are tracked. Raw API responses are cached to avoid redundant calls.
- **Persistence** — awards are stored in a SQLite database via SQLAlchemy, with
  idempotent upserts keyed on each award's unique identifier, so re-running ingestion
  refreshes data without creating duplicates.
- **Clean architecture** — a typed `Award` domain model and a translation layer isolate
  the messy external API from the rest of the app; a repository layer is the single
  point of database access.

## Components

- `contractscope.config` — loads the contractor watchlist.
- `contractscope.models` — the `Award` domain model.
- `contractscope.ingest.client` — `USASpendingClient`; sync and concurrent fetching.
- `contractscope.storage` — SQLAlchemy schema, engine/session setup, and the repository
  (save, load, and raw-SQL aggregate queries).

## Status

In active development. Current focus: spending analysis and reporting.