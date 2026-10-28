import pandas as pd
import pytest
from etl.pipeline import calculate_revenue, aggregate_by_region


def test_calculate_revenue():
    df = pd.DataFrame({
        "region": ["North"],
        "price": [10.0],
        "quantity": [5]
    })
    result = calculate_revenue(df)
    assert "revenue" in result.columns
    assert result["revenue"].iloc[0] == 50.0


def test_aggregate_by_region():
    df = pd.DataFrame({
        "region": ["North", "North", "South"],
        "revenue": [50.0, 50.0, 30.0]
    })
    result = aggregate_by_region(df)
    assert len(result) == 2
