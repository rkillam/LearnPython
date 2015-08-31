class Animal(object):
    def __init__(self, name, noise):
        self.name = name
        self.noise = noise


name = input('Name > ')
noise = input('Noise > ')

animal = Animal(name, noise)
print('{} makes a {} sound'.format(animal.name, animal.noise))
