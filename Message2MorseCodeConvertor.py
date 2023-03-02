print("This code converts your message into MORSE CODE.")

 
# Message to Morse Code
def message2morse():
    morse_code = {
        'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ', 'F': '..-. ', 'G': '--. ', 'H': '.... ',
        'I': '.. ', 'J': '.--- ', 'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ',
        'Q': '--.- ', 'R': '.-. ', 'S': '... ', 'T': '- ', 'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ',
        'Y': '-.-- ', 'Z': '--.. ', ' ': '    ',
        '0': '----- ', '1': '.---- ', '2': '..--- ', '3': '...-- ', '4': '....- ', '5': '..... ', '6': '-.... ',
        '7': '--... ', '8': '---.. ', '9': '----. '}

    message_input = input("Enter your message : ").upper()
    new_line = '\n'

    i = 0
    for message in message_input:
        if message not in morse_code:
            print(f'[ Invalid Input detected : "{message}" ] {new_line}')
            print('Terminating program.')
            break
        else:
            value = morse_code[message_input[i].title()]
            print(value, end=" ")
            i += 1

    print(f"{new_line}::[GOOD BYE]::")


if __name__ == '__main__':
    message2morse()
