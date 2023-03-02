#AGE CALCULATOR
def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    print(f'ON {today}.')
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(f'You are {age} Years OLD.')


d = int(input('DATE : '))
m = int(input('MONTH : '))
y = int(input('YEAR : '))
ageCalculator(y, m, d)
