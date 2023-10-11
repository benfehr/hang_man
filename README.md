# Hangman Game
![Screenshot 2023-10-10 at 17 12 31](https://github.com/benfehr/hang_man/assets/113368691/2bf3d875-7054-42c4-8b44-adb9fb93abe8)

Hangman is a word puzzle game where the player has to guess the individual letters of a word correctly before running out of lives. The lives of the player are depicted by an illustration or graphic of a gallows depicting a man being hanged by the neck. 

## How to play

The player starts with an empty array of empty underscores, which correlate to the amount of letters in the word that is being guessed. If a letter is guessed correctly, the underscore is replaced by the correct letter, revealing it's position in the word. The player will have the choice of 4, 6 or 8 lives.

Every wrong letter chosen adds another piece of structure to the gallows. The game ends when either the player has guessed the word correctly, or when the player fails to guess the word, resulting in the death of the stickman.

## Target Audience
- All ages above 8
- English speaking people
- Anyone learning English

## User Stories
- As a user, I would like to know how to play the game
- As a user, I would like to know how many guesses I have left
- As a user, I want to be able to understand the rules
- As a user, I want to see the visual queue of the gallows representing my lives
- As a user, I want to see how many letters are in the word that I'm trying to guess
- As a user, I want to have the option to play the game again
- As a user, I want to be able to choose the difficulty of the game
- As a user, if I accidentally guess the same letter twice, I don't want to unfairly lose a life
- As a user, I want to be able to exit the game
- As a user, I want to be able to guess the whole word if I think I am able to do so

## Site Aims
- Provide a mentally challenging game
- To entertain
- To provide a straight forward user experience
- To provide a smooth running programme without any bugs or performance issues

## Features

![Screenshot 2023-10-10 at 17 25 49](https://github.com/benfehr/hang_man/assets/113368691/fb11e2c6-8482-4362-88b7-02e552835898)

- The user is first greeted with a main menu. The title 'Hangman' appears in ASCII Characters, a welcome message and is then followed by 3 numberered bullet points.
- Pressing 1 begins the game, moving the user on to the next page.
- Pressing 2 shows the user the rules of play
- Pressing 3 exits the game entirely

## Rules

![Screenshot 2023-10-10 at 17 33 06](https://github.com/benfehr/hang_man/assets/113368691/7fbaf635-1b38-466c-a238-9202513b92f6)

- The rules are presented in an informal but understanding manner to the user.
- They are all spaced out to provide an easy to read layout
- Pressing enter will take the user back the the main menu

## Difficulty

![Screenshot 2023-10-10 at 17 47 03](https://github.com/benfehr/hang_man/assets/113368691/8c2b9f48-260e-4439-8769-47948a55de38)

- After pressing 1, the user will be presented with a choice of difficulty
- The user is prompted to type either E, M or H to dictate how many chances they'll have to guess the word

## Hangman Visual Queue and Gameplay

![Screenshot 2023-10-10 at 17 49 57](https://github.com/benfehr/hang_man/assets/113368691/cd1849ef-72c6-4c95-85ba-cd644689c998)

- As you can see the stickman figure gains appendages for each life lost, ultimately resulting in a full image of the stickman hanging

![Screenshot 2023-10-10 at 17 53 49](https://github.com/benfehr/hang_man/assets/113368691/dd66d555-8b6e-40a5-811c-b2839eaa6229)

- The game starts with just the pole from the gallows and a blank bar of text underneath

![Screenshot 2023-10-11 at 09 19 04](https://github.com/benfehr/hang_man/assets/113368691/a0177b61-764e-4611-b481-1e4e8803feb2)

- As the user progresses and guesses a letter correctly. they will be congratulated in the window and the letter appears on the word

![Screenshot 2023-10-11 at 09 19 18](https://github.com/benfehr/hang_man/assets/113368691/15baf2b9-a160-4b62-b96c-ac772f2e5fd8)

- If the user guesses incorrectly they are shown this message and are prompted to guess again

![Screenshot 2023-10-11 at 09 21 05](https://github.com/benfehr/hang_man/assets/113368691/82a42a31-674d-4a43-bc06-9d711203b639)

- When the user enters a letter that they have already guessed. they are shown this message and once again are prompted to guess again

![Screenshot 2023-10-11 at 09 19 50](https://github.com/benfehr/hang_man/assets/113368691/77f8d4e6-6c98-4917-b784-fe9d7f748d91)

- When the user fails to guess the word they are shown this message, and also the full image of the hanging man is presented. They have the option to play the game again or exit.

![Screenshot 2023-10-11 at 09 29 10](https://github.com/benfehr/hang_man/assets/113368691/c3106864-2dec-4d03-9030-8717ed6ac032)

- If the user successfully guesses the word, they are shown this message congratulating them. They are then also given the option to play again or quit the game.