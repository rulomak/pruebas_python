
def puzzle(n):
    a = 1
    b = 1
    c = 1
    d = 1
    for numero in range(n):
        x = d + 2 * c + 3 * b + 4 * a
        a = b
        b = c
        c = d
        d = x
    return d % 10000000000


print(puzzle(10))
print(puzzle(100))
print(puzzle(pow(2022, 100)))




