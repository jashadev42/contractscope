from contractscope.ingest.client import USASpendingClient
from contractscope.storage.db import init_db
from contractscope.storage.repo import save_awards, load_awards, total_by_recipient_raw

def main() -> None:
    init_db()
    client = USASpendingClient()
    awards = client.search_awards("Leidos", limit=5)
    save_awards(awards)
    
    loaded = load_awards()
    print(f"Loaded {len(loaded)} awards from the database")
    for award in loaded:
        print(f"{award.award_id} - {award.recipient_name}")

    print("\nTotal by recipient (raw SQL):")
    for name, total in total_by_recipient_raw():
        print(f"  {name}: ${total:,.2f}")

if __name__ == "__main__":
    main()