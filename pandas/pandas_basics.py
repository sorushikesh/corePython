"""
Why Pandas?
- Powerful 2D data structure: **DataFrame**
- Ideal for data analysis, CSV/Excel I/O, APIs, transformations
"""

import pandas as pd

# Create Series and DataFrame
def create_basics():
    print("Create Series and DataFrame")

    s = pd.Series([10, 20, 30], index=["a", "b", "c"])
    print("Series:\n", s)

    data = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "city": ["Pune", "Mumbai", "Delhi"]
    }

    df = pd.DataFrame(data)
    print("DataFrame:\n", df)
    print("-" * 40)
    return df


# Indexing, Filtering, Sorting
def indexing_filtering(df):
    print("Indexing & Filtering")

    print("First row:\n", df.iloc[0])
    print("By label:\n", df.loc[0, "name"])
    print("Rows where age > 28:\n", df[df["age"] > 28])
    print("Sorted by age:\n", df.sort_values("age"))
    print("-" * 40)


# Add/Update/Delete Columns
def update_dataframe(df):
    print("Update DataFrame")

    df["salary"] = [50000, 60000, 70000]  # Add column
    df["age"] = df["age"] + 1             # Update column
    df.drop("city", axis=1, inplace=True) # Remove column

    print("Modified DataFrame:\n", df)
    print("-" * 40)
    return df


# Aggregations
def aggregation_demo(df):
    print("Aggregation")

    print("Mean age:", df["age"].mean())
    print("Total salary:", df["salary"].sum())
    print("Group by age:\n", df.groupby("age")["salary"].mean())
    print("-" * 40)


# CSV & Excel I/O
def io_demo():
    print("CSV / Excel I/O")

    data = {
        "product": ["Laptop", "Phone", "Tablet"],
        "price": [75000, 40000, 30000]
    }
    df = pd.DataFrame(data)

    df.to_csv("products.csv", index=False)
    df.to_excel("products.xlsx", index=False)

    print("CSV:\n", pd.read_csv("products.csv"))
    print("Excel:\n", pd.read_excel("products.xlsx"))
    print("-" * 40)


# ML Use Case: Read CSV, preprocess
def ml_pipeline_csv():
    print("ML Example: Clean data from CSV")

    df = pd.DataFrame({
        "feature1": [1, 2, None, 4],
        "feature2": [10, None, 30, 40],
        "label": ["A", "B", "A", "B"]
    })

    print("Original:\n", df)

    df.fillna(0, inplace=True)        # Fill NaNs
    df["feature1"] = df["feature1"] / df["feature1"].max()  # Normalize
    print("Processed:\n", df)
    print("-" * 40)


def main():
    """
    Run all Pandas basics
    """
    df = create_basics()
    indexing_filtering(df)
    df = update_dataframe(df)
    aggregation_demo(df)
    io_demo()
    ml_pipeline_csv()


if __name__ == "__main__":
    main()
