for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a =", a, ", b =", b, ", c =", c)
            print("The product of abc is:", a*b*c)
            break

