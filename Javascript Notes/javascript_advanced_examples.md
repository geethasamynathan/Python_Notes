# Real-World JavaScript Examples: `map()`, `filter()`, `find()`, and `reduce()`

## **Scenario: E-commerce Product Management**
Imagine an **e-commerce application** where we need to process a list of products.

### **Sample Product List**
```javascript
const products = [
    { id: 1, name: "Laptop", price: 1200, category: "Electronics", stock: 10 },
    { id: 2, name: "Phone", price: 800, category: "Electronics", stock: 0 },
    { id: 3, name: "Shoes", price: 100, category: "Fashion", stock: 20 },
    { id: 4, name: "T-Shirt", price: 25, category: "Fashion", stock: 50 },
    { id: 5, name: "Smartwatch", price: 300, category: "Electronics", stock: 5 }
];
```

---

## **1️⃣ Using `map()`: Display Product Names with Price**
### **Use Case:** Transforming the product data to display only **name and price**.
```javascript
const productDisplay = products.map(product => `${product.name} - $${product.price}`);
console.log(productDisplay);
```

### **Output:**
```
["Laptop - $1200", "Phone - $800", "Shoes - $100", "T-Shirt - $25", "Smartwatch - $300"]
```

### **Explanation:**
- `map()` iterates over each product.
- It returns a new array containing formatted strings like `"Laptop - $1200"`.

---

## **2️⃣ Using `filter()`: Get Products that are in Stock**
### **Use Case:** Find all products that are available for purchase.
```javascript
const availableProducts = products.filter(product => product.stock > 0);
console.log(availableProducts);
```

### **Output:**
```json
[
  { "id": 1, "name": "Laptop", "price": 1200, "category": "Electronics", "stock": 10 },
  { "id": 3, "name": "Shoes", "price": 100, "category": "Fashion", "stock": 20 },
  { "id": 4, "name": "T-Shirt", "price": 25, "category": "Fashion", "stock": 50 },
  { "id": 5, "name": "Smartwatch", "price": 300, "category": "Electronics", "stock": 5 }
]
```

### **Explanation:**
- `filter()` iterates over the `products` array.
- It checks if `stock > 0` (products in stock).
- Returns a new array of available products.

---

## **3️⃣ Using `find()`: Find a Product by Name**
### **Use Case:** Retrieve details of a product by name (e.g., "Shoes").
```javascript
const productFound = products.find(product => product.name === "Shoes");
console.log(productFound);
```

### **Output:**
```json
{ "id": 3, "name": "Shoes", "price": 100, "category": "Fashion", "stock": 20 }
```

### **Explanation:**
- `find()` searches for the **first** product where `name === "Shoes"`.
- It returns the **first matching product**.

---

## **4️⃣ Combining `map()`, `filter()`, and `find()`**
### **Use Case:** Get names of all **in-stock** **Electronics** products.
```javascript
const inStockElectronics = products
    .filter(product => product.category === "Electronics" && product.stock > 0)
    .map(product => product.name);

console.log(inStockElectronics);
```

### **Output:**
```json
["Laptop", "Smartwatch"]
```

### **Explanation:**
1. `filter()`: Filters only **Electronics** products that are **in stock**.
2. `map()`: Extracts **product names**.

---

## **5️⃣ Using `reduce()`: Calculate Total Inventory Value**
### **Use Case:** Compute the **total value of available stock**.
```javascript
const totalInventoryValue = products.reduce((total, product) => {
    return total + (product.price * product.stock);
}, 0);

console.log(`Total Inventory Value: $${totalInventoryValue}`);
```

### **Output:**
```
Total Inventory Value: $15850
```

### **Explanation:**
- `reduce()` starts with `total = 0`.
- It loops through products, calculating `price * stock` and adds it to the total.

---

## **Conclusion**
| Method   | Use Case |
|----------|----------|
| `map()`  | Transform product data (e.g., format name & price). |
| `filter()` | Get only available products (in stock). |
| `find()` | Find a product by a specific attribute (e.g., name). |
| `reduce()` | Compute total inventory value. |

These **real-world JavaScript examples** show how to effectively use **map, filter, find, and reduce** for an e-commerce application.
