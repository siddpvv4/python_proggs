#Matplotlib Visualizations
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Line Plot
plt.figure()
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Bar Chart
plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()

# Scatter Plot
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

# Pie Chart
plt.figure()
plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()