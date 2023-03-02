import time

timestamp = int(time.strftime('%H'))
# print(timestamp)
if timestamp < 12:
    print("Good Morning,")
elif (timestamp >= 12) and (timestamp < 16):
    print("Good Afternoon,")
elif timestamp >= 16:
    print("Good Evening,")
elif timestamp >= 19:
    print("Good Night,")
else:
    print("Namaste,")
timestamp = time.strftime('%H:%M:%S')
print(f'The time is {timestamp}')
