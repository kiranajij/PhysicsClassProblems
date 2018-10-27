import numpy as np
import matplotlib.pyplot as plt

x = np.r_[-10:10:100j]

y_1 = x**1
y_2 = x ** 2

plt.plot(x, y_1, label="$y=x$")
plt.plot(x, y_2, label="$y=x^2$")

plt.title("Demonstration of Plotting with Python")
plt.xlabel("X")
plt.ylabel("Y")

plt.legend()
plt.show()
