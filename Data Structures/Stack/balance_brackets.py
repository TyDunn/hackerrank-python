#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    table =  { ')': '(', ']':'[', '}':'{' }
    
    stack = []
    for c in s:
        if stack and table.get(c) == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    if stack:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
