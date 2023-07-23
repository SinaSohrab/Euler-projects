for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a =", a, ", b =", b, ", c =", c)
            print("The product of abc is:", a*b*c)
            break


"""
def Condition(numbers):
    if (
        numbers["A"] < numbers["B"] < numbers["C"]
        and numbers["A"] + numbers["B"] == numbers["C"]
        and numbers["A"] + numbers["B"] + numbers["C"]==1000
    ):
        return True


for i in range(0, 1000):
    this_number = str(i).zfill(3)

    numbers = {}
    numbers["A"] = int(this_number[0])
    numbers["B"] = int(this_number[1])
    numbers["C"] = int(this_number[2])

    if Condition(numbers):
        squared_numbers = {}
        squared_numbers["A"] = numbers["A"] ** 2
        squared_numbers["B"] = numbers["B"] ** 2
        squared_numbers["C"] = numbers["C"] ** 2
        if Condition(numbers):
            print(squared_numbers)
"""

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
