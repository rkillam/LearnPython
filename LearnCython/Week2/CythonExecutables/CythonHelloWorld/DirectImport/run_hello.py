import pyximport
pyximport.install()

print('Before importing hello')
import hello
print('After importing hello')
