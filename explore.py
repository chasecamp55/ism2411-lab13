# ISM2411 Lab 13 - First DataFrame - Retail Sales Explorer
# Name: Chase Campbell

# SELF-ASSESSMENT

# 1. A boolean filter checks each row to see if it meets
# a condition. It only keeps the rows that match.

# 2. df["revenue"] returns a Series, which is one
# column of data. df[["revenue"]] returns a DataFrame,
# which keeps the data in a table format. This matters
# when using functions that require a DataFrame.

# 3. I would choose pandas over Excel because it makes
# working with large datasets faster and easier. I can
# filter, calculate, and organize data with a few lines
# of code instead of doing everything manually.

import pandas as pd

# EXERCISE 1 - Load the CSV
print("\nEXERCISE 1 - Load the CSV")

df = pd.read_csv("data/retail_sales.csv")

print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data types:")
print(df.dtypes)

# EXERCISE 2 - Filter by region
print("\nEXERCISE 2 - Filter by Region")

south = df[df["region"] == "South"]

print("South rows:", len(south))
print(south.head())

# EXERCISE 3 - Top 5 by revenue
print("\nEXERCISE 3 - Top 5 by Revenue")

top_five = df.sort_values(
    "revenue", ascending=False
).head(5)

print(top_five)

# EXERCISE 4 - Two-condition filter
print("\nEXERCISE 4 - Two-Condition Filter")

big_south = df[
    (df["region"] == "South") &
    (df["revenue"] > 1000)
]

print("Big South rows:", len(big_south))
print(big_south.head())

# EXERCISE 5 - Create a new column
print("\nEXERCISE 5 - New Column")

df["per_unit"] = df["revenue"] / df["quantity"]

print(df.head())
print("Mean per-unit price:", df["per_unit"].mean())

# EXERCISE 6 - Unique values
print("\nEXERCISE 6 - Unique Values")

print(df["region"].unique())
print(df["region"].value_counts())

# EXERCISE 7 - Select columns
print("\nEXERCISE 7 - Select Columns")

selected = df[["region", "product", "revenue"]]

print("Selected shape:", selected.shape)

# EXERCISE 8 - Save to CSV
print("\nEXERCISE 8 - Save CSV")

df.to_csv("data/explored.csv", index=False)

print("Saved data/explored.csv successfully!")