#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    min_val = abs(arr[1] - arr[0])
    for i in range(2, len(arr)):
        diff = abs(arr[i-1] - arr[i])
        if diff < min_val:
            min_val = diff
    return min_val
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()