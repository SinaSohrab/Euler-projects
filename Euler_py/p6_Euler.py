number = int(input("your number: "))
number += 1

secend = 0

for i in range(1, number):
    i = i**2
    sum = i + secend
    secend = sum

del secend
secend = 0

for i in range(1, number):
    new_sum = i + secend
    secend = new_sum

new_sum = new_sum**2
javab = new_sum - sum
print(javab)
