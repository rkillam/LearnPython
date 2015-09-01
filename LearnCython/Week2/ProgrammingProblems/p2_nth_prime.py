#####################################################################
# Problem 1: Nth Prime
#
# The code bellow takes a number, n, as a command line argument and
# then prints nth prime number. Given 3, the program prints 5 (note
# that 1 is not prime) Given 5,000,000 the program takes ~1 minute
# to run. Use Cython to improve the runtime of the program.
#
# You might want to copy this script as is under a new name so that
# you have a reference, both for code and for runtime.
#
# If you know of ways to improve the runtime of the program that do
# not involve Cython, I would suggest using the Cython approach and
# then trying those improvments with the new Cython code.
#####################################################################

import math
import sys


def is_prime(n):
    if n % 2 == 0:
        return False

    for i in range(3, math.ceil(math.sqrt(n)), 2):
        if n % i == 0:
            return False

    return True


n = int(sys.argv[1])

last_prime = 2
for _ in range(1, n):
    i = last_prime + 1
    while not is_prime(i):
        i += 1

    last_prime = i

print('The {}th prime is {}'.format(n, last_prime))
