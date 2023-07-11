number = int(input("your number: "))
number += 1

first = 0
secend = 0

for i in range(1, number):
    first = i
    first = first**2
    sum = first + secend
    secend = sum
    
del first,secend
first = 0
secend = 0

for i in range(1, number):
    first = i
    new_sum = first + secend
    secend = new_sum
    new_sum = new_sum**2

javab = new_sum - sum
print(javab)
