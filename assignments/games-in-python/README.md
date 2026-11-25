
# 📘 Assignment: Games in Python

## 🎯 Objective

Build the classic Hangman word-guessing game using Python strings, loops, conditionals, and user input to practice game logic and string manipulation.

## 📝 Tasks

### 🛠️ Game Initialization and Word Selection

#### Description
Set up the Hangman game by randomly selecting a word from a predefined list and initializing the game state.

#### Requirements
Completed program should:

- Define a list of words to choose from
- Randomly select one word at the start of the game
- Initialize game variables (attempts remaining, guessed letters, word display)
- Display the hidden word in the format: `_ _ _ _ _`

### 🛠️ Letter Guessing and Progress Tracking

#### Description
Implement the core guessing mechanism where players guess letters and see their progress updated.

#### Requirements
Completed program should:

- Accept letter guesses from the user
- Check if the guessed letter is in the word
- Update the display to reveal correctly guessed letters
- Track all previously guessed letters
- Decrement the attempts counter for incorrect guesses
- Prevent duplicate guesses

### 🛠️ Game Flow and Win/Lose Conditions

#### Description
Complete the game loop with win and lose conditions, displaying appropriate messages.

#### Requirements
Completed program should:

- Display the current game state after each guess
- Determine when the player has guessed the word (win condition)
- Determine when the player has run out of attempts (lose condition)
- Display the final word and appropriate win/lose messages
- Offer to play again or exit the game
