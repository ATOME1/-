# coding=utf8
import copy
import random

"""
冒泡排序
时间复杂度：O(n2)
"""


def bubbleSort(arr):
    pass


"""
选择排序
时间复杂度：O(n2)
"""


def selectSort(arr):
    pass


"""
插入排序
时间复杂度：最优O(n) 最差O(n2)   不稳定
"""


def insertSort(arr):
    if len(arr) < 2 or arr is None:
        return
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if (j > 0 and arr[j] < arr[j - 1]):
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
    return arr


arr = [random.randint(0, 20) for i in range(10)]
print("原数组  ：" + str(arr))

arr1 = copy.deepcopy(arr)
print("插入排序：" + str(insertSort(arr1)))

print(list(range(10)))
