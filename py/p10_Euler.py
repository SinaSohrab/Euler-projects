def IsEven(n):
    if n % 2 != 0:
        return True
    else:
        return False


first = 0
secend = 0

for i in range(2, 10):
    if i % IsEven  :
        print(i)
        first = i
        new = first + secend
        secend = new
        print("new", new)
print(new)
