# coding=utf8
import copy
import random


# 冒泡排序    时间复杂度：O(n2)
def bubbleSort(arr):
    pass


# 选择排序    时间复杂度：O(n2)
def selectSort(arr):
    pass


# 插入排序    时间复杂度：最优O(n) 最差O(n2)   不稳定
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


# 生成一组随机数组
def generateRandomArray(maxSize, maxValue):
    return [random.randint(0, maxValue) for i in range(maxSize)]


# 默认排序方式
def comparator(arr):
    arr.sort()


# 使用对数器的方式检测排序是否ok
if __name__ == '__main__':
    testTimes = 1000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(testTimes):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = copy.deepcopy(arr1)
        insertSort(arr1)
        comparator(arr2)
        if (arr1 != arr2):
            succeed = False
            print(arr1)
            print(arr2)
            break
    print("Nice" if succeed else "Error")
    a1 = generateRandomArray(maxSize, maxValue)
    print(a1)
    insertSort(a1)
    print(a1)
