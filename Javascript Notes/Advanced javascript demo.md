# **Real-World JavaScript Examples: `map()`, `filter()`, `find()`, and `reduce()`**

## **Scenario: E-commerce Product Management**
Imagine an **e-commerce application** where we need to process a list of products.

## **Sample Product List**
```javascript
const products = [
    { id: 1, name: "Laptop", price: 1200, category: "Electronics", stock: 10 },
    { id: 2, name: "Phone", price: 800, category: "Electronics", stock: 0 },
    { id: 3, name: "Shoes", price: 100, category: "Fashion", stock: 20 },
    { id: 4, name: "Notebook", price: 5, category: "Stationary", stock: 100 },
    { id: 5, name: "Smartwatch", price: 300, category: "Electronics", stock: 5 },
    { id: 6, name: "Pen", price: 2, category: "Stationary", stock: 200 }
];
```

---

## **1️⃣ Using `map()`: Display Product Names with Price**
### **Use Case:** Transform the product data to display only **name and price**.
```javascript
const productDisplay = products.map(product => `${product.name} - $${product.price}`);
console.log(productDisplay);
```

### **Output:**
```
["Laptop - $1200", "Phone - $800", "Shoes - $100", "Notebook - $5", "Smartwatch - $300", "Pen - $2"]
```

### **Explanation:**
- `map()` iterates over each product.
- It returns a new array containing formatted strings like `"Laptop - $1200"`.

---

## **2️⃣ Using `filter()`: Get Products by Category (User Input)**
### **Use Case:** Filter products based on user input.
```javascript
function getProductsByCategory(category) {
    return products.filter(product => product.category.toLowerCase() === category.toLowerCase());
}

const userCategory = "Electronics"; // User Input
const filteredProducts = getProductsByCategory(userCategory);
console.log(filteredProducts);
```

### **Output:**
```json
[
  { "id": 1, "name": "Laptop", "price": 1200, "category": "Electronics", "stock": 10 },
  { "id": 5, "name": "Smartwatch", "price": 300, "category": "Electronics", "stock": 5 }
]
```

### **Explanation:**
- `filter()` returns all products that match the user-inputted category.

---

## **3️⃣ Counting Items in a Category**
### **Use Case:** Calculate the number of items in a category.
```javascript
const countProductsByCategory = (category) => {
    return products.filter(product => product.category.toLowerCase() === category.toLowerCase()).length;
};

console.log(`Number of Electronics products: ${countProductsByCategory("Electronics")}`);
console.log(`Number of Stationary products: ${countProductsByCategory("Stationary")}`);
```

### **Output:**
```
Number of Electronics products: 2
Number of Stationary products: 2
```

---

## **4️⃣ Using `find()`: Find a Specific Product**
### **Use Case:** Retrieve details of a specific product by name.
```javascript
const findProductByName = (name) => {
    return products.find(product => product.name.toLowerCase() === name.toLowerCase());
};

console.log(findProductByName("Shoes"));
```

### **Output:**
```json
{ "id": 3, "name": "Shoes", "price": 100, "category": "Fashion", "stock": 20 }
```

---

## **5️⃣ Difference Between `filter()` and `find()`**
| Method   | Returns | Example | Use Case |
|----------|----------|----------|----------|
| `filter()` | **Array** of matching items | `[product1, product2]` | Get **all** matching products in a category |
| `find()` | **First** matching item | `{ id: 1, name: "Laptop" }` | Get **a single product** by name |

---

## **6️⃣ Using `reduce()`: Calculate Total Inventory Value**
### **Use Case:** Compute the **total value of available stock**.
```javascript
const totalInventoryValue = products.reduce((total, product) => {
    return total + (product.price * product.stock);
}, 0);

console.log(`Total Inventory Value: $${totalInventoryValue}`);
```

### **Output:**
```
Total Inventory Value: $16550
```

### **Explanation:**
- `reduce()` starts with `total = 0`.
- It loops through products, calculating `price * stock` and adds it to the total.

---

## **Conclusion**
| Method   | Use Case |
|----------|----------|
| `map()`  | Transform product data (e.g., format name & price). |
| `filter()` | Get all matching products in a category. |
| `find()` | Find a single product by name. |
| `reduce()` | Compute total inventory value. |

These **real-world JavaScript examples** show how to effectively use **map, filter, find, and reduce** for an e-commerce application.
