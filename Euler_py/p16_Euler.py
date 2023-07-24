number = 2
t_number = 1000

j_tavan = number**t_number

print(j_tavan)

j_tavan_str = str(j_tavan)
print(type(j_tavan_str))
sum = 0

for i in j_tavan_str:
    sum += int(i)


print(sum)
