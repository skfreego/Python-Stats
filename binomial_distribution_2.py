"""
Task:- A manufacturer of metal pistons finds that, on average,12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:
No more than 2 rejects?
At least 2 rejects?
Input Format:- A single line containing the following values (denoting the respective percentage of defective pistons and the size of the current batch of pistons)
"""

"""
12 10
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import *


def binomial_dist(x, n, p):
    b = (factorial(n) / (factorial(x) * factorial(n - x))) * (p ** x) * ((1 - p) ** (n - x))
    return b


if __name__ == '__main__':
    perc, piston_size = map(float, input().strip().split())
    n, p = 10, perc / 100
    b_dist = sum([binomial_dist(i, n, p) for i in range(3)])
    b_dist2 = sum([binomial_dist(i, n, p) for i in range(2, 11)])

    print(round(b_dist, 3))
    print(round(b_dist2, 3))