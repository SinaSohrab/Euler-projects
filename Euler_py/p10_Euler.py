number=int(input("Enter the number and see the sum of prime numbers: "))

def is_prim(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


first = 0
second = 0

for i in range(2, number):
    if is_prim(i):
        first1 = i
        sum = first + second
        second = sum

print(sum)
