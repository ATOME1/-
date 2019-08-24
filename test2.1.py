#coding=utf-8
"""
    插入排序
"""
a = [31,41,59,26,41,58]
print a[5]
for i in range(1,len(a)):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j+1] = a[j]
        j = j - 1
    a[j+1] = key
print a
#降序排序
a = [31,41,59,26,41,58]
for i in range(1,len(a)):
    key = a[i]
    j = i -1
    while j >= 0 and a[j] < key:
        a[j+1] = a[j]
        j = j -1
    a[j+1] = key
print a

def addBinary(a,b):
    c = [0] * (len(a) + 1)
    up = 0
    for i in range(len(a)):
        j = len(a)-i-1
        c[j+1] = (a[j] + b[j] + up) % 2
        up =  (a[j] + b[j] + up) / 2
    c[j] = up
    return c
a = [0, 1, 1, 0, 0]
b = [1, 1, 0, 1, 0]
c = addBinary(a,b)
print c