#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    def printArray():
        print(" ".join([str(num) for num in arr]))        
    last = arr[-1]
    i = n - 1
    while i > 0  and arr[i-1] > last:
        arr[i] = arr[i-1]
        printArray()
        i -= 1
    arr[i] = last
    printArray()

if __name__ == '__main__':
    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))
    insertionSort1(5, [2, 4, 6, 8, 3])
