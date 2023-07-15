def find_nth_prime(n):
    primes = [2]
    num = 3
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 2
    return primes[-1]

print(find_nth_prime(10001))
