#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    count, depth = 0, 0
    start, end = False, False
    for chr in path:
        if chr == 'D':
            if depth == 0: start = True
            depth -= 1
        else:
            depth += 1
            if depth == 0: end = True
        if start and end:
            count += 1
            start, end = False, False
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

    # print(countingValleys(8, "UDDDUDUU"))
