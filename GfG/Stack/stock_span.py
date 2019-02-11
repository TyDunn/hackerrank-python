#!/bin/python3

def calculate_span(price, spans):
	n = len(price)
	stack = []
	stack.append(0)
	spans[0] = 1
	for i in range(1, n):
		while len(stack) > 0 and price[stack[-1]] <= price[i]:
			stack.pop()
		spans[i] = i+1 if len(stack) == 0 else (i - stack[-1])
		stack.append(i)
	return spans

if __name__ == '__main__':
	price = [10, 4, 5, 90, 120, 80]
	spans = [0 for i in range(len(price))]
	print(calculate_span(price, spans))