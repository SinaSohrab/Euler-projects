number = int(input("your number: "))
number += 1

first = 0
secend = 0

new_first = 0
new_secend = 0

for i in range(1, number):
    first = i
    first = first**2
    sum = first + secend
    secend = sum

for i in range(1, number):
    new_first = i
    new_sum = new_first + new_secend
    new_secend = new_sum
    new_sum = new_sum**2

javab = new_sum - sum
print(javab)
