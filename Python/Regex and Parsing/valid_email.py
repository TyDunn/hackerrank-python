import re

pattern = r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>'
num = int(input())

for _ in range(num):
    name, email = input().split()
    valid = re.match(pattern, email) 
    if valid:
        print(name, email)