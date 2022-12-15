l = [1,2,3,4,5,6,7]
k = iter(l)
 
while True:
    try:
        items = next(k)
        print(items)
    except StopIteration:   
        break


