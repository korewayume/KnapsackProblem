# -*- coding: utf-8 -*-
import timeit
from refer import silence as refer_silence
from pack import silence as pack_silence


def main():
    refer_silence()
    pack_silence()


if __name__ == '__main__':
    statements = (
        ('refer_silence()', "from __main__ import refer_silence"),
        ('pack_silence()', "from __main__ import pack_silence"),
    )
    repeat = 10
    number = 1000

    for stmt, setup in statements:
        t = timeit.repeat(stmt=stmt, setup=setup, repeat=repeat, number=number)
        print(stmt, sum(t) / repeat, sep=": ")
