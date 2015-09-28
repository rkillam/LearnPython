cpdef unsigned long long sum_nums(long n):
    cdef unsigned long long s = 0
    cdef long i
    for i in range(1, n+1):
        s += i

    return s


if __name__ == '__main__':
    import sys
    print(sum_nums(long(sys.argv[1])))
