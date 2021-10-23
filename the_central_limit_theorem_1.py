"""
9800
49
205
15
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import *

max_wght = int(input())
box = int(input())
mean = int(input())
std = int(input())

sample_mean = mean * box
sample_std = std * sqrt(box)

cdf = lambda x,sample_mean, sample_std : 0.5 * (1 + erf((x-sample_mean)/(sample_std * sqrt(2))))

print(round(cdf(max_wght, sample_mean, sample_std), 4))