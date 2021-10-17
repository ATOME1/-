"""
公司用一个字符串来表示员工的出勤信息

现需根据员工的出勤信息，判断本次是否能获得出勤奖，能获得出勤奖的条件如下：
缺勤不超过一次；
没有连续的吃到/早退；
任意连续7次考勤，缺勤/迟到/早退不超过3次
"""


def func1(str):
    arr = str.strip().split(" ")
    absent = 0
    lateOrleave = 0
    for i in range(len(arr)):

        if arr[i] == 'absent':
            absent += 1
        if arr[i] in ['late', 'leaveearly']:
            lateOrleave += 1

        # 缺勤不超过1次或没有连续的迟到早退
        if absent > 1 or lateOrleave > 1:
            return 'false'

        if i <= len(arr) - 7:
            other = 0
            for j in range(i, i + 7):
                if arr[j] in ['absent', 'late', 'leaveearly']:
                    other += 1
            if other > 3:
                return 'false'

    return 'true'


num = int(input())
# str = 'present absent present present leaveearly present absent'
res = []
for i in range(num):
    res.append(func1(input()))
print(" ".join(res))
