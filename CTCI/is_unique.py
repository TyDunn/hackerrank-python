#!/bin/python3

def is_unique(input):
    if len(input) > 128: 
        return False

    char_set = [False] * 128

    for char in input:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

    return True
            
if __name__ == '__main__':

    result = is_unique(input())
    print(result)