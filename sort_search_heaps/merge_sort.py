tests = [
    [3, 6, 4, 0, 1, 5, 2],
    [],
    [1, 1, 1],
    [0, 2, 3, 2, 1, 3, 0, 3],
    [0, -2, -1, 3, 4],
]

def merge_sort(nums):
    if len(nums) > 1:
    	mid = int(len(nums)/2)
    	left = merge_sort(nums[:mid])
    	right = merge_sort(nums[mid:])

    	i = 0
    	j = 0
    	res = []
    	while i < len(left) and j < len(right):
    		if left[i] < right[j]:
    			res.append(left[i])
    			i += 1
    		else:
    			res.append(right[j])
    			j += 1

    	if i < len(left):
    		res = res + left[i:]

    	if j < len(right):
    		res = res + right[j:]

    	return res

    else:
    	return nums

for test in tests:
    print(merge_sort(test))