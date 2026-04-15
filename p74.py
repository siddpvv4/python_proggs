#Pandas: Element-wise Power
import pandas as pd

data = {'X':[78,85,96,80,86],
        'Y':[84,94,89,83,86],
        'Z':[86,97,96,72,83]}

df = pd.DataFrame(data)

# Raise each element to the power of 2
power_df = df.pow(2)

print("Original DataFrame:\n", df)
print("After Power Operation:\n", power_df)