#!/usr/bin/env python3

# http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/


def cal_price(items, n):
    picks = items[:n]
    result = sum(picks) + len(picks) ** 2
    return result


def solve(n, m, prices):
    MAX = 9999999999999
    K = [[MAX for x in range(n+1)] for x in range(n+1)]
    sorted_price = [sorted(p) for p in prices]

    for d in range(1, n+1):
        for w in range(n+1):
            for i in range(m+1):
                items = sorted_price[d-1]
                if i <= w:
                    prev = 0 if w - i == 0 else K[d-1][w-i]
                    val = cal_price(items, i)
                    K[d][w] = min(val + prev, K[d][w])
    return K[n][n]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()]
        prices = [[int(i) for i in input().split()] for _ in range(n)]
        result = solve(n, m, prices)
        print("Case #{0}: {1}".format(i + 1, result))
