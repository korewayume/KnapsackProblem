# -*- coding: utf-8 -*-
import sys
from functools import update_wrapper
import numpy as np
import pandas as pd

counter = {}


def logged(key):
    def decorator(f):
        def wrapped_function(idx, v):
            if idx >= 0 and v > 0:
                counter.setdefault(key, []).append((idx + 1, v))
            return f(idx, v)

        return update_wrapper(wrapped_function, f)

    return decorator


def zero_one_pack(volume, volumes, values):
    """
    0-1 背包问题(每个物品只能取0次, 或者1次)
    :param volume:  背包总容量, volume=15
    :param volumes: 每个物品的容量数组表示, volumes=[5, 4, 7, 2, 6]
    :param values:  每个物品的价值数组表示, values=[12, 3, 10, 3, 6]
    :return:        返回最大的总价值对应的选择方案
    """

    @logged(sys._getframe().f_code.co_name)
    def inner(idx, v):
        if idx < 0 or v <= 0:
            return [], 0
        idx_volume = volumes[idx]
        idx_value = values[idx]
        if v < idx_volume:
            return inner(idx - 1, v)
        a, b = [], 0
        for k in range(2):
            c, d = inner(idx - 1, v - (idx_volume * k))
            if d + (idx_value * k) > b:
                a, b = c + ([idx] * k), d + (idx_value * k)
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

    @logged(sys._getframe().f_code.co_name)
    def inner(idx, v):
        if idx < 0 or v <= 0:
            return [], 0
        idx_volume = volumes[idx]
        idx_value = values[idx]
        if v < idx_volume:
            return inner(idx - 1, v)
        a, b = [], 0
        for k in range(v // idx_volume + 1):
            c, d = inner(idx - 1, v - (idx_volume * k))
            if d + (idx_value * k) > b:
                a, b = c + ([idx] * k), d + (idx_value * k)
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

    @logged(sys._getframe().f_code.co_name)
    def inner(idx, v):
        if idx < 0 or v <= 0:
            return [], 0
        idx_volume = volumes[idx]
        idx_value = values[idx]
        idx_num = numbers[idx]
        if v < idx_volume:
            return inner(idx - 1, v)
        a, b = [], 0
        for k in range(min(v // idx_volume, idx_num) + 1):
            c, d = inner(idx - 1, v - (idx_volume * k))
            if d + (idx_value * k) > b:
                a, b = c + ([idx] * k), d + (idx_value * k)
        return a, b

    selection = inner(len(volumes) - 1, volume)[0]

    return selection


def main():
    volumes = [5, 4, 7, 2, 6]
    values = [12, 3, 10, 3, 6]
    numbers = [2, 4, 1, 5, 3]

    print("01背包:")
    selection = zero_one_pack(15, volumes, values)
    print(selection, np.sum(np.array(values)[selection]))
    print(call_counter(zero_one_pack))

    print("完全背包:")
    selection = complete_pack(15, volumes, values)
    print(selection, np.sum(np.array(values)[selection]))
    print(call_counter(complete_pack))

    print("多重背包:")
    selection = multiple_pack(15, volumes, values, numbers)
    print(selection, np.sum(np.array(values)[selection]))
    print(call_counter(multiple_pack))


def call_counter(func):
    call_stack = counter.get(func.__name__)
    shape = (max([x[0] for x in call_stack]), max([x[1] for x in call_stack]))
    table = np.zeros(shape, dtype=np.int)
    for idx, v in call_stack:
        table[idx - 1, v - 1] += 1
    return pd.DataFrame(
        table,
        index=range(1, shape[0] + 1),
        columns=["{:>2}".format(x) for x in range(1, shape[1] + 1)],
    )


if __name__ == '__main__':
    main()
