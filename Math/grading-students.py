#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    for idx, grade in enumerate(grades):
        if grade >= 38:
            q = grade // 5
            if (q + 1) * 5 - grade < 3:
                grades[idx] = (q + 1) * 5
    return grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
