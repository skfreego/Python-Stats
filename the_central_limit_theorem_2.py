"""
250
100
2.4
2.0

"""

from math import *

ticket = int(input())
student = int(input())
mean = float(input())
std = float(input())

sample_mean = mean * student
sample_std = std * sqrt(student)

cdf = lambda x,sample_mean, sample_std : 0.5 * (1 + erf((x-sample_mean)/(sample_std * sqrt(2))))

print(round(cdf(ticket, sample_mean, sample_std), 4))