"""
简易内存池
"""


class Memory():
    maxSize = 100
    dict = {100: 0}

    def request(self, size):
        if size > self.maxSize or size <= 0:
            return "error"
        keys = sorted(list(self.dict.keys()))
        address = -1

        if len(keys) <= 1 or keys[0] >= size:
            address = 0
            self.dict[address] = size
            return address

        for i in range(len(keys) - 1):
            if keys[i + 1] - keys[i] - self.dict[keys[i]] >= size:
                address = keys[i] + self.dict[keys[i]]
                self.dict[address] = size
                break

        return address if address >= 0 else "error"

    def releasee(self, startSddress):
        return self.dict.pop(startSddress, "error")

num = int(input())
mem = Memory()
for i in range(num):
    arr = input().strip().split("=")
    if arr[0] == 'REQUEST':
        print(mem.request(int(arr[1])))
    elif arr[0] == 'RELEASE':
        if mem.releasee(int(arr[1])) == 'error':
            print('error')
    else:
        print("input error")