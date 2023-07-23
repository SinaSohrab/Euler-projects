a = 0
b = 0
c = 0
number = []

for i in range(0, 10):
    for x in range(0, 10):
        for y in range(0, 10):
            if i < x and x < y:
                number.append(i)
                number.append(x)
                number.append(y)
                a = i**2
                b = x**2
                c = y**2
                sum = i + x + y
                sum1=a+b+c
                if a + b == c:
                    print(a, b, c, sum1)
                    if sum1==1000:
                        print(a, b, c, sum1)
