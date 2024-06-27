from datetime import datetime
from TextToMorse import TextToMorseConverter
import re
from collections import Counter
from TextToMorse import MorseConverter

class MorseCodeGraph:
    @classmethod
    def report(cls, input_file, output_file):
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
                        decrypted_text += ' '
                    else:
                        decrypted_text += f"This '{char}' does not exist."
                decrypted_text += ' '
            decrypted_text += '\n'

        
        # Load stopwords from a file
        stopwords_file = 'stopwords.txt'  
        stopwords = cls.load_stopwords(stopwords_file)

        # Clean the text
        cleaned_text = cls.clean_text(decrypted_text)

        # Count the words, excluding stopwords
        word_counts = cls.count_words(cleaned_text, stopwords)

        # Write the vertical histogram to the output file
        with open(output_file, 'w') as OutFile:
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")
            OutFile.write('*************************************************\n')
            OutFile.write('       REPORT GENERATED ON: ' + timestamp + '\n')
            OutFile.write('*************************************************\n\n')
            cls.write_vertical_histogram(word_counts, OutFile)

    # Function to load stopwords from a file
    @staticmethod
    def load_stopwords(stopwords_file):
        with open(stopwords_file, 'r') as file:
            stopwords = set(line.strip() for line in file.readlines())
        return stopwords

    @staticmethod
    def clean_text(text):
        # Remove punctuation and non-alphabet characters
        text = re.sub(r'[^a-z\s]', '', text.lower())
        return text

    @staticmethod
    def count_words(text, stopwords):
        words = text.split()
        # Remove stopwords
        words = [word for word in words if word not in stopwords]
        word_counts = Counter(words)
        return word_counts

    @staticmethod
    def write_vertical_histogram(word_counts, output_file):
        max_word_length = max(len(word) for word in word_counts)
        max_frequency = max(word_counts.values())

        # Create a list of words and their Morse code representations
        words_and_morse = [
          (
             word,
             ' '.join(TextToMorseConverter.get_morse_dict().get(char, '') for char in word)
          ) for word in word_counts.keys()
        ]

        # Sort words_and_morse by frequency in descending order
        words_and_morse.sort(key=lambda x: word_counts[x[0]], reverse=True)

        # Calculate the required width for each column (word and its morse code)
        column_width = max(len(word) for word, _ in words_and_morse) + 2  # Adding space for separation
        total_columns = len(words_and_morse) * (column_width + 1)

        # Create the histogram including space for words and Morse codes at the bottom
        total_height = max_frequency + max_word_length + 2  # Adding extra space for Morse code and separator
        histogram = [[' ' for _ in range(total_columns)] for _ in range(total_height)]

        # Populate the histogram with frequencies
        for i, (word, morse) in enumerate(words_and_morse):
            start_col = i * (column_width + 1)
            for level in range(word_counts[word]):
                histogram[max_frequency - level - 1][start_col] = '*'
            # Add separator line
            histogram[max_frequency][start_col:start_col + column_width] = '-' * (column_width + 1)            # Populate the histogram with words vertically at the bottom
            morse_chars = morse.split()
            for j, char in enumerate(morse_chars):
                histogram[max_frequency + 1 + j][start_col + len(word) + 1] = char 
            for j, char in enumerate(word.upper()):
                histogram[max_frequency + 1 + j][start_col] = char
            # Populate the histogram with Morse code vertically beside the words
            

        # Write the histogram to the output file
        for row in histogram:
            output_file.write(''.join(row) + '\n')









