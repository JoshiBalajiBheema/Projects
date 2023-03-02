n = int(input("Enter a range for numbers : "))
summ = 0
if n > 1000:
    print("Maximum limit reached")

else:
    for i in range(1, n + 1):
        summ = summ + i


print(summ)
