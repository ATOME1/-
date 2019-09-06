#!/usr/local/bin/python3
#coding=utf-8
import math
import time
import sys
import random
#实例1  有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
"""
res = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j) and (i != k) and (j != k):
                res.append(i * 100 + j * 10 + k)
print("组成的所有三位数是： " + str(res) + "\n总数为： " + str(len(res)))
"""


""" 实例2
    企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
    高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
    60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
    
profit = 0
while True:
    profit = input("当月利润： ")
    if profit != '' and int(profit) > 0:
        break
    else:
        print("请重新输入!!!\n")
profit = int(profit)
arr = [100, 60, 40, 20, 10, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
bonus = 0
for i in range(0,len(arr)):
    if profit > arr[i]:
        bonus += (profit - arr[i]) * rat[i]
        print((profit - arr[i]) * rat[i])
        profit = arr[i]
print(bonus)
"""


""" 实例3
    一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？（10000以内）

for i in range(10000):
    if float(int(math.sqrt(i+100))) == math.sqrt(i+100) and float(int(math.sqrt(i+268))) == math.sqrt(i+268):
        print(i)
"""


""" 实例4
    输入某年某月某日，判断这一天是这一年的第几天？

year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))
days = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0<month<13:
    sum = days[month - 1]
else:
    print('data error')
sum += day
leap = 0
if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
    leap = 1
if month > 2:
    sum += leap
print('it is the %dth day.' % sum)
"""


""" 实例5
    输入三个整数x,y,z，请把这三个数由小到大输出。

l = []
for i in range(3):
    x = int(input('Integer:'))
    l.append(x)
l.sort()
print(l)
"""


""" 实例6
    斐波那契数列。

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    l = [1, 1]
    for i in range(2, n):
        x = l[i - 1] + l[i - 2]
        l.append(x)
    return l
res = fib(20)
print(res)
"""


""" 实例7
    将一个列表的数据复制到另外一个列表中

a = [1,2,3,4,6]
b = a[:]
print(id(a))
print(id(b))
print(b)
"""


""" 实例8
    输出9*9乘法口诀表。

for i in range(1,10):
    for j in range(1,10):
        if j > i:
            break
        print('%d*%d=%d\t' % (j,i,i*j),end='')
    print()
"""


""" 实例9
    暂停一秒输出。 

myD = {1:'a',2:'b'}
for a,b in dict.items(myD):
    print(a,b)
    time.sleep(1)
"""


""" 实例10
    暂停一秒输出

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
time.sleep(2)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
"""


""" 实例11
    古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
    斐波那契数列
"""


""" 实例12
    判断101-200之间有多少个素数，并输出所有素数。

l = []
for i in range(101,201):
    x = int(math.sqrt(i));
    res = 1
    for j in range(2,x+1):
        if i % j == 0:
            res = 0
    if res:
        l.append(i)
print(l)
print(len(l))
"""


""" 实例13
    打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
"""
"""
res = []
for i in range(100,1000):
    a = int(i / 100)
    b = int(i / 10) % 10
    c = i % 10
    if a**3 + b**3 + c**3 == i:
        res.append(i)
print(res)
"""


""" 实例14
    将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""
"""
n = int(input('input number:'))
for i in range(2,n + 1):
    while i != n:
        if n % i == 0:
            print('%d * ' % i,end='')
            n = n / i
        else:
            break
print('%d' % n)
"""


""" 实例15
    利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
"""
"""
score = int(input('请输入分数：'))
if score >= 90:
    grade = 'A'
elif 60 <= score < 90:
    grade = 'B'
else:
    grade = 'C'
print('%d belongs to %s' % (score,grade))
"""


# 实例16
 #   输出指定格式的日期。




""" 实例17
    输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""
"""
res = input('please input your message:')
letters = 0
space = 0
digit = 0
others = 0
for i in res:
    if i.isalpha():
        letters += 1
    elif i.isalnum():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        others += 1
print('letters : %d, space : %d, digit : %d, others : %d.' % (letters,space,digit,others))
"""


