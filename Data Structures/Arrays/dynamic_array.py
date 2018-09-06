#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    result = []
    seqList = [[]] * n
    lastAnswer = 0
    for q in queries:
        if q[0] == 1:
            seqList[(q[1] ^ lastAnswer) % n].append(q[2])
        else:
            size = len(seqList[(q[1] ^ lastAnswer) % n])
            lastAnswer = seqList[(q[1] ^ lastAnswer) % n][q[2] % size]
            result.append(lastAnswer)
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
