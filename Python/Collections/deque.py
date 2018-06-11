from collections import deque

deq = deque()

for _ in range(int(input())):
    inpu = input().split()
    getattr(deq, inpu[0])(*inpu[1:])
    
print(' '.join(deq))