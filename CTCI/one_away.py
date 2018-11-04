#!/bin/python3

def is_one_away(str1, str2):
    
    if abs(len(str1) - len(str2)) > 1:
        return False

    s1 = str1 if len(str1) < len(str2) else str2
    s2 = str2 if len(str1) < len(str2) else str1

    idx1 = 0
    idx2 = 0
    diff = False

    while idx2 < len(s2) and idx1 < len(s1):
        if s1[idx1] != s2[idx2]:
            if diff:
                return False
            else:
                diff = True
            if (len(s1) == len(s2)):
                idx1 += 1
        else:
            idx1 += 1
        idx2 += 1

    return True

if __name__ == '__main__':

    str1 = input()
    str2 = input()

    result = is_one_away(str1, str2)
    
    print(result)