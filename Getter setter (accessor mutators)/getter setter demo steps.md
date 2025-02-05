# 🔹 Private Variables, Methods, and Getter/Setter Methods in Python

In Python, **private variables and methods** are not truly private but are indicated by **a single or double underscore (`_var` or `__var`)** as a convention.

---

## 🔹 When to Use Private Variables and Methods?
- **To prevent accidental modification** of critical data.
- **To encapsulate logic** inside a class.
- **To enforce data validation** using **getter and setter methods**.
- **For security reasons** (e.g., API keys, passwords).

---

## 🔹 Step-by-Step Explanation with a Real-World Scenario
Let's consider a **Bank Account Management System** where:
1. **Balance (`__balance`) should be private** so users cannot modify it directly.
2. **Getter (`get_balance()`) method** allows retrieving the balance.
3. **Setter (`set_balance()`) method** ensures balance updates **follow rules** (e.g., cannot be negative).
4. **A private method (`__update_transaction_history()`)** logs transactions internally.

---

### **📌 Step 1: Create a Class with Private Variables and Methods**
```python
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private variable

    # Private method (only used inside the class)
    def __update_transaction_history(self, amount, transaction_type):
        print(f"Transaction: {transaction_type} | Amount: {amount} | New Balance: {self.__balance}")

    # Getter method to access private balance
    def get_balance(self):
        return self.__balance

    # Setter method to modify private balance safely
    def set_balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = amount
            self.__update_transaction_history(amount, "Balance Update")

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__update_transaction_history(amount, "Deposit")
        else:
            print("Deposit amount must be positive!")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__update_transaction_history(amount, "Withdraw")
        else:
            print("Insufficient funds or invalid amount!")

# Creating an account
account = BankAccount("Alice", 1000)
```

---

### **📌 Step 2: Accessing and Modifying Private Variables Using Getters and Setters**
```python
print(account.get_balance())  # ✅ Accessing balance via getter

account.set_balance(2000)  # ✅ Updating balance safely using setter
print(account.get_balance())  # ✅ Checking updated balance

account.set_balance(-500)  # ❌ Attempting invalid balance update (Fails)
```
**🔹 Why use getters and setters?**
- Prevents direct access: `account.__balance = 5000` would be **invalid**.
- Ensures **validation** before updating balance.

---

### **📌 Step 3: Depositing and Withdrawing Money**
```python
account.deposit(500)   # ✅ Depositing money (Valid)
account.withdraw(300)  # ✅ Withdrawing money (Valid)

account.withdraw(5000) # ❌ Trying to withdraw more than balance (Fails)
```

---

## 🔹 Real-World Scenario: Why This Matters?
🔹 Suppose you are **developing a banking app**.  
- Without private variables, **anyone could modify the balance** like:
  ```python
  account.__balance = 999999  # 🚨 Security risk!
  ```
- With **private variables + getters/setters**, you **protect** data and enforce rules.

---

## 🔹 Summary
| Feature | Description |
|---------|------------|
| **Private Variable** | Defined with `__` (e.g., `__balance`). Cannot be accessed directly. |
| **Private Method** | Defined with `__`. Used internally in a class. |
| **Getter (`get_balance()`)** | Retrieves private variables safely. |
| **Setter (`set_balance(value)`)** | Updates private variables with validation. |

---

