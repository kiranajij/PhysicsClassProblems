import numpy as np
import matplotlib.pyplot as plt


x = np.r_[0:2*np.pi:100j]
y_1 = np.sin(x)
y_2 = np.cos(x)

plt.plot(x, y_1, 'r', label='$sin(x)$')
plt.scatter(x, y_2, marker='o', s=1, c='b', label="$cos(x)$")

plt.xticks([0, np.pi/2, np.pi, 3*np.pi /2, 2*np.pi], ("$0$", "$\pi/2$", "$\pi$",
                                            "$3\pi /2$", "$2\pi$"))
plt.yticks([-1, 0, 1], [-1, 0, 1])

plt.legend()
plt.grid()
plt.show()
