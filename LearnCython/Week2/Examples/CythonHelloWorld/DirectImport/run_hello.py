# pyximport lets you import cython (.pyx) files without compiling them first
import pyximport
pyximport.install()

print('Before importing hello')
import hello
print('After importing hello')