""" 实例18
    求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
"""
"""
a = int(input('数字：'))
n = int(input('数量：'))
sum = 0
for i in range(n):
    sum += a * (10 ** i) * (n - i)
print(sum)
"""


""" 实例19
    一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
"""
"""
for i in range(1,1001):
    sum = 0
    for j in range(1,i):
        if i % j == 0:
           sum += j
    if sum == i:
        print(i)
"""


""" 实例20
    一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""
"""
Sn = 100
Hn = Sn / 2
for i in range(2,11):
    Sn += Hn * 2
    Hn /= 2
print(Sn)
print(Hn)
"""


""" 实例21
    猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，
    又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
"""
"""
sum = 1
for i in range(9,0,-1):
    sum = (sum + 1) * 2
print(sum)
"""


# 实例22
 #   两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。
  #  a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。



""" 实例23
    打印出如下图案（菱形）:
"""
"""
for i in range(7):
    for j in range(7):
        if (i + j) > 2 and (i + j) < 10 and (j - i) < 4 and (i - j) <4:
            print('*\t',end='')
        else:
            print('\t',end='')
    print()
"""


""" 实例24
    有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""
"""
a = 1
b = 2
sum = 0
for i in range(20):
    sum += b/a
    c = a + b
    a = b
    b = c
print(sum)
"""


""" 实例25
    求1+2!+3!+...+20!的和。
"""
"""
t = 1
sum = 0
for i in range(1,21):
    t *= i
    sum += t
print(sum)
"""


""" 实例26
    利用递归方法求5!。
"""
"""
def sum(n):
    if n == 1:
        return n
    return n * sum(n-1)
print(sum(5))
"""


""" 实例27
    利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
"""
"""
def output(a,l):
    if l == 0:
        return
    print(a[l-1],end='\t')
    output(a,l-1)


a = input('message:')
output(a, len(a))
"""


""" 实例28
    有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
    问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
"""
"""
def age(n):
    if n == 1:c = 10
    else: c = age(n-1) + 2
    return c


print(age(5))
"""


""" 实例29
    给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
"""
"""
def reverse(a):
    num = 0
    if a == 0:
        return 0
    elif a < 0:
        a = -a
        while a != 0:
            num = num * 10 + a % 10
            a = int(a/10)
        num = -num
    else:
        while a != 0:
            num = num * 10 + a % 10
            a = int(a / 10)
    return num

a = int(input('number : '))
res = reverse(a)
print(res)
print(int(math.log10(a))+1)
"""


""" 实例30
    一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""
"""
a = int(input('number : '))
len = int(math.log10(a) + 1)
if len == 5 :
    b = a % 10
    c = int(a/10000)
    d = int(a%100/10)
    e = int(a/1000)%10
    if b == c and d == e:
        print('%d 是回文数' % a)

    else:
        print('%d 不是回文数' % a)
else:
    print('请输入正确数值')
"""


#实例31

""" 实例32
    按相反的顺序输出列表的值。
"""
"""
a = ['a','v',2,4]
b = a.reverse()
print(a)
print(a[::-1])
"""


""" 实例33
    按逗号分隔列表。
"""
"""
l = [1,2,3,4,5,6]
s1 = '..'.join(str(n) for n in l)
print(s1)
"""


""" 实例35
    文本颜色设置。
"""
"""
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)
"""


""" 实例36
    求100之内的素数。
"""
"""
l = []
for i in range(2,101):
    res = 1
    for j in range(2,int(math.sqrt(i) + 1)):
        if i > j and i % j == 0:
            res = 0
    if res:l.append(i)
print(l)
"""


""" 实例37
    对10个数进行排序。
"""
"""
l = [12,2,34,13,35,6,32,56,676,45,23]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            a = l[i]
            l[i] = l[j]
            l[j] = a
print(l)
"""


""" 实例38
    求一个3*3矩阵对角线元素之和。
