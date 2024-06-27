import random

class MorseCodePractice:
    def __init__(self):
        self.__morse_code_table = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
        }

    def get_morse_code_table(self):
        return self.__morse_code_table

    def generate_random_morse_sequence(self):
        morse_sequence = []
        morse_sequence.append(random.choice(list(self.__morse_code_table.values())))
        return ' '.join(morse_sequence)

    def morse_code_practice(self):
        print("Welcome to Morse Code Practice!")
        while True:
            morse_sequence = self.generate_random_morse_sequence()
            print("Decode the following Morse code sequence:")
            print(morse_sequence)
            
            user_translation = input("Your translation: ").upper()
            
            if user_translation == ''.join([key for key, value in self.__morse_code_table.items() if value == morse_sequence]):
                print("Correct!")
            else:
                print("Incorrect. The correct translation is:")
                correct_translation = ''.join([key for key, value in self.__morse_code_table.items() if value == morse_sequence])
                print(correct_translation)

            repeat = input("Do you want to practice again? (y/n): ")
            if repeat.lower() != 'y':
                break
