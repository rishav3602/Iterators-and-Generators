data = ["Rishav","kumar","Seth"]
x = iter(data)
print(next(x))
for i in x:
    print(i)

s = {1,2,3,4,3,45}
y = iter(s)
print(next(y))

name = "Rishavkumar"
z = iter(name)
print(next(z))

t = (1,2,3,4,5,6)
a = iter(t)
print(next(a))

d = {"name": "Rishav","age": 21}
b = iter(d)
print(next(b))