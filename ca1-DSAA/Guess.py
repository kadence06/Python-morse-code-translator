import random

class MorseGame:
    def __init__(self, morse_code_practice):
        self.__morse_code_table = morse_code_practice.get_morse_code_table()
        self.__characters = list(self.__morse_code_table.keys())

    def get_morse_code_table(self):
        return self.__morse_code_table

    def get_characters(self):
        return self.__characters

    def generate_random_character(self):
        return random.choice(self.__characters)

    def text_to_morse(self, text):
        morse_sequence = ''
        for char in text.upper():
            if char in self.__morse_code_table:
                morse_sequence += self.__morse_code_table[char] + ' '
        return morse_sequence.strip()

    def morse_code_game(self):
        print("Welcome to the Morse Code Translation Game!")
        while True:
            try:
                rounds = int(input('How many rounds? '))
                if rounds > 10:
                    print("Sorry, that's too many rounds. Please choose 10 or fewer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    
        score = 0
        for i in range(rounds):
            character = self.generate_random_character()
            print("Character:", character)
            
            user_translation = input("Translation: ").upper()
            
            if user_translation == self.text_to_morse(character):
                print("Correct!")
                score += 1
            else:
                print("Incorrect. \nThe correct Morse code translation is:", self.text_to_morse(character))

        print("Your score:", score, '/', rounds)





