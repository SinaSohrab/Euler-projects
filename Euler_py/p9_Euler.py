a = 0
b = 0
c = 0
number = []

for i in range(0, 1000):
    for x in range(0, 1000):
        for y in range(0, 1000):
            number.append(i)
            number.append(x)
            number.append(y)
            if i < x and x < y:
                a = i**2
                b = x**2
                c = y**2
                sum=a+b+c
                if a + b == c and sum<1000:
                    print(c)
