# TASK 4: Closure Practice


def make_hangman(secret_word):
    """Factory function that returns a closure for playing hangman."""
    guesses = []
    
    def hangman_closure(letter):
        """Process a guessed letter and display current state."""
        # Append the guessed letter
        guesses.append(letter)
        
        # Build display: show guessed letters, underscore for others
        display = ""
        for char in secret_word.lower():
            if char in guesses:
                display += char
            else:
                display += "_"
        print(display)
        
        # Check if all letters have been guessed
        all_guessed = all(char in guesses for char in secret_word.lower())
        return all_guessed
    
    return hangman_closure


if __name__ == "__main__":
    print("=== Hangman Game ===")
    secret = input("Enter the secret word: ").strip()
    
    game = make_hangman(secret)
    
    print("\nStart guessing! Enter one letter at a time.")
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
            
        if game(guess):
            print(f"Congratulations! You guessed the word: {secret}")
            break
