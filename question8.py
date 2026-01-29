import pandas as pd

# I used this dictionary as the data source for the DataFrame
data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

# I created the DataFrame using pandas
df = pd.DataFrame(data)

# I added a new column derived from existing columns
# Here, I multiplied column A by B and then added column C
df["D"] = df["A"] * df["B"] + df["C"]

# I printed the final DataFrame to verify the result
print(df)
