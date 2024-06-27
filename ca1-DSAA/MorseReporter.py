from datetime import datetime
from MorseToText import MorseConverter
from TextToMorse import TextToMorseConverter
from collections import Counter
import re

class MorseCodeReporter:
    @classmethod
    def decrypt(self, input_file):
        with open(input_file, "r") as file:
            morse_lines = file.read().strip().split('\n')

        reversed_dict = {value: key for key, value in MorseConverter.get_morse_dict().items()}

        decrypted_text = ""
        for line in morse_lines:
            words = line.strip().split(', ')
            for word in words:
                characters = word.split(',')
                for char in characters:
                    if char in reversed_dict:
                        decrypted_text += reversed_dict[char]
                    elif char == '':
                        decrypted_text += ''
                    else:
                        decrypted_text += f"This '{char}' does not exist."
                decrypted_text += ' '
            decrypted_text += '\n'
        
        return decrypted_text
    
    @classmethod
    def write_report(cls, decrypted_text, output_file):
        with open(output_file, 'w') as OutFile:
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")
            OutFile.write('**********************************************\n')
            OutFile.write('REPORT GENERATED ON: ' + timestamp + '\n')
            OutFile.write('**********************************************\n\n')
            OutFile.write('*** Decoded Morse Text\n')
            OutFile.write(decrypted_text)
            OutFile.write('\n\n')

    @classmethod
    def generate_report(cls, input_file, output_file):
        decrypted_text = cls.decrypt(input_file)
        cls.write_report(decrypted_text, output_file)

        stopwords_file = 'stopwords.txt'

        # Call print_word_frequencies using decrypted_text
        frequencies_text = cls.print_word_frequencies(decrypted_text, stopwords_file)
        
        # Call sort_keywords_by_frequency using decrypted_text
        sorted_keywords_text = cls.sort_keywords_by_frequency(decrypted_text, stopwords_file)

        # Write both frequencies and sorted keywords to the report
        with open(output_file, 'a') as OutFile:
            OutFile.write(frequencies_text)
            OutFile.write('\n')
            OutFile.write(sorted_keywords_text)

    @classmethod
    def print_word_frequencies(cls, decrypted_text, stopwords_file):
        # Function to load stopwords from file
        def load_stopwords(filename):
            with open(filename, 'r') as file:
                return set(word.strip() for word in file)

        # Load stopwords
        stopwords = load_stopwords(stopwords_file)

        # Extract words from decrypted text
        words = decrypted_text.lower().split()

        # Filter out stopwords and count frequencies
        word_counts = Counter(words)

        # Sort words by frequency in ascending order, length in descending order, and alphabetically
        sorted_words = sorted(word_counts.items(), key=lambda x: (x[1], -len(x[0]), x[0]))

        frequencies_text = "*** Words with Frequency =>1\n"
        for word, count in sorted_words:
            if count == 1:
                morse_code = ','.join(TextToMorseConverter.get_morse_dict().get(char.upper(), '') for char in word)
                if word not in stopwords:
                    frequencies_text += f"[{morse_code}] => {word.upper()}(*)\n"
                else:
                    frequencies_text += f"[{morse_code}] => {word.upper()}\n"

        frequencies_text += "\n*** Words with Frequency =>2\n"
        for word, count in sorted_words:
            if count == 2:
                morse_code = ','.join(TextToMorseConverter.get_morse_dict().get(char.upper(), '') for char in word)
                if word not in stopwords:
                    frequencies_text += f"[{morse_code}] => {word.upper()}(*)\n"
                else:
                    frequencies_text += f"[{morse_code}] => {word.upper()}\n"

        frequencies_text += "\n*** Words with Frequency =>5\n"
        for word, count in sorted_words:
            if count == 5:
                morse_code = ','.join(TextToMorseConverter.get_morse_dict().get(char.upper(), '') for char in word)
                if word not in stopwords:
                    frequencies_text += f"[{morse_code}] => {word.upper()}(*)\n"
                else:
                    frequencies_text += f"[{morse_code}] => {word.upper()}\n"

        return frequencies_text



    @classmethod
    def sort_keywords_by_frequency(cls, decrypted_text, stopwords_file):
        # Function to load stopwords from file
        def load_stopwords(filename):
            with open(filename, 'r') as file:
                return set(word.strip() for word in file)

        # Count word frequencies
        def count_words(words):
            return Counter(words)

        # Load stopwords
        stopwords = load_stopwords(stopwords_file)

        # Extract words from decrypted text
        words = decrypted_text.lower().split()

        # Filter out stopwords and count frequencies
        word_counts = count_words(words)

        # Remove stopwords from word_counts
        filtered_word_counts = {word: count for word, count in word_counts.items() if word not in stopwords}

        # Sort words by frequency in descending order
        sorted_words = sorted(filtered_word_counts.items(), key=lambda item: item[1], reverse=True)

        # Generate formatted text for sorted keywords
        sorted_keywords_text = "*** Keywords sorted by frequency\n"
        for word, count in sorted_words:
            sorted_keywords_text += f"{word.upper()}({count})\n"

        return sorted_keywords_text



    

    
   


