from functools import cmp_to_key

def sorter(a, b):
	if a < b:
		return -1
	if a > b:
		return 1

	return 0

data = sorted([2,5,7,1], key=cmp_to_key(sorter))

print(data)

