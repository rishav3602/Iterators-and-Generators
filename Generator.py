def square(n):
    for i in range(n):
        return i**2

k = square(9)
print(k)
print(type(k))

def square(n):
    for i in range(n):
        yield i**2

r = square(3)
print(r)
print(next(r))
for i in r:
    print(i)
print(type(r))
