#coding=utf-8
import random
import datetime
import math
"""
    插入排序    时间复杂度：n^2
    ceshi
"""

def insertSort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = key
#降序排序
a = [31,41,59,26,41,58]
for i in range(1,len(a)):
    key = a[i]
    j = i -1
    while j >= 0 and a[j] < key:
        a[j+1] = a[j]
        j = j -1
    a[j+1] = key
print(a)

#2.1-4二进制加法
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
print(c)
"""
    选择排序    时间复杂度：n^2
"""
def chooseSort(a):
    for i in range(len(a)):
        k = i
        for j in range(i+1,len(a)):
            if a[k] > a[j] :
                k = j
        key = a[k]
        a[k] = a[i]
        a[i] = key


"""
    归并排序，不使用哨兵元素    时间复杂度：nlg(n)
"""
def merge(a,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = a[p+i]
    for i in range(n2):
        R[i] = a[q+i+1]
    i = 0
    j = 0
    for k in range(p,r+1):
        if i == len(L):
            a[k] = R[j]
            j+=1
        elif j == len(R):
            a[k] = L[i]
            i+=1
        elif L[i] <= R[j]:
            a[k] = L[i]
            i+=1
        else:
            a[k] = R[j]
            j+=1

def mergeSort(a,p,r):
    q = 0
    if p >= r:
        return
    q = (p+r)/2
    mergeSort(a,p,q)
    mergeSort(a,q+1,r)
    merge(a,p,q,r)


"""
    归并排序中对小数组采用插入排序     时间复杂度：nk+nlg(n/k)
    k = lg(n)   效率最优
"""

def mergeInsertSort(a,p,r,k):
    if r-p+1 > k:
        q = (p + r) / 2
        mergeInsertSort(a, p, q, k)
        mergeInsertSort(a, q + 1, r, k)
        merge(a, p, q, r)
    else:
        insert_merge(a,p,r)

def insert_merge(a,p,r):
    for i in range(p,r+1):
        key = a[i]
        j = i-1
        while j>=p and a[j]>key:
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = key



print("----------------------------------")
a =[0]*20000
for i in range(20000):
    a[i] = random.randint(0,100000)
b = a[:]
c = a[:]
d = a[:]
print(id(a),id(b),id(c),id(d))


b1 = datetime.datetime.now()
mergeSort(a,0,len(a)-1)
e1 = datetime.datetime.now()
print(e1 - b1)
print(a)
"""
b2 = datetime.datetime.now()
chooseSort(b)
e2 = datetime.datetime.now()
print e2 - b2
print b
b3 = datetime.datetime.now()
insertSort(c)
e3 = datetime.datetime.now()
print e3 - b3
print c
"""
k = math.log(len(d),2)
b4 = datetime.datetime.now()
mergeInsertSort(d,0,len(d)-1,k)
e4 = datetime.datetime.now()
print(e4 - b4)
print(d)
