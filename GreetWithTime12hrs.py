import time
print("This code helps you to know the time.")
useR = input("Enter your name: ")
useR_Cap = useR.capitalize()
timestamp = int(time.strftime('%H'))
# print(timestamp)
if timestamp < 12:
    print(f"Good Morning, {useR_Cap}")
elif (timestamp >= 12) and (timestamp < 16):
    print(f"Good Afternoon, {useR_Cap}")
elif timestamp >= 16:
    print(f"Good Evening, {useR_Cap}")
elif timestamp >= 19:
    print(f"Good Night, {useR_Cap}")
else:
    print(f"Namaste, {useR_Cap} something went Wrong.")
time_now = time.strftime('%I:%M')
if timestamp < 12:
    print(f'The Time is, {time_now} AM')
else:
    print(f'The Time is, {time_now} PM')

