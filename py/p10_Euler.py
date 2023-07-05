number=int(input("your number: "))

def is_prim(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


firs = 0
secend = 0

for i in range(2, number):
    if is_prim(i):
        firs = i
        sum = firs + secend
        secend = sum

print(sum)
