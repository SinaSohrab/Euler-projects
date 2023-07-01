adad_aval = int(input("whats your number: "))
first = 1
secend = 1
for i in range(2, adad_aval):
    if adad_aval % i == 0:
        print(i)
        while i <= adad_aval:
            if i <= adad_aval:
                new = i * secend
                i = secend
                secend = new
                new = secend
                print("n", new)
                if new == adad_aval:
                    break
            break
