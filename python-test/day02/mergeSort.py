import random, copy

# 归并排序
def mergeSort(arr, L, R):
    if L == R:
        return
    mid = L + ((R - L) >> 1)
    mergeSort(arr, L, mid)
    mergeSort(arr, mid + 1, R)
    merge(arr, L, mid, R)


def merge(arr, L, mid, R):
    temp = [0 for i in range(R - L + 1)]
    i = 0
    p1 = L
    p2 = mid + 1
    while p1 <= mid and p2 <= R:
        if arr[p1] >= arr[p2]:
            temp[i] = arr[p2]
            p2 += 1
        else:
            temp[i] = arr[p1]
            p1 += 1
        i += 1
    while p1 <= mid:
        temp[i] = arr[p1]
        p1 += 1
        i += 1
    while p2 <= R:
        temp[i] = arr[p2]
        p2 += 1
        i += 1
    for i in range(R - L + 1):
        arr[L + i] = temp[i]


