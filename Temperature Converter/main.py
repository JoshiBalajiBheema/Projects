# Degree symbol code is {ALT + 0176}
def temperature_c_f():
    print("How do you want your output? [ Celsius : c | Fahrenheit : f ]")
    output = input("c or f : ").lower()

    if output == 'c':
        temperature = int(input("The Temperature in Celsius : "))
        celsius = (temperature - 32) * 5 / 9
        print(f'{celsius} °C')
    elif output == 'f':
        temperature = int(input("The Temperature in Fahrenheit : "))
        fahrenheit = (temperature * 9 / 5) + 32
        print(f'{fahrenheit} °F')

    else:
        print("Check your inputs.")


if __name__ == '__main__':
    temperature_c_f()
