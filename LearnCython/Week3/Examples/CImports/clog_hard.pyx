cdef extern from "math.h":
    float log(float n)

cpdef double log_loop(double n, unsigned long iters):
    cdef unsigned long i
    cdef double s = 0
    for i in range(iters):
        s += log(n)

    return s
