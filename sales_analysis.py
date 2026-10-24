"""CodeOrbit Task 2: Sales Data Analysis
Uses a small illustrative sample dataset. Replace it with the official task dataset if provided.
Run: python sales_analysis.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path("sales_dataset.csv")
OUTPUT_FILE = Path("sales_analysis_output.csv")
CHART_FILE = Path("revenue_by_product.png")


def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Could not find {DATA_FILE}. Keep it in the same folder as this script."
        )

    df = pd.read_csv(DATA_FILE)
    required = ["Order_ID", "Date", "Product", "Category", "Quantity",
                "Unit_Price", "Region", "Revenue"]
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing required columns: {missing}")

    initial_rows = len(df)
    df = df.drop_duplicates()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    for col in ["Quantity", "Unit_Price", "Revenue"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["Order_ID", "Date", "Product", "Quantity", "Unit_Price", "Region"])
    df = df[(df["Quantity"] > 0) & (df["Unit_Price"] >= 0)]
    # Calculate revenue from quantity and unit price to ensure consistency.
    df["Revenue"] = df["Quantity"] * df["Unit_Price"]
    df["Product"] = df["Product"].astype(str).str.strip()
    df["Category"] = df["Category"].fillna("Unknown").astype(str).str.strip()
    df["Region"] = df["Region"].astype(str).str.strip()
    df.to_csv(OUTPUT_FILE, index=False, date_format="%Y-%m-%d")

    if df.empty:
        print("No valid rows remain after cleaning.")
        return

    total_orders = df["Order_ID"].nunique()
    total_units = int(df["Quantity"].sum())
    total_revenue = df["Revenue"].sum()
    average_order_revenue = df.groupby("Order_ID")["Revenue"].sum().mean()
    product_revenue = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
    region_revenue = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

    print("=== Sales Analysis Summary ===")
    print(f"Rows before cleaning: {initial_rows}")
    print(f"Rows after cleaning:  {len(df)}")
    print(f"Duplicate rows removed: {initial_rows - len(df)} (includes any rows dropped during cleaning)")
    print(f"Unique orders: {total_orders}")
    print(f"Units sold: {total_units}")
    print(f"Total revenue: Rs. {total_revenue:,.2f}")
    print(f"Average revenue per order: Rs. {average_order_revenue:,.2f}")
    print("\nRevenue by product:")
    print(product_revenue.to_string())
    print("\nRevenue by region:")
    print(region_revenue.to_string())

    ax = product_revenue.plot(kind="bar", figsize=(8, 5), title="Revenue by Product")
    ax.set_xlabel("Product")
    ax.set_ylabel("Revenue (Rs.)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=150)
    plt.close()
    print(f"\nCleaned data saved to: {OUTPUT_FILE}")
    print(f"Chart saved to: {CHART_FILE}")


if __name__ == "__main__":
    main()
