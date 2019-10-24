tests = [
    [3, 6, 4, 0, 1, 5, 2],
    [],
    [1, 1, 1],
    [0, 2, 3, 2, 1, 3, 0, 3],
    [0, -2, -1, 3, 4],
]


def quicksort(nums, lo, hi):
    if lo < hi:
        p = partition(nums, lo, hi)

        quicksort(nums, lo, p - 1)
        quicksort(nums, p + 1, hi)

    return nums


def partition(nums, lo, hi):
    # Lomuto partition

    pivot = nums[hi]
    i = lo

    for j in range(lo, hi):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[hi] = nums[hi], nums[i]

    return i


for test in tests:
    print(quicksort(test, 0, len(test) - 1))
