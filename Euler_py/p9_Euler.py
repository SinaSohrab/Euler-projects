a = 0
b = 0
c = 0
def abc(i):
    for i in range(0,1000):
        for x in range(0,1000):
            for y in range(0,1000):
                if a<b and b<c:
                    return True
                
                return False

for i in range(0,1000):
    if abc(i):
        print(i)