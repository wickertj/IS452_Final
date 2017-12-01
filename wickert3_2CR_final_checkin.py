# wickert3_2CR_final_checkin
# This program is a check-in of an in-progress project
# This project is a game that details a few techniques taught in the course under the
# narrative of a day at work as a data scientist.

import time

def start_game():

    print("Welcome")
    print(" ")
    time.sleep(1)

    start_game = input("Would you like to begin? Y/N ")
    start_game = start_game.lower()

    if start_game == "y":
        print("Beginning game...")
        time.sleep(1)
        situation_001_start()
    if start_game == "n":
        print("Exiting...")
        time.sleep(1)
        print("Done.")
    else:
        print("Invalid input, please try again.")
        start_game()

def situation_001_start():

    time.sleep(1)
    print(" ")
    print("You are a data scientist at a secretive branch of government.")
    print("Your current project is to set up a series of programs to extract data from text files and webpages.")
    print("One of your co-workers is struggling with an error in Python early on into his program.")
    print("He has isolated the problem lines and asks you for help.")

    choice_help_1 = input("Do you choose to help him? Y/N ")
    choice_help_1 = choice_help_1.lower()

    if choice_help_1 == "y":
        print("He shows you the first lines of the program:")
        print(" ")
        print("fileio = open('extracteddata007.txt', 'r')")
        print("text_readline = fileio.readline()")
        print("fileio.close()")
        print(" ")
        print("outfile = open('data_out_007')")
        print("outfile.write(text_readline)")
        time.sleep(3)
        situation_001_solution()
    if choice_help_1 == "n":
        print("He pulls you over anyway and out of pressure you decide to help him.")
        print("He shows you the first lines of the program:")
        print(" ")
        print("fileio = open('extracteddata007.txt', 'r')")
        print("text_readline = fileio.readline()")
        print("fileio.close()")
        print(" ")
        print("outfile = open('data_out_007')")
        print("outfile.write(text_readline)")
        time.sleep(3)
        situation_001_solution()
    else:
        print(" ")
        print("Invalid input, please try again.")
        situation_001_start()

def situation_001_solution():

    print(" ")
    print("You have a few options to respond:")
    print("a. I don't have enough coffee to deal with this right now.")
    print("b. You forgot to write to the outfile, add ', 'w'' to your outfile definition.")
    print("c. I don't want to deal with this right now, I have my own problems to work on.")

    choice_help_2 = input("Do you choose a, b, or c? ")
    choice_help_2 = choice_help_2.lower()

    if choice_help_2 == 'a':
        print("You go and grab a fresh cup of coffee and return to your co-worker.")
        time.sleep(1)
        situation_001_solution()
    if choice_help_2 == 'b':
        print("After telling your co-worker the mistake, he thanks you and you go to return to your own work.")
        time.sleep(1)
        situation_002_start()
    if choice_help_2 == 'c':
        print("Your co-worker guilt-trips you into sticking it through.")
        time.sleep(1)
        situation_001_solution()
    else:
        print("Invalid input, please try again.")
        situation_001_solution()

def situation_002_start():
    print(" ")
    print("You are making progress on extracting data from an XML file.")
    print("")

def main():

    start_game()

main()
