"""
在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和。求一个数组的小和
"""


def smallSum(arr):
    if arr is None or len(arr) < 2:
        return 0
    return mergeSort(arr, 0, len(arr) - 1)


def mergeSort(arr, L, R):
    if L == R:
        return 0
    mid = L + ((R - L) >> 2)
    return mergeSort(arr, L, mid) + mergeSort(arr, mid + 1, R) + merge(arr, L, mid, R)


def merge(arr, L, mid, R):
    temp = [0] * (R - L + 1)
    i = 0
    p1 = L
    p2 = mid + 1
    sub = 0
    while p1 <= mid and p2 <= R:
        if arr[p1] >= arr[p2]:
            temp[i] = arr[p2]
            i += 1
            p2 += 1
        else:
            temp[i] = arr[p1]
            sub += (R - p2 + 1) * arr[p1]
            i += 1
            p1 += 1
    while p1 < mid:
        temp[i] = arr[p1]
        i += 1
        p1 += 1
    while p2 < R:
        temp[i] = arr[p2]
        i += 1
        p2 += 1

    for j in range(i):
        arr[L + j] = temp[j]
    return sub


arr = [1, 3, 4, 2, 5]
# smallSum(arr)
print(smallSum(arr))




"""
逆序对问题，在一个数组中，左边的数如果比右边的数大，则这两个数构成一个逆序对，请打印所有逆序对
"""
def mergeSort1(arr, L, R):
    if L == R:
        return 0
    mid = L + ((R - L) >> 2)
    mergeSort1(arr, L, mid)
    mergeSort1(arr, mid + 1, R)
    merge1(arr, L, mid, R)


def merge1(arr, L, mid, R):
    temp = [0] * (R - L + 1)
    i = 0
    p1 = L
    p2 = mid + 1
    while p1 <= mid and p2 <= R:
        if arr[p1] > arr[p2]:
            print([arr[p1],arr[p2]])
            temp[i] = arr[p2]
            i += 1
            p2 += 1
        else:
            temp[i] = arr[p1]
            i += 1
            p1 += 1
    while p1 <= mid:
        temp[i] = arr[p1]
        i += 1
        p1 += 1
    while p2 <= R:
        temp[i] = arr[p2]
        i += 1
        p2 += 1

    for j in range(i):
        arr[L + j] = temp[j]


arr1 = [1, 3, 4, 2, 5]
mergeSort1(arr1,0,len(arr1)-1)