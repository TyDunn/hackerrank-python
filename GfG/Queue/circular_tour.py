#!/bin/python3

class PetrolPump:

	def __init__(self, petrol, distance):
		self.petrol = petrol
		self.distance = distance

def print_tour(arr):

	length = len(arr)
	start = 0
	end = 1

	current = arr[start].petrol - arr[start].distance

	while end != start or current < 0:
		while current < 0 and start != end:
			current -= arr[start].petrol - arr[start].distance
			start = (start + 1) % length
			if start == 0:
				return -1
		current += arr[end].petrol - arr[end].distance
		end = (end + 1) % length
	return start

if __name__ == '__main__':
	arr = [PetrolPump(6,4), PetrolPump(3,6), PetrolPump(7,3)]
	start = print_tour(arr)
	print("No Solution") if start == -1 else print("start:", start)