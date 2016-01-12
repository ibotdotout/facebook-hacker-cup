#!/usr/bin/env python3

import math
import collections as cols


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)


def count_boomerang_constellation(stars):
    results = 0
    for s in stars:
        dist = [math.hypot(r[0] - s[0], r[1] - s[1]) for r in stars]
        results += sum([nCr(v, 2)
                        for k, v in cols.Counter(dist).items() if v > 1])
    return results

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        stars = [tuple(int(i) for i in input().split()) for _ in range(n)]
        result = count_boomerang_constellation(stars)
        print("Case #{0}: {1}".format(i + 1, int(result)))
