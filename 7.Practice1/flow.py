# Game start

# Read quesiton (1000 words)
  # Choose 1 of them, and get it's length
  # EX. cat -> _ _ _
import random

def ReadQuestion() -> tuple:
    # Read the file from the specified path
    file_path = r"C:\Users\sunni\OneDrive1\OneDrive\Python\240701\python-practice\7.Practice1\source\1000.txt"
    
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.readlines()  # Read all lines from the file

    # Pick one word randomly
    chosen_line = random.choice(words).strip()  # Select a random line
    parts = chosen_line.split('\t')  # Split by tab to separate word and meaning
    chosen_word = parts[1]  # Get the word (second element)
    meaning = parts[2] if len(parts) > 2 else "Meaning not found."  # Get the meaning (third element)

    return chosen_word, meaning  # Return the chosen word and its meaning

# Initialize 
  # You can guess 10 times
  # Enter player's name
def Initialize() -> str:
    player_name = input("Enter your name: ")
    return player_name

# Start guessing
def StartGuessing(word: str, meaning: str, player_name: str) -> None:
    lives = 10
    guessed_letters = []
    score = 0
    word_length = len(word)
    display_format = "_ " * word_length  # Create a string of underscores

    print(f"The chosen word is: {display_format.strip()}")  # Show the underscores
    print(f"This word contains {word_length} letters.")  # Show the length of the word

    while lives > 0:
        guess = input("Enter a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            lives -= 1
            print(f"Wrong guess! Lives left: {lives}")

        # Display current state of the word
        current_display = ''.join(letter if letter in guessed_letters else '_' for letter in word)
        print(f"Current word: {current_display}")

        # Check for game over conditions
        if '_' not in current_display:
            print(f"You finished the word: {word}")
            print(f"Meaning: {meaning}")  # Show the meaning of the word
            score += 1
            lives = 10  # Reset lives to 10 for the next round
            print(f"Score: {score}")
            word, meaning = ReadQuestion()  # Get a new word and its meaning for the next round
            display_format = "_ " * len(word)  # Update display format
            print(f"The chosen word is: {display_format.strip()}")  # Show the underscores
            print(f"This word contains {len(word)} letters.")  # Show the length of the new word

        # Check for game over conditions
        if lives <= 0:
            print(f"You died! The correct word was: {word}")
            print(f"Meaning: {meaning}")  # Show the meaning of the word
            Died(score)

# Died 
def Died(score: int) -> None:
    print(f"You died! Your score was: {score}")
    GameOver(score)

# Game over (record score)
def GameOver(score: int) -> None:
    print(f"Game over! Your final score is: {score}")
    # Here you can add logic to record the highest score for each player, rank players, etc.

# Main game loop
if __name__ == "__main__":
    print("Welcome to the Hangman Game!")
    player_name = Initialize()
    word, meaning = ReadQuestion()  # Get the first word and its meaning
    StartGuessing(word, meaning, player_name)
    