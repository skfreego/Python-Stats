"""
100
500
80
.95
1.96
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import *

sample_size = int(input())
mean = int(input())
std = int(input())
confidence = float(input())
z = float(input())

mu_neg = mean - z * (std / sqrt(sample_size))
mu_pos = mean + z * (std / sqrt(sample_size))

print(round(mu_neg, 2))
print(round(mu_pos, 2))