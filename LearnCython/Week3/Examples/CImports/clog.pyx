cimport libc.math as cmath

cpdef double log_loop(double n, unsigned long iters):
    cdef unsigned long i
    cdef double s = 0
    for i in range(iters):
        s += cmath.log(n)

    return s
