import pandas as pd

# Creating a DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, None, 30, 28],
    'Salary': [50000, 60000, None, 45000]
}

df = pd.DataFrame(data)

# Drop rows with any NaN values
df_cleaned = df.dropna()

# Display the modified DataFrame
print(df_cleaned)
