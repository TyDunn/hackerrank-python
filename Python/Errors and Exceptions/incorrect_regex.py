import re

for _ in range(int(input())):
    strg = True
    try:
        reg = re.compile(input())
    except re.error:
        strg = False
    print(strg)