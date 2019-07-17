#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    base = [1, 1, 2]

    if n <= 3:
        return base[n]
    # after base case
    # f(n) = f(n-3) + f(n-2) + f(n-1)
    # Set up base case
    x1 = base[0]
    x2 = base[1]
    x3 = base[2]
    for i in range(3, n):
        x3, x2, x1 = x1 + x2 + x3, x3, x2

    return x1 + x2 + x3


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
