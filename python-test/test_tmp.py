from day02.MergeSort import *
from day02.QuickSort import *



# 生成一组随机数组
def generateRandomArray(maxSize, maxValue):
    return [random.randint(0, maxValue) for i in range(maxSize)]


# 默认排序方式
def comparator(arr):
    arr.sort()


# 使用对数器的方式检测排序是否ok
if __name__ == '__main__':
    testTimes = 10000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(testTimes):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = copy.deepcopy(arr1)
        # mergeSort(arr1,0,len(arr1)-1)
        quickSort(arr1,0,len(arr1)-1)
        comparator(arr2)
        if (arr1 != arr2):
            succeed = False
            print(arr1)
            print(arr2)
            break
    print("Nice" if succeed else "Error")
    a1 = generateRandomArray(maxSize, maxValue)
    print(a1)
    mergeSort(a1,0,len(a1)-1)
    print(a1)
