tests = [
    [3, 6, 4, 0, 1, 5, 2],
    [],
    [1, 1, 1],
    [0, 2, 3, 2, 1, 3, 0, 3],
    [0, -2, -1, 3, 4],
]

def bubble_sort(nums):
    swapped = True
    while swapped: # outter loop
        swapped = False # If no swap happen, exit the outer loop
        for i in range(len(nums)-1): # inner loop
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True
    return nums


for test in tests:
    print(bubble_sort(test))