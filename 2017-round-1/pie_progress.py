#!/usr/bin/env python3

# http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/

MAX = 9999999999999
N = 310

# shared matrix for reduce computed time
K = [[MAX for _ in range(N)] for _ in range(N)]  # dp
C = [[0 for _ in range(N)] for _ in range(N)]  # accumulate


def solve(n, m, prices):
    sorted_price = [sorted(p) for p in prices]

    # calculate accumulate
    for i in range(1, n + 1):
        C[i][0] = 0
        for j in range(1, m + 1):
            C[i][j] = C[i][j-1] + sorted_price[i-1][j-1]

    # clear K
    for i in range(n + 1):
        for j in range(n + 1):
            K[i][j] = MAX

    K[0][0] = 0
    for d in range(1, n+1):
        for w in range(d, n+1):
            for i in range(min(m + 1, w + 1)):
                K[d][w] = min(K[d-1][w-i] + C[d][i] + i * i,  K[d][w])
    return K[n][n]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()]
        prices = [[int(i) for i in input().split()] for _ in range(n)]
        result = solve(n, m, prices)
        print("Case #{0}: {1}".format(i + 1, result))
