"""
Task:- Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places (i.e.,1.234 format).
Input Format:- A single line containing the following values:
Output Format:- Print a single line denoting the answer, rounded to a scale of 3 decimal places (i.e.,1.234 format).
"""

"""
1.09 1
"""

from math import *


def binomial_dist(x, n, p):
    b = (factorial(n) / (factorial(x) * factorial(n - x))) * (p ** x) * ((1 - p) ** (n - x))
    return b


if __name__ == '__main__':
    boy, girl = map(float, input().strip().split())
    n, p = 6, boy / (boy + girl)
    b_dist = sum([binomial_dist(i, n, p) for i in range(3, 7)])

    print(round(b_dist, 3))

