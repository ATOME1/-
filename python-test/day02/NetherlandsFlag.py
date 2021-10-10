"""
问题一：
给定一个数组arr，和一个数num，请把小于等于num的数放在数组的左边，大于num的数放在数组的右边。要求额外空间复杂度O(1)，时间复杂度O(N)
思路：
1、遍历一遍，小于给定数的话进行交换操作
2、大于给定数的话不作擦操作
3、需要两个指针
"""


def test1(arr, num):
    i = 0
    j = 0
    while j < len(arr):
        if arr[j] <= num:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
            j += 1
        else:
            j += 1


arr = [1, 3, 7, 2, 5, 6, 3, 1]
num = 4
test1(arr, num)
print(arr)

"""
问题二：
荷兰国旗问题：给定一个数组arr，和一个数num，请把小于num的数放在数组的左边，等于num的放在数组的中间，大于num的数放在数组的右边。要求额外空间复杂度O(1),时间复杂度O(N)
思路：
1、分三个区域，需要两个指针
"""


def test1(arr, num):
    i = 0
    j = 0
    k = len(arr) - 1
    while j < k:
        if arr[j] < num:
            # 交换，i++
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
            j += 1
        elif arr[j] > num:
            # 仅仅交换
            tmp = arr[j]
            arr[j] = arr[k]
            arr[k] = tmp
            k-=1
        else:
            j += 1


a2 = [3, 5, 6, 3, 4, 5, 2, 6, 9, 0]
test1(a2,5)
print(a2)
a3 = [4,2]
test1(a3,3)
print(a3)