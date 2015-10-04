import datetime

N = 100000000

def python_for():
    for i in range(N):
        pass

def cython_for():
    cdef int i
    for i in range(N):
        pass


print('{} Python for...'.format(str(datetime.datetime.now())))
python_for()
print('{} Done Python for'.format(str(datetime.datetime.now())))

print('{} Cython for...'.format(str(datetime.datetime.now())))
cython_for()
print('{} Done Cython for'.format(str(datetime.datetime.now())))
