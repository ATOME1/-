"""
字符串加密
"""


def func2(str, a):
    max = ord('z')
    newStr = ''
    for i in range(len(str)):
        add = a[i] % 26

        if (ord(str[i]) + add) > max:
            newStr += chr(ord(str[i]) + add - 26)
        else:
            newStr += chr(ord(str[i]) + add)

    return newStr


num = int(input())
res = []
a = [0] * 50
for i in range(50):
    if i < 3:
        a[i] = 2 ** i
    else:
        a[i] = a[i - 1] + a[i - 2] + a[i - 3]

for i in range(num):
    res.append(func2(input(), a))
print("\n".join(res))
