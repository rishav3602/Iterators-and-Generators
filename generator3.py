def new(n):
    l = []
    for i in range(n):
        l.append(i**3)
    return l 

k = new(300)
for i in k:
   print(k)

def gencube(n):
    for i in range(n):
        yield(i**3)

l = gencube(50089)
print(l)
print(type(l))
for i in l:
    print(i)

