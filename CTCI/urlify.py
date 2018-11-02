#!/bin/python3

import string

def urlify(input):
    return string.replace(input, ' ', '%')
            
if __name__ == '__main__':

    result = urlify(input())
    print(result)