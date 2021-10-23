"""
2 7
0.18 0.89 109.85
1.0 0.26 155.72
0.92 0.11 137.66
0.07 0.37 76.17
0.85 0.16 139.75
0.99 0.41 162.6
0.87 0.47 151.77
4
0.49 0.18
0.57 0.83
0.56 0.64
0.76 0.18
"""

from sklearn.linear_model import LinearRegression
import numpy as np

m, n = map(int, input().strip().split())
x, y = [], []
for i in range(n):
    data = list(map(float, input().strip().split()))
    x.append(data[:-1])
    y.append(data[-1])

reg = LinearRegression()
reg.fit(x, y)

a = reg.intercept_
b = reg.coef_

q = int(input())

for j in range(q):
    data = list(map(float, input().strip().split()))
    y = a + np.dot(data, b)
    print(round(y, 2))