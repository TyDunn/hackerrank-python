#!/bin/python3

def binary_to_string(num):
	if num <= 0 or num >= 1:
		return "ERROR"

	binary = "."
	frac = 0.5
	while num > 0:
		if len(binary) >= 32:
			return "ERROR"
		if num >= frac:
			binary += "1"
			num -= frac
		else:
			binary += "0"
		frac /= 2

	return binary

if __name__ == '__main__':

	num = float(input())

	result = binary_to_string(num)

	print(result)