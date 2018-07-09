from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

count = OrderedCounter(input() for _ in range(int(input())))
print(len(count))
print(*count.values())