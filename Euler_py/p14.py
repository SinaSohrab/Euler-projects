def collatz_sequence_length(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

max_length = 0
starting_number = 0

for i in range(1, 1000000):
    length = collatz_sequence_length(i)
    if length > max_length:
        max_length = length
        starting_number = i

print("The starting number that produces the longest chain:", starting_number)
print("Chain Length:", max_length)