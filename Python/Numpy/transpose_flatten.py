import numpy

N, M = map(int, input().split())

arr = numpy.array([input().split() for _ in range(N)], int)

print (arr.transpose())
print (arr.flatten())