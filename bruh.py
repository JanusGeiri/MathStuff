import math


def digitsum(n):
    string = str(n)
    s = 0
    for i in string:
        s += int(i)
    return s


nums1 = []
for n in range(50, 100):
    if digitsum(n) < 10 and n % 3 == 0 and n % 4 == 0:
        nums1.append(n)
print(nums1)
