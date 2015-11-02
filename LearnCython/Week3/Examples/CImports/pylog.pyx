import math

cpdef double log_loop(double n, unsigned long iters):
    cdef unsigned long i
    cdef double s = 0
    for i in range(iters):
        s += math.log(n)

    return s
