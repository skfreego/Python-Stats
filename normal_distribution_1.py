"""
20 2
19.5
20 22
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import *

mean, std = map(int, input().strip().split())

x = float(input())
p_x = 0.5*(1 + erf((x - mean)/(std * sqrt(2.0))))

lower, upper = map(int, input().strip().split())

p_upper = 0.5*(1 + erf((upper - mean)/(std * sqrt(2.0))))
p_lower = 0.5*(1 + erf((lower - mean)/(std * sqrt(2.0))))

print(round(p_x , 3))
print(round(p_upper - p_lower, 3))