from dataclasses import asdict
from .rank import canonical_recipient

import pandas as pd

from ..storage.repo import load_awards

def awards_dataframe() -> pd.DataFrame:
    awards = load_awards()
    rows = [asdict(award) for award in awards]
    return pd.DataFrame(rows)

def spend_by_agency() -> pd.DataFrame:
    df = awards_dataframe()
    result = (
        df.groupby("awarding_agency")["award_amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    return result

def top_recipient() -> pd.DataFrame:
    df = awards_dataframe()
    result = (
        df.groupby("recipient_name")["award_amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    return result

def spend_by_company() -> pd.DataFrame:
    df = awards_dataframe()
    df["company"] = df["recipient_name"].apply(canonical_recipient)
    result = (
        df.groupby("company")["award_amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    return result