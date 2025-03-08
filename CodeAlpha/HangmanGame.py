import random  # Importing the random module to randomly select a word

# Function to choose a random word from a predefined list
def choose_word():
    words = ['python', 'romaisa', 'meet', 'developer', 'hangman', 'function', 'variable', 'algorithm', 'computer']
    return random.choice(words)  # Randomly selecting and returning a word from the list

# Function to display the word with guessed letters revealed and unknown letters as underscores
def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

# Main function to run the Hangman game
def hangman():
    word = choose_word()  # Selecting a random word
    guessed_letters = set()  # Creating an empty set to store guessed letters
    attempts = 6  # Setting the number of allowed incorrect attempts

    print("Welcome to Hangman!")  # Displaying welcome message

    # Game loop: Runs until the player runs out of attempts or guesses the word
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))  # Displaying the current progress of the word
        print(f"Attempts left: {attempts}")  # Showing remaining attempts
        guess = input("Guess a letter: ").lower()  # Taking user input and converting it to lowercase

        # Validating user input to ensure it's a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue  # Skipping the rest of the loop iteration if input is invalid

        # Checking if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue  # Skipping to the next loop iteration

        guessed_letters.add(guess)  # Adding the guessed letter to the set

        # Checking if the guessed letter is in the word
        if guess not in word:
            attempts -= 1  # Reducing attempts for incorrect guesses
            print("Incorrect guess!")

        # Checking if all letters in the word have been guessed
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break  # Exiting the loop if the word is completely guessed
    else:
        # If the loop ends without a correct guess, the game is over
        print("\nGame over! The word was:", word)

# Ensuring the script runs only if executed directly (not when imported)
if __name__ == "__main__":
    hangman()