"""


""" 实例39
    有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
"""
"""
l = [2, 6, 12, 13, 23, 32, 34, 35, 45, 56, 676]
a = int(input('input your num: '))
l.append(a)
for i in range(len(l)-1,0,-1):
    if l[i] < l[i-1]:
        a = l[i]
        l[i] = l[i-1]
        l[i-1] = a
print(l)
"""


""" 实例40
    将一个数组逆序输出。
"""
"""
l = [2,4,6,3,34,21]
l.reverse()
print(l)
"""


""" 实例41
    模仿静态变量的用法。
"""


""" 实例42
    学习使用auto定义变量的用法。
"""
"""
num = 2


def autofunc():
    num =1
    print('internal block num is %d' % num)
    num +=1


for i in range(3):
    print('The num is %d' % num)
    num += 1
    autofunc()
"""


""" 实例43
    模仿静态变量(static)另一案例。
"""

""" 实例44
    学习使用external的用法。。
"""


""" 实例46
    求输入数字的平方，如果平方运算后小于 50 则退出。
"""
"""
while True:
    a = int(input('input your num: '))
    res = a * a
    print('%d的平方是：%d' % (a,res))
    if res < 50:
        break
"""


""" 实例47
    两个变量值互换。
"""
"""
def exchange(a,b):
    a,b = b,a
    return (a,b)
if __name__ == '__main__':
    x = 10
    y = 20
    print('x = %d, y = %d' % (x,y))
    exchange(x,y)
    print('x = %d, y = %d' % (x, y))
"""


""" 实例49
    使用lambda来创建匿名函数。    
"""
"""
MAXIMUM = lambda x,y : (x > y) * x + (x < y) * y
MINIMUM = lambda x,y : (x > y) * y + (x < y) * x
if __name__ == '__main__':
    a = 10
    b = 32
    print(MAXIMUM(a,b))
    print(MINIMUM(a,b))
"""


""" 实例50
    输出一个随机数。
"""
"""
for i in range(5):
    print(random.randrange(1,100,2))
a = [12,23,43,1,45,23]
random.shuffle(a)
print(a)
"""


""" 实例54
    取一个整数a从右端开始的4〜7位。
"""
"""
a = 123456789
b = str(a)
print(int(b[-6:-3]))
"""


""" 实例56
    画图，学用circle画圆形。　　
"""


""" 实例61
    打印出杨辉三角形（要求打印出10行如下图）
"""
"""
l = [1]
for i in range(1,11):
    l.append(0)
    for j in range(1,i+1):
        l[j] = pre[j-1] + pre[j]
    l.append(1)
    pre = l[:]
    print(l)
"""


def triangles():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]
        print(pre)

triangles()


""" 实例62
    查找字符串。　
"""
"""
str1 = 'qwertyuiop'
str2 = 'ert'
print(str1.find(str2))
"""


""" 实例66
    输入3个数a,b,c，按大小顺序输出。　　
"""
"""
def sort(a,b,c):
    if a > b:a, b = b, a
    if a > c:a,b,c = c,a,b
    if a < c and b > c:b,c = c,b
    return (a,b,c)
print(sort(1,3,5))
"""


""" 实例67
    输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
"""
def change():
    #a = [1, 3, 4, 5, 7, 43, 23, 79, 0, 12]
    a = [1,2,3,7,9,8]
    b = a[:]
    b.sort()
    c = a[0]
    d = a.index(b[-1])
    a[0] = b[-1]
    a[d] = c

    c = b[0]
    d = a.index(b[0])
    a[d] = a[-1]
    a[-1] = c
    return a


""" 实例68
    有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
"""
"""
n = 7
m = 3
a = [1,2,3,4,5,6,7]
b = a[-m:] + a[0:-m]
print(b)
"""

""" 实例69
    有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
"""
num = []
for i in range(1,21):
    num.append(i)
print(num)
i = 0
while True:

    pass































