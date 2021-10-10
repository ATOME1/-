"""
快速排序
"""
import random


def quickSort(arr, L, R):
    if L < R:
        swap(arr, L + random.randint(0, R - L), R)
        p = partition(arr, L, R)
        quickSort(arr, L, p[0] - 1)
        quickSort(arr, p[1] + 1, R)


def partition(arr, L, R):
    less = L
    more = R - 1
    while L <= more:
        if arr[L] < arr[R]:
            swap(arr, less, L)
            less += 1
            L += 1
        elif arr[L] > arr[R]:
            swap(arr, more, L)
            more -= 1
        else:
            L += 1
    swap(arr, L, R)
    return [less, L]


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


arr = [1, 3, 7, 2, 5, 6, 3, 1]

quickSort(arr, 0, len(arr) - 1)
print(arr)

# print(random.randint(1, 2))
