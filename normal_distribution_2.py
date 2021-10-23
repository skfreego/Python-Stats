"""
70 10
80
60
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import *

mean, std = map(int, input().strip().split())

h_grade = int(input())
l_grade = int(input())

cdf_grade = lambda x : 0.5*(1 + erf((x - mean)/(std * sqrt(2))))

print(round((1 - cdf_grade(h_grade)) * 100 , 2))
print(round((1 - cdf_grade(l_grade)) * 100 , 2))
print(round(cdf_grade(l_grade) * 100 , 2))