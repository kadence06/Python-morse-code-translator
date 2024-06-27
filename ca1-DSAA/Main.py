from Intro import Start
from TextToMorse import TextToMorseConverter
from MorseToText import MorseToTextConverter
from MorseReporter import MorseCodeReporter
from graph import MorseCodeGraph
from PracticeMe import MorseCodePractice
from Guess import MorseGame


####################################################################
#                         Main Programme                           #
####################################################################

while True:
    #Part 0(Intro)#
    start = Start()
    choice = start.display_menu()

    while choice not in ['1', '2', '3', '4', '5', '6', '7']:
        print("\nINVALID CHOICE. CHOOSE A NUMBER BETWEEN 1-7\n")
        choice = start.display_menu()
    
    #Part 1(Text-Morse)#
    if choice == '1':        
        input_file = input('Please enter input file:')
        output_file = input('Please enter output file:')
        a = TextToMorseConverter()
        a.encrypt(input_file, output_file)
        
    #Part 2(Morse-Text)#
    elif choice == '2':
        input_file = input("Enter the name of the encrypted text file: ")
        output_file = input("Enter the name of the output text file: ")
        b = MorseToTextConverter()
        b.decrypt(input_file, output_file)
        
    elif choice == '3':
        input_file = input("Please enter input file: ")
        output_file = input("Please enter output file: ")
        MorseCodeReporter.generate_report(input_file, output_file)
        print(f"Report generated and saved to {output_file}")
    
    elif choice == '4':
        input_file = input("Please enter input file: ")
        output_file = input("Please enter output file: ")
        MorseCodeGraph.report(input_file, output_file)\
    
    elif choice == '5':
        morse_practice = MorseCodePractice()
        morse_practice.morse_code_practice()

    elif choice == '6':
        practice = MorseCodePractice()  
        morse_game = MorseGame(practice)  
        morse_game.morse_code_game()

    elif choice == '7':
        print("\nBye, thanks for using ST1507 DSAA: MorseCode Message Analyzer")
        break