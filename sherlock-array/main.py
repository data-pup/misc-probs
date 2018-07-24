#!/bin/python

import sys

def solve(a):
    cnt = len(a)
    left_sums = [0] * cnt
    right_sums = [0] * cnt
    for left_i in range(cnt):
        right_i = cnt - 1 - left_i

        if left_i > 0:
            left_sums[left_i] = left_sums[left_i - 1] + a[left_i]
        else:
            left_sums[left_i] = a[left_i]

        if right_i < cnt - 1:
            right_sums[right_i] = right_sums[right_i + 1] + a[right_i]
        else:
            right_sums[right_i] = a[right_i]

    for i in range(cnt):
        if i == 0:
            left_total = 0
        else:
            left_total = left_sums[i - 1]

        if i == cnt - 1:
            right_total = 0
        else:
            right_total = right_sums[i + 1]

        if left_total == right_total:
            return 'YES'

    return 'NO'

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = solve(a)
    print(result)
