class FixedMultiStack:

	def __init__(self, capacity):
		self.num_stacks = 3
		self.capacity = capacity
		self.values = [0] * (self.num_stacks * self.capacity)
		self.sizes = [0] * self.num_stacks

	def print(self):
		for val in self.values:
			print(val, end=" ")
		print()

	def push(self, stack_num, val):
		if self.is_full(stack_num):
			return 'Stack full!' # TODO: make this an exception
		self.sizes[stack_num] += 1
		self.values[self._top_index(stack_num)] = val

	def pop(self, stack_num):
		if self.is_empty(stack_num):
			return 'Stack empty!' # TODO: make this an exception
		idx = self._top_index(stack_num)
		val = self.values[idx]
		self.values[idx] = 0
		self.sizes[stack_num] -= 1
		return val

	def peek(self, stack_num):
		if self.is_empty(stack_num):
			return 'Stack empty!' # TODO: make this an exception
		return self.values[self._top_index(stack_num)]

	def is_empty(self, stack_num):
		return self.sizes[stack_num] == 0

	def is_full(self, stack_num):
		return self.sizes[stack_num] == self.capacity

	def _top_index(self, stack_num):
		offset = stack_num * self.capacity
		size = self.sizes[stack_num]
		return offset + size - 1

if __name__ == '__main__':
	stack = FixedMultiStack(3)
	stack.push(0, 1)
	stack.push(0, 2)
	stack.push(0, 3)
	stack.push(1, 4)
	stack.push(1, 5)
	stack.push(1, 6)
	stack.push(2, 7)
	stack.push(2, 8)
	stack.push(2, 9)
	stack.pop(0)
	stack.pop(1)
	stack.pop(2)
	stack.pop(0)
	stack.pop(1)
	stack.pop(2)
	stack.print()
