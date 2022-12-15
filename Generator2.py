def new():
    n = 1
    print("First line")
    yield n

    n = n + 1
    print("second line")
    yield n

    n = n + 1
    print("third line")
    yield n

for i in new():
    print(i)

q = new()
print(q)
print(type(q))
print(next(q))
for i in q:
    print(i)