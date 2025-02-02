# people = [("Geetha", 38),("Alice", 30),('Veena',30), ("Bob", 25), ("Charlie", 35)]
# sorted_people = sorted(people, key=lambda person: person[1])

# print(sorted_people)

# employees =[
#     {"name": "Alice", "salary": 50000},
#     {"name": "Bob", "salary": 60000},
#     {"name": "Charlie", "salary": 40000},
#     {"name": "Fransy", "salary": 50000},
#     {"name": "Jey", "salary": 60000},
#     {"name": "Nikhil", "salary": 40000}
# ]

# sorted_employees=sorted(employees,\
#   key=lambda x: (x["salary"],x["name"]),reverse=True)
# Sort by salary (descending) and name (ascending)
# sorted_employees = sorted(
#     employees, 
#     key=lambda x: (x['salary'], x['name'])
# )
# for employee in sorted_employees:
#     print(f'{employee}')
# print(f'{sorted_employees}',"\n")

# example for filter
products = [
    {"name": "Product A", "price": 200, "category": "Electronics"},
    {"name": "Product B", "price": 50, "category": "Clothing"},
    {"name": "Product C", "price": 150, "category": "Electronics"},
    {"name": "Product D", "price": 300, "category": "Furniture"}
]

electronics=filter(lambda x:x['category']=='Electronics',products);
print('Electonics after filter')
for item in electronics:
    print(item)

electronics=filter(lambda x:x['category']=='Electronics',products);

sorted_electronics = sorted(electronics,key=lambda p: p["price"])
print(sorted_electronics.count)

print(f'\n Sorted Electronics')
for item in sorted_electronics:
    print(item)
product_info = map(lambda p: (p["name"], p["price"]), sorted_electronics)
print(f'\n mapped Electronics')
for item in product_info:
    L = ['abc', [(1, 2), ([3], 4)], 5]
    print(item)