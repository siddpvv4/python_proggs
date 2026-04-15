#Handle Missing Values
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [10, 11, 12, 13]
})

print("Original Data:\n", df)

# Replace NaN with mean
df_filled = df.fillna(df.mean())

print("\nAfter replacing missing values:\n", df_filled)

# OR drop missing values
df_dropped = df.dropna()

print("\nAfter dropping missing values:\n", df_dropped)