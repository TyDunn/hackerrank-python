import numpy

N, M = map(int, input().split())

a = numpy.array([input().split() for _ in range(N)], int)
b = numpy.array([input().split() for _ in range(N)], int)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)