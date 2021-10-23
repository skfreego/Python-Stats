"""
95 85
85 95
80 70
70 65
60 70
"""

from math import *

inp_X = 80

x, y = [], []
for _ in range(5):
    X, Y = map(int, input().strip().split())
    x.append(X)
    y.append(Y)

x_mean = sum(x) / 5
y_mean = sum(y) / 5

sum_sq_x = sum([i ** 2 for i in x])
sum_sq_y = sum([i ** 2 for i in y])

sum_xy = sum([i * j for i, j in zip(x, y)])

b = ((5 * sum_xy) - (sum(x) * sum(y))) / ((5 * sum_sq_x) - (sum(x) ** 2))
a = y_mean - (b * x_mean)

reg = a + (b * inp_X)
print(round(reg, 3))