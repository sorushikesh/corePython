"""
Covers:
- Merge / Join
- GroupBy + Aggregation
- Pivot Table
- Query-based filtering
- Datetime conversion + filtering
- Chained condition filtering
"""

import pandas as pd
from datetime import datetime

# Merge / Join
def merge_demo():
    print("Merge (like SQL JOIN)")

    users = pd.DataFrame({
        "user_id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"]
    })

    orders = pd.DataFrame({
        "order_id": [101, 102, 103],
        "user_id": [1, 2, 2],
        "amount": [250, 400, 600]
    })

    merged = pd.merge(users, orders, on="user_id", how="inner")
    print("Merged Data:\n", merged)
    print("-" * 40)


# GroupBy + Multiple Aggregations
def groupby_aggregation():
    print("GroupBy with Aggregation")

    df = pd.DataFrame({
        "category": ["A", "B", "A", "B", "C"],
        "value": [10, 20, 30, 40, 50]
    })

    agg = df.groupby("category").agg(
        total=("value", "sum"),
        avg=("value", "mean"),
        count=("value", "count")
    )
    print(agg)
    print("-" * 40)


# Pivot Table
def pivot_table_demo():
    print("Pivot Table")

    sales = pd.DataFrame({
        "region": ["West", "West", "East", "East", "South"],
        "product": ["A", "B", "A", "B", "A"],
        "amount": [100, 200, 150, 250, 300]
    })

    pivot = pd.pivot_table(sales, index="region", columns="product", values="amount", aggfunc="sum", fill_value=0)
    print(pivot)
    print("-" * 40)


# Query-based Filtering
def query_filter_demo():
    print("Filtering with query()")

    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 32, 29],
        "city": ["Pune", "Mumbai", "Delhi"]
    })

    filtered = df.query("age > 28 and city != 'Mumbai'")
    print("Filtered:\n", filtered)
    print("-" * 40)


# Date Handling & Filtering
def datetime_handling():
    print("Datetime Handling")

    df = pd.DataFrame({
        "event": ["Login", "Logout", "Payment", "Error"],
        "timestamp": ["2024-01-01 08:00", "2024-01-01 09:30", "2024-01-02 12:00", "2024-01-02 15:45"]
    })

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    filtered = df[df["timestamp"].dt.date == datetime(2024, 1, 1).date()]

    print("All Events:\n", df)
    print("Filtered (2024-01-01):\n", filtered)
    print("-" * 40)


# Chained Filtering with & and |
def chained_filtering():
    print("Chained Filtering with & and |")

    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "David"],
        "score": [85, 67, 92, 40],
        "passed": [True, True, True, False]
    })

    result = df[(df["score"] > 70) & (df["passed"])]
    print("Passed and scored > 70:\n", result)
    print("-" * 40)


def main():
    """
    Run all advanced pandas features
    """
    merge_demo()
    groupby_aggregation()
    pivot_table_demo()
    query_filter_demo()
    datetime_handling()
    chained_filtering()


if __name__ == "__main__":
    main()
