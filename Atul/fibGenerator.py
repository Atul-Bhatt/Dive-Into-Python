
def fib(elements):
    a, b = 0, 1
    i = 0
    while i < elements:
        i += 1
        yield a
        a, b = b, (a + b)


for n in fib(20):
    print(n, end=' ')

# pass it to the list() function to generate a list

print(list(fib(30)))
