number = int(input('Enter the number for which you need a Table : '))

range_val = int(input('Enter the range of the Table : '))

for i in range(1,range_val + 1):
    print('{0} x {1} = {2}'.format(number, i, (number * i)))
