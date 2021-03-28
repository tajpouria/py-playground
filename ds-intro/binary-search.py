def bs_recursive(arr, tar, **kwargs):
	start = kwargs.get("start", 0)
	end = kwargs.get("end", len(arr) - 1)
		
	if start > end:
		return -1

	mi = (start + end) // 2	
	if arr[mi]  == tar:
		return mi
	elif arr[mi] > tar:
		return bs_recursive(arr, tar, start=start, end=mi-1)
	else:
		return bs_recursive(arr, tar, start=mi+1, end=end) 

def bs_iterative(arr, tar, **kwargs):
	start = 0
	end = len(arr) - 1

	while(start <= end):
		mi = (start + end) // 2

		if arr[mi] == tar:
			return mi
		elif arr[mi] > tar:
			end = mi - 1
		else:
			start = mi + 1	
	
	return None

a = [1,2,3,4,5,6,7]
print(bs_recursive(a, 5))
print(bs_iterative(a, 0))

