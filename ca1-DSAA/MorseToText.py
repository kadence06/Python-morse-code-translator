from TextToMorse import MorseConverter

class MorseToTextConverter(MorseConverter):
    def __init__(self):
        # Private attribute to store the reversed dictionary
        self.__reversed_dict = {value: key for key, value in self.get_morse_dict().items()}

    def decrypt(self, input_file, output_file):
        with open(input_file, "r") as file:
            morse_lines = file.read().strip().split('\n')

        decrypted_text = ""
        for line in morse_lines:
            words = line.strip().split(', ')
            for word in words:
                characters = word.split(',')
                for char in characters:
                    if char in self.__reversed_dict:
                        decrypted_text += self.__reversed_dict[char]
                    elif char == '':
                        decrypted_text += ''
                    else:
                        decrypted_text += f"This '{char}' does not exist."
                decrypted_text += ' '
            decrypted_text += '\n'

        with open(output_file, 'w') as out_file:
            out_file.write(decrypted_text.strip())

        print("Decryption successful. Text written to", output_file)



