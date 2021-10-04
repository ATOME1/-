import random

"""
二分法的详解与扩展
1、在一个有序数组中，找某个数是否存在
2、在一个有序数组中，找>=某个数最左侧的位置
3、局部最小值问题
"""


# 1、在一个有序数组中，找某个数是否存在
def BSExist(arr, num):
    L = 0
    R = len(arr) - 1
    mid = 0
    while L < R:
        mid = L + ((R - L) >> 1)
        if (arr[mid] == num):
            return True
        elif (arr[mid] > num):
            R = mid - 1
        else:
            L = mid + 1
    return arr[L] == num


arr = [random.randint(0, 10) for i in range(10)]
arr.sort()
num = 5
print(BSExist(arr, num))


# 2、在一个有序数组中，找>=某个数最左侧的位置
def BSNearLeft(arr, num):
    L = 0
    R = len(arr) - 1
    mid = 0
    point = 0
    if num > arr[R]:
        return "不存在"
    while L < R:
        mid = L + ((R - L) >> 1)
        if (arr[mid] >= num):
            R = mid - 1
            point = mid
        else:
            L = mid + 1
    return point


arr1 = [random.randint(0, 10) for i in range(20)]
arr1.sort()
num = 5
print(arr1)
print(BSNearLeft(arr1, num))


# 无需数组，任何两相邻数不相等，找出局部最小值（某一个数小于其左边和右边）
def BSAwesome(arr):
    num = 0
    L = 0
    R = len(arr) - 1
    mid = 0
    if arr[L] < arr[L + 1]:
        return L
    if arr[R] < arr[R - 1]:
        return R
    while True:
        mid = L + ((R - L) >> 1)
        if arr[mid] > arr[mid - 1]:
            R = mid - 1
        elif arr[mid] > arr[mid+1]:
            L = mid + 1
        else:
            return mid



arr2 = []
while len(arr2) < 20:
    num = random.randint(0, 100)
    if num not in arr2:
        arr2.append(num)
print(arr2)
index = BSAwesome(arr2)
print(index+1)
print(arr2[index])
