#!/bin/python3

def merge_sorted(arrA, arrB):
	idxA = len(arrA) - len(arrB) - 1
	idxB = len(arrB) - 1
	idxMerged = len(arrA) - 1

	while idxB >= 0:
		if idxA >= 0 and arrA[idxA] > arrB[idxB]:
			arrA[idxMerged] = arrA[idxA]
			idxA -= 1
		else:
			arrA[idxMerged] = arrB[idxB]
			idxB -= 1
		idxMerged -= 1

	return arrA

if __name__ == '__main__':

	lstA = list(map(int, input().split()))
	lstB = list(map(int, input().split()))

	lstA = lstA + ([0] * len(lstB))

	result = merge_sorted(lstA, lstB)

	print(result)