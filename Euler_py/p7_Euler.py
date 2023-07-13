number = int(input("your number: :"))


def is_prime(n):
    for i in range(2, int(n)):
        if n % i == 0 and n % 1 == 0:
            return False
    return True


sum = 0
for i in range(2, number):
    if is_prime(i):
        ii=i
        sum += 1

taghsim = sum / 2
int(taghsim)

for i in range(1, number):
    if is_prime(i):    
        if i <= taghsim:
            print("taghsim:", ii, sum,)
