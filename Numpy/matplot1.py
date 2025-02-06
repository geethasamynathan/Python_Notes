import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

# Creating the plot
plt.plot(x, y, marker='o', linestyle='-', color='b')

# Adding labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Basic Line Plot")

# Display the plot
plt.show()

days = np.arange(1, 6)  # Days from 1 to 5
plt.plot(days, stock_prices, marker='o', linestyle='-', color='b', label="Stock Price")
plt.xlabel("Days")
plt.ylabel("Stock Price ($)")
plt.title("Stock Price Trend")
plt.legend()
plt.show()