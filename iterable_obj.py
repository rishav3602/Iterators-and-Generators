#iterables__objects

l = [1,2,3,4,"rishav","mango",89.23]
for i in l:
    print(i)

t = (1,2,3,4,"rishav","mango",89.23)
for i in t:
    print(i)

s = {1,2,3,4,"rishav","mango",89.23}
for i in s:
    print(i)

d = {"name": "Rishav","class":"BCA"}
for x,y in d.items():
    print(f"{x} : {y}")


name = "Rishav"
for i in name:
    print(i)