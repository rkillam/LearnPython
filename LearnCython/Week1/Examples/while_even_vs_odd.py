n = int(input('Number > '))

while n > 1:
    print(n)

    if n % 2 == 0:
        n /= 2
    else:
        n += 1

print(n)
