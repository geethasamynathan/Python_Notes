# JavaScript Tutorial: From Basic to Advanced

## **Table of Contents**
1. Introduction to JavaScript
2. Variables and Data Types
3. Operators in JavaScript
4. Conditional Statements
5. Loops in JavaScript
6. Functions in JavaScript
7. Arrays and Objects
8. DOM Manipulation
9. Event Handling
10. Asynchronous JavaScript (Promises, Async/Await)
11. ES6 Features
12. JavaScript Modules
13. Working with APIs (Fetch API)
14. Error Handling and Debugging
15. JavaScript in the Backend (Node.js)
16. Real-World Example: To-Do App

---

## **Step 1: Introduction to JavaScript**
JavaScript is used for:
- **Client-side scripting** (in browsers)
- **Dynamic web pages** (DOM manipulation)
- **Backend development** (Node.js)
- **Asynchronous programming** (AJAX, Fetch API)

### **How to Run JavaScript?**
```html
<script>
    alert("Hello, JavaScript!");
</script>
```

---

## **Step 2: Variables and Data Types**
```js
var name = "John";  
let age = 25;       
const PI = 3.14;    

console.log(name, age, PI);
```

---

## **Step 3: Operators in JavaScript**
```js
let a = 10, b = 5;
console.log(a + b);  // Addition
console.log(a - b);  // Subtraction
console.log(a * b);  // Multiplication
console.log(a / b);  // Division
console.log(a % b);  // Modulus
```

---

## **Step 4: Conditional Statements**
```js
let age = 18;
if (age >= 18) {
    console.log("You are an adult.");
} else {
    console.log("You are a minor.");
}
```

---

## **Step 5: Loops in JavaScript**
```js
for (let i = 0; i < 5; i++) {
    console.log("Iteration:", i);
}
```

---

## **Step 6: Functions in JavaScript**
```js
function greet(name) {
    return "Hello, " + name;
}
console.log(greet("Alice"));
```

---

## **Step 7: Arrays and Objects**
```js
let fruits = ["Apple", "Banana", "Cherry"];
console.log(fruits[1]); // Banana
fruits.push("Mango");
console.log(fruits);
```

```js
let person = {
    name: "John",
    age: 30
};
console.log(person.name); // John
```

---

## **Step 8: DOM Manipulation**
```js
document.getElementById("demo").innerText = "Hello, DOM!";
```

---

## **Step 9: Event Handling**
```js
document.getElementById("btn").addEventListener("click", function() {
    alert("Button clicked!");
});
```

---

## **Step 10: Asynchronous JavaScript**
```js
async function fetchData() {
    let response = await fetch("https://jsonplaceholder.typicode.com/posts/1");
    let data = await response.json();
    console.log(data);
}
fetchData();
```

---

## **Step 11: ES6 Features**
```js
let arr1 = [1, 2, 3];
let arr2 = [...arr1, 4, 5];
console.log(arr2);
```

---

## **Step 12: Working with APIs**
```js
fetch("https://jsonplaceholder.typicode.com/posts")
    .then(response => response.json())
    .then(data => console.log(data));
```

---

## **Step 13: Real-World Example: To-Do App**
```html
<!DOCTYPE html>
<html>
<body>
    <input type="text" id="taskInput" placeholder="Enter task">
    <button onclick="addTask()">Add Task</button>
    <ul id="taskList"></ul>

    <script>
        function addTask() {
            let input = document.getElementById("taskInput").value;
            let li = document.createElement("li");
            li.innerText = input;
            document.getElementById("taskList").appendChild(li);
        }
    </script>
</body>
</html>
```

---

## **Conclusion**
- JavaScript is a **powerful and versatile language** for web development.
- It supports **front-end, back-end, and full-stack development**.
- Advanced features like **ES6, APIs, Async programming, and Node.js** make it scalable.

---

Would you like to explore **advanced projects** using JavaScript? 🚀
