import numpy as np  # Import NumPy with alias np

# Create a NumPy array representing stock prices over 5 days
stock_prices = np.array([100, 102, 105, 103, 107])

print("Stock Prices:", stock_prices)


# Calculate daily percentage change
daily_change = np.diff(stock_prices) / stock_prices[:-1] * 100

print("Daily Percentage Change:", daily_change)