n, x = map(int, input().split())

scores = []
for _ in range(x):
    scores.append(map(float, input().split()))

for stu in zip(*scores):
    print(sum(stu) / len(stu))