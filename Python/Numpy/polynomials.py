import numpy

lst = list(map(float, input().split()))
x = float(input())
           
print(numpy.polyval(lst, x))