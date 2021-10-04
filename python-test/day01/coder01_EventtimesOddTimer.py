"""
异或运算
特性： 1、满足交换律、结合律
      2、无进位相加
"""

"""
一个数组中存在一个数奇数次，其他数偶数次，找出这个数
"""


def OddTimesNums1(arr):
    res = 0
    for i in arr:
        res ^= i
    return res


"""
一个数组中存在两个数奇数次，其他数偶数次，找出这两个数
"""


def OddTimesNums2(arr2):
    r1 = 0
    for i in arr2:
        r1 ^= i

    rightOne = r1 & (~r1 + 1)
    r2 = 0
    for i in arr2:
        if ((i & rightOne) == 0):
            r2 ^= i
    return r2, r1 ^ r2


if __name__ == '__main__':
    # 数组一 [ 3, 3, 2, 3, 1, 1, 1, 3, 1, 1, 1 ]
    arr = [3, 3, 2, 3, 1, 1, 1, 3, 1, 1, 1]
    res1 = OddTimesNums1(arr)
    print(res1)

    # 数组二[4, 3, 4, 2, 2, 2, 4, 1, 1, 1, 3, 3, 1, 1, 1, 4, 2, 2]
    arr2 = [4, 3, 4, 2, 2, 2, 4, 1, 1, 1, 3, 3, 1, 1, 1, 4, 2, 2]
    res2 = OddTimesNums2(arr2)
    print(res2)
