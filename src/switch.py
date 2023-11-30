import unittest

def switch_sort(a):
    for i in range(0, len(a) - 1):  # 控制比较的轮数
        for j in range(i + 1, len(a)):  # 控制每轮比较的次数
            if a[i] < a[j]:  # 从大到小排列
                a[i], a[j] = a[j], a[i]
    return a