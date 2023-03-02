responses = {}

polling_active = True

while polling_active:
    name = input("\nEnter Your Full Name or Press 'Q' to Exit : ")
    if name != "Q":
        response = input("Your Ambition: ")
        responses[name] = response
        repeat = input("Would you like to make another person take the poll? : (Yes or No)").lower()
        if repeat == 'no':
            polling_active = False
    else:
        print(responses)
        break
print('\n --- Poll Results ---')
for name, response in responses.items():
    print(f'{name.capitalize()} wants to be, {response.capitalize()}')
