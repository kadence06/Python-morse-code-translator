class MorseConverter:
    # Class attribute containing the Morse code dictionary
    __morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-',
        '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', '!': '-.-.--'
    }

    # Public class method to access the Morse code dictionary (read-only)
    @classmethod
    def get_morse_dict(cls):
        return cls.__morse_dict


class TextToMorseConverter(MorseConverter):
    @classmethod
    def encrypt(cls, input_file, output_file):
        with open(input_file, "r") as file:
            text = file.read().upper()

        morse_message = ""
        for letter in text:
            if letter in cls.get_morse_dict():
                morse_message += cls.get_morse_dict()[letter] + ","
            elif letter == ' ':
                morse_message += ' ,'
            else:
                morse_message += '\n'

        if morse_message.endswith(','):
                morse_message = morse_message[:-1]
            

        with open(output_file, 'w') as file_out:
            file_out.write(morse_message)
            
        print("\nTranslation successful. Morse code written to", output_file, "\n")
        

