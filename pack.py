# -*- coding: utf-8 -*-
import numpy as np

"""
https://blog.csdn.net/huanghaocs/article/details/77920358
"""


def zero_one_pack(volume, volumes, values):
    """
    0-1 背包问题(每个物品只能取0次, 或者1次)
    :param volume:  背包总容量, volume=15
    :param volumes: 每个物品的容量数组表示, volumes=[5, 4, 7, 2, 6]
    :param values:  每个物品的价值数组表示, values=[12, 3, 10, 3, 6]
    :return:        返回最大的总价值对应的选择方案
    """

    def inner(idx, v):
        idx_volume = volumes[idx]
        idx_value = values[idx]
        if idx < 0 or v < 0:
            return [], 0
        if v < idx_volume:
            return inner(idx - 1, v)
        a, b = [], 0
        for i in range(2):
            c, d = inner(idx - 1, v - (idx_volume * i))
            if d + (idx_value * i) > b:
                a, b = c + ([idx] * i), d + (idx_value * i)
        return a, b

    selection = inner(len(volumes) - 1, volume)[0]

    return selection


def complete_pack(volume, volumes, values):
    """
    完全背包问题(每个物品可以取无限次)
    :param volume:  背包总容量, volume=15
    :param volumes: 每个物品的容量数组表示, volumes=[5, 4, 7, 2, 6]
    :param values:  每个物品的价值数组表示, values=[12, 3, 10, 3, 6]
    :return:        返回最大的总价值对应的选择方案
    """

    def inner(idx, v):
        idx_volume = volumes[idx]
        idx_value = values[idx]
        if idx < 0 or v < 0:
            return [], 0
        if v < idx_volume:
            return inner(idx - 1, v)
        a, b = [], 0
        for i in range(v // idx_volume + 1):
            c, d = inner(idx - 1, v - (idx_volume * i))
            if d + (idx_value * i) > b:
                a, b = c + ([idx] * i), d + (idx_value * i)
        return a, b

    selection = inner(len(volumes) - 1, volume)[0]

    return selection


def multiple_pack(volume, volumes, values, numbers):
    """
    多重背包问题(每个物品都有次数限制)
    :param volume:  背包总容量, volume=15
    :param volumes: 每个物品的容量数组表示, volumes=[5, 4, 7, 2, 6]
    :param values:  每个物品的价值数组表示, values=[12, 3, 10, 3, 6]
    :param numbers: 每个物品的个数限制，numbers=[2, 4, 1, 5, 3]
    :return:        返回最大的总价值对应的选择方案
    """

    def inner(idx, v):
        idx_volume = volumes[idx]
        idx_value = values[idx]
        idx_num = numbers[idx]
        if idx < 0 or v < 0:
            return [], 0
        if v < idx_volume:
            return inner(idx - 1, v)
        a, b = [], 0
        for i in range(min(v // idx_volume, idx_num) + 1):
            c, d = inner(idx - 1, v - (idx_volume * i))
            if d + (idx_value * i) > b:
                a, b = c + ([idx] * i), d + (idx_value * i)
        return a, b

    selection = inner(len(volumes) - 1, volume)[0]

    return selection


def main():
    volumes = np.array([5, 4, 7, 2, 6])
    values = np.array([12, 3, 10, 3, 6])
    numbers = np.array([2, 4, 1, 5, 3])

    print("01背包:")
    selection = zero_one_pack(15, volumes, values)
    print(selection, np.sum(values[selection]))
    print("完全背包:")
    selection = complete_pack(15, volumes, values)
    print(selection, np.sum(values[selection]))
    print("多重背包:")
    selection = multiple_pack(15, volumes, values, numbers)
    print(selection, np.sum(values[selection]))


if __name__ == '__main__':
    main()
