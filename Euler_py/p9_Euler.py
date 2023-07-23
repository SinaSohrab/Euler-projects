def Condition(numbers):
        if numbers["A"] < numbers["B"] < numbers["C"]:
            numbers["A"] ** 2
            numbers["B"] ** 2
            numbers["C"] ** 2
            if numbers["A"] + numbers["B"] + numbers["C"] == 1000:
                return True


for i in range(0, 1000):
    this_number = str(i).zfill(3)

    numbers = {}
    numbers["A"] = int(this_number[0])
    numbers["B"] = int(this_number[1])
    numbers["C"] = int(this_number[2])

    if Condition(numbers):
        print(i)


"""
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
"""
