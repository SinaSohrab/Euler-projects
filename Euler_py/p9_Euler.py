def jame_argham(number_digits):
    sum_digits = 0
    for k in number_digits:
        sum_digits += number_digits[k]
    return sum_digits


def number_is_ok(number_digits):   
    if (
        number_digits["a"]**2 < number_digits["b"]**2
        and number_digits["b"]**2 < number_digits["c"]**2
        and number_digits["a"]**2 + number_digits["b"]**2 == number_digits["c"]**2
    ):
        if jame_argham(number_digits) == 1000:
            return True


for number in range(0, 1000):
    this_number = str(number).zfill(3)

    number_digits = {}
    number_digits["a"] = int(this_number[0])
    number_digits["b"] = int(this_number[1])
    number_digits["c"] = int(this_number[2])

    if number_is_ok(number_digits):
        print(number)
