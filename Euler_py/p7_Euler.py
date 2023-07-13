number = int(input("your number: :"))


def is_prime(n):
    for i in range(2, int(n)):
        if n % i == 0 and n % 1 == 0:
            return False
    return True

sum=0
for i in range(2, number):
    if is_prime(i):
        sum+=1

print(sum)
