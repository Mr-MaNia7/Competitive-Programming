#!/bin/python3

import math
import os
import random
import re
import sys

def countSwaps(a):
    count = 0
    def swap(x: int, y: int):
        xpos = a.index(x)
        ypos = a.index(y)
        a[xpos], a[ypos] = a[ypos], a[xpos]
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                swap(a[j], a[j + 1])
                count += 1
    print("Array is sorted in {} swaps.".format(count))
    print("First Element:", a[0])
    print("Last Element:", a[-1])

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
