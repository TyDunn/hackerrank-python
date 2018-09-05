#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import accumulate
from collections import defaultdict

# Complete the arrayManipulation function below.
def arrayManipulation(m, queries):
    arr = defaultdict(int)
    for q in queries:
        arr[q[0]] += q[2]
        arr[q[1]+1] -= q[2]
    return max(accumulate(arr[idx] for idx in sorted(arr)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(m, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
