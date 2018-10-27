import numpy as np

a1 = np.array([[1, 3],
                [2, 4]])
a2 = np.array([[4, -2],
                [-3, 1]])
a3 = np.array([[1, 2],
                [2, 1]])

print a1.dot(a2) + 2 * a3
