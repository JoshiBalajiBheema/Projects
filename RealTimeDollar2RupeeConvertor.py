from forex_python.converter import CurrencyRates

cr = CurrencyRates()
amount = int(input("Enter the amount : "))

USD_c = 'USD'
INR_c = 'INR'

print(f"{USD_c} to {INR_c}, {amount}")
print('Converting...')
resultt = cr.convert(USD_c, INR_c, amount)
print(f'Rs.{round(resultt, 2)}')  # round function takes 2 parameters (num, digits)
