from contractscope.ingest.client import USASpendingClient

def main() -> None:
    client = USASpendingClient()
    awards = client.search_awards("leidos", limit=5)
    print(f"Got {len(awards)} awards")
    for award in awards:
        print(f"{award.award_id} - {award.recipient_name} - ${award.award_amount:,.0f}")

if __name__ == "__main__":
    main()