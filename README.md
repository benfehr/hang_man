# Hangman Game
![Screenshot 2023-10-10 at 17 12 31](https://github.com/benfehr/hang_man/assets/113368691/2bf3d875-7054-42c4-8b44-adb9fb93abe8)

Hangman is a word puzzle game where the player has to guess the individual letters of a word correctly before running out of lives. The lives of the player are depicted by an illustration or graphic of a gallows depicting a man being hanged by the neck. 

## How to play

The player starts with an empty array of empty underscores, which correlate to the amount of letters in the word that is being guessed. If a letter is guessed correctly, the underscore is replaced by the correct letter, revealing it's position in the word. The player will have the choice of 4, 6 or 8 lives.

Every wrong letter chosen adds another piece of structure to the gallows. The game ends when either the player has guessed the word correctly, or when the player fails to guess the word, resulting in the death of the stickman.

## Target Audience
- All ages above 8.
- English speaking people.
- Anyone learning English.

## User Stories
- As a user, I would like to know how to play the game.
- As a user, I would like to know how many guesses I have left.
- As a user, I want to be able to understand the rules.
- As a user, I want to see the visual queue of the gallows representing my lives.
- As a user, I want to see how many letters are in the word that I'm trying to guess.
- As a user, I want to have the option to play the game again.
- As a user, I want to be able to choose the difficulty of the game.
- As a user, if I accidentally guess the same letter twice, I don't want to unfairly lose a life.
- As a user, I want to be able to exit the game.
- As a user, I want to be able to guess the whole word if I think I am able to do so.

## Site Aims
- Provide a mentally challenging game.
- To entertain.
- To provide a straight forward user experience.
- To provide a smooth running programme without any bugs or performance issues.

## Features

![Screenshot 2023-10-10 at 17 25 49](https://github.com/benfehr/hang_man/assets/113368691/fb11e2c6-8482-4362-88b7-02e552835898)

- The user is first greeted with a main menu. The title 'Hangman' appears in ASCII Characters, a welcome message and is then followed by 3 numberered bullet points.
- Pressing 1 begins the game, moving the user on to the next page.
- Pressing 2 shows the user the rules of play.
- Pressing 3 exits the game entirely.

## Rules

![Screenshot 2023-10-10 at 17 33 06](https://github.com/benfehr/hang_man/assets/113368691/7fbaf635-1b38-466c-a238-9202513b92f6)

- The rules are presented in an informal but understanding manner to the user.
- They are all spaced out to provide an easy to read layout.
- Pressing enter will take the user back the the main menu.

## Difficulty

![Screenshot 2023-10-10 at 17 47 03](https://github.com/benfehr/hang_man/assets/113368691/8c2b9f48-260e-4439-8769-47948a55de38)

- After pressing 1, the user will be presented with a choice of difficulty.
- The user is prompted to type either E, M or H to dictate how many chances they'll have to guess the word.

## Hangman Visual Queue and Gameplay

![Screenshot 2023-10-10 at 17 49 57](https://github.com/benfehr/hang_man/assets/113368691/cd1849ef-72c6-4c95-85ba-cd644689c998)

- As you can see the stickman figure gains appendages for each life lost, ultimately resulting in a full image of the stickman hanging.

![Screenshot 2023-10-10 at 17 53 49](https://github.com/benfehr/hang_man/assets/113368691/dd66d555-8b6e-40a5-811c-b2839eaa6229)

- The game starts with just the pole from the gallows and a blank bar of text underneath.

![Screenshot 2023-10-11 at 09 19 04](https://github.com/benfehr/hang_man/assets/113368691/a0177b61-764e-4611-b481-1e4e8803feb2)

- As the user progresses and guesses a letter correctly. they will be congratulated in the window and the letter appears on the word.

![Screenshot 2023-10-11 at 09 19 18](https://github.com/benfehr/hang_man/assets/113368691/15baf2b9-a160-4b62-b96c-ac772f2e5fd8)

- If the user guesses incorrectly they are shown this message and are prompted to guess again.

![Screenshot 2023-10-11 at 09 21 05](https://github.com/benfehr/hang_man/assets/113368691/82a42a31-674d-4a43-bc06-9d711203b639)

- When the user enters a letter that they have already guessed. they are shown this message and once again are prompted to guess again.

![Screenshot 2023-10-11 at 09 19 50](https://github.com/benfehr/hang_man/assets/113368691/77f8d4e6-6c98-4917-b784-fe9d7f748d91)

- When the user fails to guess the word they are shown this message, and also the full image of the hanging man is presented. They have the option to play the game again or exit.

![Screenshot 2023-10-11 at 09 29 10](https://github.com/benfehr/hang_man/assets/113368691/c3106864-2dec-4d03-9030-8717ed6ac032)

- If the user successfully guesses the word, they are shown this message congratulating them. They are then also given the option to play again or quit the game.

# Testing

## Python Linter Testing

![Screenshot 2023-10-11 at 09 31 36](https://github.com/benfehr/hang_man/assets/113368691/de63e150-88df-4e63-a0c7-c3a0240bfd33)

![Screenshot 2023-10-11 at 09 30 31](https://github.com/benfehr/hang_man/assets/113368691/df9ae040-9af1-4ad8-8157-f41933af4495)

- After running both of my pages of code through the Python Linter, I have successfully returned no problems with the code.

## Manual Testing

### Start Page

![Screenshot 2023-10-11 at 09 36 06](https://github.com/benfehr/hang_man/assets/113368691/546e1961-e69c-4be6-9749-7d64da2d9fdf)

- I implemented testing by typing different characters that are being asked by the user.
- The user is asked to enter 1,2 or 3. After entering different characters like letters or special characters the user is prompted to choose an option again.
- You can only enter the 1,2 or 3 characters to progress.

### Difficulty Page

![Screenshot 2023-10-11 at 09 41 39](https://github.com/benfehr/hang_man/assets/113368691/868c1706-82a7-4c88-a859-e23648744a00)

- I tested this by entering different characters than what were asked for.
- The user only has the option to E, M or H and when failed to do so are prompted to enter only those characters.

### Main Game

![Screenshot 2023-10-11 at 09 44 19](https://github.com/benfehr/hang_man/assets/113368691/f2054b0d-0d92-45a3-9df5-08ccd0fc5bd3)


- The user is able to enter a single letter or a whole word as a guess.
- If guessing a whole word, it has to be the same length as the word onscreen, otherwise it won't be valid and the user is told so.
- If the user enters a number, this is also not a valid guess and they are told by a message on the screen.
- You can only progess through the game with valid guesses of single letters, or words with the appropriate length.

## Bugs

- Upon the initial first launch of the app the heroku, I encountered a few issues with the lengths of some of the code being too long, and some of the ascii art I had used not being legible
- I had to shorten a few lines of code and re do the ASCII characters to a font that was easier to read and wasn't being pushed onto the next line because of the character limit the python has.
- I had a lot of empty whitespace problems when first uploading the code to the linter, and this was also because of the ASCII characters I had in the project. This was fixed by just deleting all the whitespace until no problems were showing

## Deployment

1. Push code to GitHub after git add . and finishing commits.
2. Log in or Sign up to Heroku.
3. Select a unique name, I went for Hangeth the man as this was available.
4. In the settings tab reveal the config vars.
5. For KEY, input PORT and for VALUE, imput 8000 and click add.
6. Click add buildpack and select Python.
7. Click add buildpack again and select Nodejs.
8. Python should be above Nodejs on the list. If it isn't the app may not work correctly once deployed
9. Go to deploy tab and select GitHub and connect to your GitHub account.
10. Search for the repository you want to deploy. Connect it.
11. I then chose to automatically update the app so I had the option to see it in the Heroku app window for testing
12. After doing this correctly you will be given a link to the live app

Mine can be found here:

https://hangeth-the-man-0a903a59cc73.herokuapp.com/


## Flowchart

![Screenshot 2023-10-11 at 10 18 31](https://github.com/benfehr/hang_man/assets/113368691/fb397bb1-6d9c-4209-a607-2b8ef44e8b6a)

- Created on Drawio

# Credits

- To Richard Wells my mentor for helping me to fully understand the logic of the game
- ASCII art generator at https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
- Youtube tutorial from Shaun Halverson to help me understand the code https://www.youtube.com/watch?v=pFvSb7cb_Us
- Youtube tutorial from Kite where I found the character drawings of the Hangman https://www.youtube.com/watch?v=m4nEnsavl6w

