# hero_profile = {
#     "name": "Vijay",
#     "age": 50,
#     "country": "India",
#     "occupation": "Actor"
# }

# print(hero_profile["name"])

# def dictEx1():
#     D = dict(name='Bob', age=40)
#     print(f'{D["name"]}')

# # dictEx1()

# def dictEx2():
#     keyslist = ['name', 'age', 'city']
#     valslist = ['Alice', 30, 'New York']

#     # Create a dictionary by zipping the two lists
#     D = dict(zip(keyslist, valslist))
#     print(D)


# dictEx2()

def dictFromKeys():
    D=dict.fromkeys('123',"n")
    coll = {'food': {'Banana': 1, 'egg': 2}}
    # print(D)
    print("Banana V")
    print(f'{coll['food']['Banana']}')
    #set Values
    D["age"]=10
    D["name"]="Raj"
    print(D)

    print ("Items from coll")
    collCopy =coll.copy()
    print(f'Collection Items ---- {coll.items()}')
    print(f'Collection Copy {collCopy}')

    for item in coll.items():
        print(f'{item[0]}')
# dictFromKeys()

print("**********************************************")

def DictItemsExample():
    # Sales data: Product and their sales in units
    sales_data = {
    "Laptops": 150,
    "Smartphones": 300,
    "Tablets": 120,
    "Headphones": 180
    }

# Display product sales and calculate total sales
    total_sales = 0
    print("Product Sales Report:")
    print("=======================")
    for product11, units_sold in sales_data.items():
        print(f"{product11}: {units_sold} units")
        total_sales += units_sold

    print("=======================")
    print(f"Total Sales: {total_sales} units")

DictItemsExample()

def getInput():
    d=input()
    g=input()
    return d,g

v,t=getInput()
print(v)
print(t)

