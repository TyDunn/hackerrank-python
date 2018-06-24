import re

for _ in range(int(input())):
    if re.search(r'^(7|8|9)\d{9}$', input()):
        print("YES")
    else:
        print("NO")