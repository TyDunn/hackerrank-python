#!/bin/python3


def search(pat, txt):

	for i in range(len(txt) - len(pat) + 1):
		j = 0
		for j in range(0, len(pat)):
			if(txt[i + j] != pat[j]):
				break

		if j == len(pat) - 1:
			print('pattern found at index {}'.format(i))


if __name__ == '__main__':
	txt = 'AABAACAADAABAAABAA'
	pat = 'AABA'
	search(pat, txt)