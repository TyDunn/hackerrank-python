#!/bin/python3

import os

def is_unique(input):
    if len(input) > 128: 
        return False

    char_set = [False] * 128

    for char in input:
        val = ord(char)
        if char_set[val]:
            return False
        har_set[val] = True

    return True
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    result = is_unique(input())

    fptr.write(result)
    fptr.write('\n')

    fptr.close()