import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
#print(df)
#print(df.head(2))

# https://www.datablist.com/learn/csv/download-sample-csv-files

df = pd.read_csv('customers-1000.csv')
# print(df.head(10))
# df.to_csv('output.csv', index=False)
# df.to_csv('output.csv')

# df['First Name']
# print(df['First Name'])

# df[['First Name', 'City']]
# print(df[['First Name', 'City']])

# df1=df.sort_values(by='First Name', ascending=False)
# print(df1.head(10))

 #Group by City and count customers
result = df.groupby('City')['First Name'].count().reset_index()

# Rename column
result.columns = ['City', 'Count']

# Display the result
result.to_csv("city_customer_count.csv", index=False)

