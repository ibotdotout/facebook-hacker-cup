#!/usr/bin/env python3

import math


def solve(inputs):
    p, x, y = inputs
    r = 50
    opposite = y - 50
    adjacent = x - 50
    degreeX = math.atan2(opposite, adjacent) / math.pi * 180
    degreeY = (degreeX * -1 + 180 + 270) % 360  # clockwise and start as Y axis
    distance = math.hypot(opposite, adjacent)
    P = p * 360 / 100.0
    result = True if distance <= r and degreeY < P else False
    return result

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        inputs = [int(i) for i in input().split()]
        result = solve(inputs)
        flag = "black" if result else "white"
        print("Case #{0}: {1}".format(i + 1, flag))
