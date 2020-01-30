tests = [
    [3, 6, 4, 0, 1, 5, 2],
    [],
    [1, 1, 1],
    [0, 2, 3, 2, 1, 3, 0, 3],
    [0, -2, -1, 3, 4],
]

def selection_sort(nums):
    for l in range(len(nums)-1):
        for r in range(l, len(nums)):
            if nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
    return nums

for test in tests:
    print(selection_sort(test))