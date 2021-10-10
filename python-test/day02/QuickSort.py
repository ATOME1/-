"""
快速排序
"""


def quickSort(arr, L, R):
    if L >= R:
        return
    partition(arr, )


def partition(arr, L, R):
    pass


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


arr = [1, 3, 7, 2, 5, 6, 3, 1]

quickSort(arr, 0, len(arr) - 1)
print(arr)
