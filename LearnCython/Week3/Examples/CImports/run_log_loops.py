import time

# C log function
s = time.time()
import clog
#                                              100,000,000  10,000,000
print('clog.log_loop: {:,}'.format(clog.log_loop(100000000, 10000000)))
e = time.time()
print('clog took: {:.2f}s'.format(e - s))


print('\n')


# Python log function
s = time.time()
import pylog
#                                                100,000,000  10,000,000
print('pylog.log_loop: {:,}'.format(pylog.log_loop(100000000, 10000000)))
e = time.time()
print('pylog took: {:.2f}s'.format(e - s))
