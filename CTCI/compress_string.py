#!/bin/python3

def compress_string(in_str):
	compressed = ''
	count = 0
	for idx in range(len(in_str)):
		count += 1
		if idx + 1 >= len(in_str) or in_str[idx] != in_str[idx+1]:
			compressed += in_str[idx]
			compressed += str(count)
			count = 0
	if len(compressed) < len(in_str):
		return compressed
	else:
		return in_str

if __name__ == '__main__':

	result = compress_string(input())
	print(result)