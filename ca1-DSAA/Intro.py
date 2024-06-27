class Start:
    
    def __init__(self):
        print('\n')
        print('*******************************************************')
        print('* ST1507 DSAA :MorseCode message Analyzer             *')
        print('*-----------------------------------------------------*')
        print('*                                                     *')
        print('*  - Done By: Kadence Chan(p2317889)                  *')
        print('*  - Class: DAAA/2A/03                                *')
        print('*******************************************************')
        input('Press Enter, to continue....')
        
    def display_menu(self):
        print("Please select your choice ('1', '2', '3', '4', '5', '6', '7'): \n\t1. Convert Text to Morse Code\n\t2. Convert Morse Code To Text\n\t3. Generate Morse Word Frequencies Report\n\t4. Generate Morse Keyword Frequencies Graph\n\t5. PracticeMe\n\t6. Guess!\n\t7. Exit")
        choice = input('Enter Choice: ')
        return choice

