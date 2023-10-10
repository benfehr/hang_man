# Hangman Game

Hangman is a word puzzle game where the player has to guess the individual letters of a word correctly before running out of lives. The lives of the player are depicted by an illustration or graphic of a gallows depicting a man being hanged by the neck.

## How to play

The player starts with an empty array of '_', which correlate to the amount of letters in the word that is being guessed. If a letter is guessed correctly, the '_' is replaced by the correct letter, revealing it's position in the word.

Every wrong letter chosen adds another piece of structure to the gallows. The game ends when either the player has guessed the word correctly, or when the player fails to guess the word, resulting in the death of the stickman.