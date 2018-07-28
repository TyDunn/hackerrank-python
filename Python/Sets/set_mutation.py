(_, orgSet) = (input(), set(map(int, input().split())))

for _ in range(int(input())):
    (command, newSet) = (input().split()[0], set(map(int, input().split())))
    getattr(orgSet, command)(newSet)

print(str(sum(orgSet)))