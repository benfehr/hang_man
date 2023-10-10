import random
from words import word_list

def main_menu():
    """
    Function to show user a main menu with title and options to begin gameplay
    """
    print(""" 
    
██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █ 
▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ 
 ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░ 
    """)
    print("""Welcome to Hangman""")
    print("1. Start the game")
    print("2. View the rules")
    print("3. Exit")
    can_play = False

    while not can_play:
        choice = input("Please choose an option \n").upper()
        if choice == "1":
            select_difficulty()
            play(get_word())
            can_play = True
        elif choice == "2":
            instructions()
            can_play = True
        elif choice == "3":
            print("So long, farewell, auf wiedersehen goodbye ")
            exit()
        else:
            print('Please choose again from the options')

def instructions():
    """
    Shows users the rules of hangman
    """
    print("Guess a letter\n")
    print("Guess another letter\n")
    print("Think, 'what letter could be next?' \n")
    print("Guess another letter or if you're a genius, try and guess the whole word \n")
    print("If you run out of letters, then Mr Stickman shall be hanged by the neck until DEAD \n")
    input("Press enter to return to the main menu \n")
    main_menu()

def select_difficulty():
    """
    Allows user to select how many chances they have to complete the game
    """
    print("Choose a difficulty\n")
    print("Type E for easy (8 Lives)\n")
    print("Type M for medium (6 Lives)\n")
    print("Type H for hard (4 Lives)\n")
    can_continue = False

    while not can_continue:
        choice = input("Please choose E, M or H \n").upper()

        if choice == 'E':
            return 8
        if choice == 'M':
            return 6
        if choice == 'H':
            return 4


def get_word():
    """
    Pulls word from words.py for the user to try and guess
    """
    word = random.choice(word_list)
    return word.upper()

def play(word):
    """
    Function to create the logic for the game
    """
    word_status = " _ " * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = select_difficulty()
    print("Let's play!")
    print(display_hangman(tries))
    print(word_status)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Nice one,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_status)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_status = "".join(word_as_list)
                if "_" not in word_status:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already tried that word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_status = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_status)
        print("\n")
    if guessed:
        print(" You saved Mr Stickman! Well done you absolute hero!")
    else:
        print("The word was " + word + ". Maybe next time!")

def display_hangman(tries):
    """
    Displays different stages of hangman figure
    """
    stages = [  # end state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # just head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # base, pole and top of rope
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                # base and pole
                """
                    --------
                    |
                    |
                    |
                    |
                    |
                    -
                """,
                # base
                                """
                    -
                    |
                    |
                    |
                    |
                    |
                    -
                """,

    ]
    return stages[tries]

def main():
    main_menu()
    while input("Play Again? (Y/N) ").upper() == "Y":
        play(get_word())

if __name__ == "__main__":
    main()
