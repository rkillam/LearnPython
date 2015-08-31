import animal_class

def make_animal():
    name = input('Name > ')
    noise = input('Noise > ')
    return animal_class.Animal(name, noise)


def get_query():
    name = input('Name > ')
    noise = input('Noise > ')
    return name, noise


def menu():
    print('add to add an animal')
    print('find to find an added animal')
    print('q to quit')


animals = []
choice = ''

while choice != 'q':
    menu()
    choice = input('> ')

    if choice == 'add':
        animals.append(make_animal())

    elif choice == 'find':
        name, noise = get_query()
        for animal in animals:
            if animal.name == name or animal.noise == noise:
                print('Found {} who makes a {} noise'.format(animal.name, animal.noise))
    print('')
