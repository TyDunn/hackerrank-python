from collections import OrderedDict

sprmkt = OrderedDict()

for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    sprmkt[item] = sprmkt.get(item, 0) + int(quantity)
    
for item, quantity in sprmkt.items():
    print(item, quantity)