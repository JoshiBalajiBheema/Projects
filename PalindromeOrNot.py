def PalindromeOrNot():
    input_data = input("Enter your input to know if its PALINDROME or Not : ")
    (rev_input) = input_data[::-1]
    if input_data == rev_input:
        print(True)
    else:
        print(
            f"{False}\nBecause\nfrom Left to Right it reads '{input_data}' and \nfrom Right to Left it reads '{rev_input}'")


PalindromeOrNot()

