#coding=utf8


def hailStone(n):
    length = 1
    while n > 1:
        n = 3*n+1 if n%2 else n/2
        print n
        length+=1
    return length

print '长度为%d' % hailStone(27)
