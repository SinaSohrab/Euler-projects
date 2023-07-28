number=7
def get_divisors_count(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n // i != i:
                count += 2
            else:
                count += 1
    return count


def find_triangle_number_with_divisors_count(divisors_count):
    n = 1
    while True:
        triangle_number = n * (n + 1) // 2
        divisors_count_of_triangle_number = get_divisors_count(triangle_number)
        if divisors_count_of_triangle_number >= divisors_count:
            return triangle_number
        n += 1


print(find_triangle_number_with_divisors_count(number))