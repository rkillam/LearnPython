#!/usr/bin/python3
# -*- coding: utf-8 -*-


def sum_nums(n):
    s = 0
    for i in range(1, n+1):
        s += i

    return s


if __name__ == '__main__':
    import sys
    print(sum_nums(int(sys.argv[1])))
