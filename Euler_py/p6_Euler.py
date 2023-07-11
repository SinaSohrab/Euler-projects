number = int(input("your number: "))
number += 1

first=0
sum=0
new_sum=0
for i in range(1, number):
    first = i**2
    sum = first + sum

print(sum)
del first
first = 0

for i in range(1, number):
    new_sum = i + new_sum
new_sum = new_sum**2
javab = new_sum - sum
print(javab)