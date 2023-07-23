a = 0
b = 0
c = 0
number = []

for i in range(0, 10):
    for x in range(0, 10):
        for y in range(0, 10):
            number.append(i)
            number.append(x)
            number.append(y)
            if i < x and x < y:
                a = i**2
                b = x**2
                c = y**2
                sum = a + b + c
                if a + b == c:
                    print(a, b, c)
