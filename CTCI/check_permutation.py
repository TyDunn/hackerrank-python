#!/bin/python3

from collections import defaultdict

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    char_set = [0] * 128
    
    for char in str1:
        char_set[ord(char)] += 1

    for char in str2:
        char_set[ord(char)] -= 1
        if char_set[ord(char)] < 0:
            return False        

    return True

if __name__ == '__main__':

    str1 = input()
    str2 = input()

    result = check_permutation(str1, str2)
    
    print(result)