import time

n = int(input("Enter the number to count: "))
i = n
# print(i)
while i in range(n + 1):
    if i >= 0:
        print(i, end=' # ')
        i -= 1
        time.sleep(1)
