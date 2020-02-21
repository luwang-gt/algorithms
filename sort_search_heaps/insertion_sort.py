tests = [
    [3, 6, 4, 0, 1, 5, 2],
    [],
    [1, 1, 1],
    [0, 2, 3, 2, 1, 3, 0, 3],
    [0, -2, -1, 3, 4],
]

def insertion_sort(nums):
    for i in range(1, len(nums)):
        num_to_insert = nums[i]
        j = i - 1
        # from nums[i-1], move numbers backwards by one position until number < num_to_insert
        while j >= 0 and nums[j] > num_to_insert:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = num_to_insert

    return nums

for test in tests:
    print(insertion_sort(test))