# src/etl.py
import pandas as pd

def load_data(path):
    """Load CSV dataset"""
    return pd.read_csv(path)

def transform_data(df):
    """Basic cleaning and feature engineering"""
    df = df.dropna()
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def save_data(df, output_path):
    """Save cleaned dataset"""
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    raw_path = "../data/sales.csv"   # placeholder
    out_path = "../data/cleaned_sales.csv"
    df = load_data(raw_path)
    df = transform_data(df)
    save_data(df, out_path)
    print("✅ ETL completed. Clean data saved!")
