import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David','Shankar','Aravind','Rajesh','uma','Rani','Mahathi'],
    'Age': [25, 30, 35, 40,21,34,24,27,None,34],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston','Chennai','Hyderabad','Mumbai','Pune','Pune','Mumbai']
}

df = pd.DataFrame(data)
# print(df)

#print(df.head())

# print(df.head(2))

# print(df)

df = pd.read_csv('customers-1000.csv')

#print(df.head())
# print(df.head(15))

# result=df.head(30)
# result.to_csv('output.csv', index=False)


#print(df['First Name'])

# print(df[['First Name', 'City']])

df = pd.read_csv('output.csv')
# df1=df.sort_values(by='First Name', ascending=False)
# print(df1[['Index','First Name']])

# result = df.groupby('City')['First Name'].count().reset_index()

# result.columns = ['City', 'Count']

# print(result)
# # Display the result
# result.to_csv("city_customer_count.csv", index=False)

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, None, 30, 28],
    'Salary': [50000, 60000, None, 45000]
}

df = pd.DataFrame(data)

print(df)
# Fill NaN with a specific value
df_filled = df.fillna({'Age': 27, 'Salary': 55000})

print(df_filled)