#!/bin/python3


def to_string(a):
	return ''.join(a)


def permute(a, l, r):
	if l == r:
		print(to_string(a))
	else:
		for i in range(l, r+1):
			a[l], a[i] = a[i], a[l]
			permute(a, l+1, r)
			a[l], a[i] = a[i], a[l]


if __name__ == '__main__':
	string = "ABC"
	n = len(string)
	a = list(string)
	permute(a, 0, n-1)