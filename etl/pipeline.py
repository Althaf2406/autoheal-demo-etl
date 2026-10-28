import os
import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """Load sales data from CSV."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    return pd.read_csv(filepath)


def calculate_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total revenue per transaction.
    BUG: Column name in CSV is 'price', but here it mistakenly accesses 'total_price'.
    """
    df["revenue"] = df["price"] * df["quantity"]
    return df


def aggregate_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total revenue by region."""
    return df.groupby("region")["revenue"].sum().reset_index()


def save_output(df: pd.DataFrame, output_path: str) -> None:
    """Save processed data to CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Output saved to {output_path}")


def main():
    print("Starting ETL pipeline...")
    input_file = "data/sales.csv"
    output_file = "output/revenue_by_region.csv"

    df = load_data(input_file)
    print(f"Loaded {len(df)} rows from {input_file}")

    df_with_revenue = calculate_revenue(df)
    summary = aggregate_by_region(df_with_revenue)

    save_output(summary, output_file)
    print("ETL pipeline completed successfully!")


if __name__ == "__main__":
    main()
