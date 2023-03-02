n = int(input("ENTER THE YEAR TO FIND OUT IF IT's A LEAP YEAR OR NOT : "))
if (n % 4 == 0) and (n % 100 != 0) or (n % 400 == 0):
    print(n, ", is a LEAP YEAR")
else:
    print(f"{n},is not a LEAP YEAR")
