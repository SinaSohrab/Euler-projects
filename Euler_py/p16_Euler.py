number = int(input("your number: "))
t_number = int(input("to the power of the number: "))

j_tavan = number**t_number
j_tavan_str = str(j_tavan)

sum = 0

for i in j_tavan_str:
    sum = i + sum


print(sum)
