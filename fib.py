def fibonacci():
    current = 0
    next = 1

    while True:
        current, next = next, current + next
        yield current


for n in fibonacci():
    if n > 10000000:
        break

    print(n, end=',')
