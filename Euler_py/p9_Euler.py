a = 0
b = 0
c = 0


def bozorg_tar(bg):
    for i in range(0,1000):    
        if a < b and b < c and a**2 + b**2 == c**2:
            return True
    return False


for i in range(0, 1000):
    if bozorg_tar(i):
        for x in range(0,1000):
            print(x)