# import pandas as pd

# # Creating a DataFrame with missing values
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, None, 30, 28],
#     'Salary': [50000, 60000, None, 45000]
# }

# df = pd.DataFrame(data)

# print(df)
# # Fill NaN with a specific value
# df_filled = df.fillna({'Age': 27, 'Salary': 55000})

# print(df_filled)
# # Optionally, save the result to a CSV file
# #df_filled.to_csv("filled_dataframe.csv", index=False)


import pandas as pd

# Creating a DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', None, 'David'],
    'Age': [25, None, 30, None],
    'City': ['New York', None, 'Chicago', 'Los Angeles']
}

df = pd.DataFrame(data)

# Fill all NaN values with 'Unknown'
df_filled = df.fillna('Unknown')

# Display the modified DataFrame
print(df_filled)
