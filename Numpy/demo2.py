#pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np

stock_prices = np.array([100, 102, 105, 103, 107])
days = np.arange(1, 6)  # Days from 1 to 5
plt.plot(days, stock_prices, marker='o', linestyle='-', color='b', label="Stock Price")
plt.xlabel("Days")
plt.ylabel("Stock Price ($)")
plt.title("Stock Price Trend")
plt.legend()
plt.show()