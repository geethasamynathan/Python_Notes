# What is NumPy?

NumPy (Numerical Python) is a fundamental library in Python used for numerical computing. It provides powerful multi-dimensional array objects, functions for mathematical operations, and tools for working with large datasets efficiently.

# Why Use NumPy?

**Performance:** NumPy is much faster than Python lists because it uses optimized C-based implementations.

**Memory Efficiency:** NumPy arrays consume less memory than Python lists.

**Convenience:** Provides built-in mathematical functions, linear algebra, statistics, and more.

**Vectorization:** Allows operations on entire arrays without explicit loops.

**Integration:** Works well with libraries like Pandas, SciPy, TensorFlow, and Matplotlib.

# When to Use NumPy?

When working with large numerical datasets.

When performing scientific and mathematical computing.

When doing image processing, machine learning, or data analysis.

When handling multi-dimensional data (matrices, tensors, etc.).

#  Example: Data Analysis in Finance

Let’s say we are analyzing stock price data to calculate the daily percentage change using NumPy.

### Step 1: Install NumPy

If you haven't installed NumPy yet, use:

`pip install numpy`
```python
### Step 2: Import NumPy and Create a Stock Price Dataset

import numpy as np  # Import NumPy with alias np

# Create a NumPy array representing stock prices over 5 days
stock_prices = np.array([100, 102, 105, 103, 107])

print("Stock Prices:", stock_prices)
```
## Explanation:

import numpy as np → Imports NumPy and assigns it the alias np (common convention).

np.array([...]) → Creates a NumPy array from a list of stock prices.

print(...) → Displays the stock prices.

## Step 3: Calculate Daily Percentage Change
```python
# Calculate daily percentage change
daily_change = np.diff(stock_prices) / stock_prices[:-1] * 100

print("Daily Percentage Change:", daily_change)
```
## Explanation:

np.diff(stock_prices) → Computes the difference between consecutive stock prices.

stock_prices[:-1] → Extracts all elements except the last one to align array sizes.

np.diff(stock_prices) / stock_prices[:-1] * 100 → Converts changes into percentages.

print(...) → Displays the daily percentage change.

## Step 4: Compute Average Stock Price
```python
average_price = np.mean(stock_prices)

print("Average Stock Price:", average_price)
```
Explanation:
```python
np.mean(stock_prices) → Computes the average stock price.

print(...) → Displays the result.
```
## Step 5: Identify Maximum and Minimum Stock Prices
```python
max_price = np.max(stock_prices)
min_price = np.min(stock_prices)

print("Max Stock Price:", max_price)
print("Min Stock Price:", min_price)
```
# Explanation:
```python
np.max(stock_prices) → Finds the highest stock price.

np.min(stock_prices) → Finds the lowest stock price.

print(...) → Displays the results.
```
## Step 6: Find Stock Price Volatility (Standard Deviation)
```python
volatility = np.std(stock_prices)

print("Stock Price Volatility:", volatility)
```
# Explanation:
```python
np.std(stock_prices) → Computes standard deviation (a measure of price fluctuation).

print(...) → Displays the stock price volatility.
```
# Step 7: Visualize Stock Price Trend (Optional)
```python
import matplotlib.pyplot as plt

days = np.arange(1, 6)  # Days from 1 to 5
plt.plot(days, stock_prices, marker='o', linestyle='-', color='b', label="Stock Price")
plt.xlabel("Days")
plt.ylabel("Stock Price ($)")
plt.title("Stock Price Trend")
plt.legend()
plt.show()
```

## Explanation:

import matplotlib.pyplot as plt → Imports Matplotlib for visualization.

np.arange(1, 6) → Creates an array for days [1, 2, 3, 4, 5].

plt.plot(...) → Plots stock prices over days with markers.

plt.xlabel(), plt.ylabel(), plt.title() → Adds labels and a title.

plt.legend() → Adds a legend to the graph.

plt.show() → Displays the plot.

# Summary

NumPy makes numerical operations easy and efficient, especially for financial analysis, machine learning, and data science. The vectorized operations avoid manual loops, making computations much faster and cleaner.