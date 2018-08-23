import numpy

N = int(input())

arr = numpy.array([input().split() for _ in range(N)], float)

numpy.set_printoptions(legacy='1.13')
print(numpy.linalg.det(arr))