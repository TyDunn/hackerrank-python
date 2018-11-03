#!/bin/python3

from collections import defaultdict

def is_pdrome_perm(input):

    letters = {}
    letters = defaultdict(lambda: 0, letters)

    for char in input:
        letters[char] += 1

    foundOdd = False
    for char in letters:
        if letters[char] % 2 != 0:
            if foundOdd:
                return False
            else:
                foundOdd = True

    return True

if __name__ == '__main__':

    result = is_pdrome_perm(input())
    print(result)