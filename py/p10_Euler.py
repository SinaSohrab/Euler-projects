
def is_prim(n):
    aval = True
    for i in range(2, n/2):
        if n % i == 0:
            aval = False
    return aval

firs=0
secend=0

for i in range(2,2000000):
    if is_prim(i):
        firs=i
        sum=firs+secend
        secend=sum
        
print(sum)