tests = [
    [3, 6, 4, 0, 1, 5, 2],
    [],
    [1, 1, 1],
    [0, 2, 3, 2, 1, 3, 0, 3],
    [0, -2, -1, 3, 4],
]

def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = root_index * 2 + 1
    right_child = root_index * 2 + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if root_index != largest:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

    return nums

for test in tests:
    print(heap_sort(test))