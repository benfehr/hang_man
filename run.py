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
    print("Guess a letter")
    print("Guess another letter")
    print("Think, 'what letter could be next?' ")
    print("Guess another letter or if you're a genius, try and guess the whole word")
    print("If you run out of letters, then Mr Stickman shall be hung by the neck until they are dead")
    input("press enter to return to main menu")
    main_menu()

def select_difficulty():
    """
    Allows user to select how many chances they have to complete the game
    """
    print("Choose a difficulty")
    print("Type E for easy (8 Lives)")
    print("Type M for medium (6 Lives)")
    print("Type H for hard (4 Lives)")
    can_continue = False

    while not = can_continue:
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
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def display_hangman(tries):
    """
    Displays different stages of hangman figure to show user how many attempts remain"
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