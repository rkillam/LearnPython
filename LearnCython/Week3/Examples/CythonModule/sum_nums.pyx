cdef unsigned long long sum_nums(unsigned long n):
    cdef unsigned long long s = 0
    cdef unsigned long i
    for i in range(1, n+1):
        s += i
    return s
