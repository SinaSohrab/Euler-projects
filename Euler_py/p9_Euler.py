a = 0
b = 0
c = 0
number=[]

for i in range(0, 10):
    for x in range(0, 10):
        for y in range(0, 10):
            a=i
            b=x
            c=y
            if a<b and b<c:
                i=a**2
                x=b**2
                y=c**2
                number.append(i)
                number.append(x)
                number.append(y)
                if i+x==y:
                    print(number)


print("number ",number)

