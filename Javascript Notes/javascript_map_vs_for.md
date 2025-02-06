# **JavaScript: `map()` vs. `for` Loop Example**

## **Scenario: Display Product Names with Prices**
We have an **e-commerce product list**, and we need to transform it to display only **name and price**.

### **📌 Product List**
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

## **🔹 Approach 1: Without Using `map()` (Using `for` Loop)**
### **How it Works?**
- We use a `for` loop to iterate over the `products` array.
- We manually push each formatted product string into a new array.

### **Code:**
```javascript
let productDisplayWithoutMap = []; // Create an empty array

// Using for loop
for (let i = 0; i < products.length; i++) {
    let formattedProduct = \`\${products[i].name} - $\${products[i].price}\`;
    productDisplayWithoutMap.push(formattedProduct);
}

console.log("Without map():", productDisplayWithoutMap);
```

### **Output:**
```
Without map(): [ 'Laptop - $1200', 'Phone - $800', 'Shoes - $100', 'T-Shirt - $25', 'Smartwatch - $300' ]
```

### **Explanation:**
- We **initialize an empty array** `productDisplayWithoutMap`.
- We use a `for` loop to **iterate** through the `products` array.
- For each product, we **construct a formatted string**.
- We **push** the formatted string into `productDisplayWithoutMap`.

---

## **🔹 Approach 2: Using `map()` (Optimized Way)**
### **How it Works?**
- The `map()` method **automatically loops** through the `products` array.
- It **transforms each product** into a formatted string.
- It **returns a new array** with the transformed data.

### **Code:**
```javascript
const productDisplayWithMap = products.map(product => \`\${product.name} - $\${product.price}\`);
console.log("With map():", productDisplayWithMap);
```

### **Output:**
```
With map(): [ 'Laptop - $1200', 'Phone - $800', 'Shoes - $100', 'T-Shirt - $25', 'Smartwatch - $300' ]
```

### **Explanation:**
- `map()` **automatically iterates** over each item in the array.
- It **creates a new array** without modifying the original.
- The **callback function** returns a **formatted string** for each product.

---

## **🔹 Key Differences: `for` Loop vs. `map()`**
| Feature         | `for` Loop Approach  | `map()` Approach |
|---------------|------------------|----------------|
| **Code Length**  | Longer | Shorter |
| **Performance** | Manual iteration | Optimized for transformation |
| **Readability** | More code to achieve the result | Concise & easy to read |
| **Modification of Original Array** | Requires a new array to store results | Directly returns a new array |

---

## **🚀 Conclusion**
- **Using `map()` is the preferred approach** because it is cleaner, more readable, and optimized for transforming data.
- However, **if you need complex processing** or **need to modify the original array**, using a `for` loop might be better.

Would you like me to extend this to another real-world scenario? 🚀
