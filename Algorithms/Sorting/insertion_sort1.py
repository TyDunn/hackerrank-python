#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    i = n - 1
    num = arr[i]
    while arr[i - 1] > num and i > 0:
        arr[i] = arr[i - 1]
        i = i - 1
        print(' '.join(map(str, arr)))
    arr[i] = num
    print(' '.join(map(str, arr)))
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)