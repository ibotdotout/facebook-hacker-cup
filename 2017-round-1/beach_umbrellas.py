#!/usr/bin/env python3

# Failed with large factorial
# http://fredrikj.net/blog/2012/03/factorials-mod-n-and-wilsons-theorem/
# http://fishi.devtail.io/weblog/2015/06/25/computing-large-binomial-coefficients-modulo-prime-non-prime/
# https://codeaccepted.wordpress.com/tag/modulo-1000000007/


import itertools
import math


mod = 1000000007


def combinations_with_replacement_len(n, r):
    # (n+r-1)! / r! / (n-1)!
    a = math.factorial(n+r-1)
    b = math.factorial(r)
    c = math.factorial(n-1)
    return a / b / c


def solve(n, m, umbrellas):
    if n == 1:
        return m
    totals = sum(umbrellas) * 2
    pairs = itertools.combinations(umbrellas, 2)
    spaces = [totals - a - b + 1 for a, b in pairs if totals]
    left_spaces = [m - i for i in spaces if i <= m]
    comb_pairs = [
        combinations_with_replacement_len(n+1, r) % mod for r in left_spaces]
    result = sum(comb_pairs) * math.factorial(n - 2) % mod * 2 % mod
    return int(result)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()]
        umbrellas = [int(input()) for _ in range(n)]
        result = solve(n, m, umbrellas)
        print("Case #{0}: {1}".format(i + 1, result))
