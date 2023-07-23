a = 0
b = 0
c = 0
number=[]

for i in range(0, 1000):
    for x in range(0, 1000):
        for y in range(0, 1000):
            a=i
            b=x
            c=y
            if a<b and b<c:
                ta=a**2
                tb=b**2
                tc=c**2
                jam=ta+tb
                if jam==tc:
                    jam_2=ta+tb+tc
                    if jam_2==1000:
                        print(jam_2)




