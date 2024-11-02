# Game start
import random
# Read quesiton (1000 words)
# Choose 1 of them, and get it's length
# EX. cat -> _ _ _
def ReadQuestion() -> tuple:
    # Read the file from the specified path
    file_path = r"C:\Users\sunni\OneDrive1\OneDrive\Python\240701\python-practice\7.Practice1\source\1000.txt"
    
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.readlines()  # Read all lines from the file

    # Pick one word randomly
    chosen_line = random.choice(words).strip()  # Select a random line
    parts = chosen_line.split()  # Split by space
    
    # Extract word and meaning
    first_part = parts[0].split('.')  # Split the "487.flu" into ["487", "flu"]
    word = first_part[1]  # Get the word after the number
    meaning = ' '.join(parts[1:])  # Get everything after the word
    
    return word, meaning

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
    display_format = "_ " * word_length

    print(f"The word you are guessing is: {display_format.strip()}")
    print(f"This word contains {word_length} letters.")

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

        current_display = ''.join(letter if letter in guessed_letters else '_' for letter in word)
        print(f"Current word: {current_display}")

        if '_' not in current_display:
            print(f"You finished the word: {word}")
            print(f"Meaning: {meaning}")
            score += 1
            lives = 10
            guessed_letters = []
            print(f"Score: {score}")
            word, meaning = ReadQuestion()
            display_format = "_ " * len(word)
            print(f"The word you are guessing is: {display_format.strip()}")
            print(f"This word contains {len(word)} letters.")

        if lives <= 0:
            print(f"You died! The correct word was: {word}")
            print(f"Meaning: {meaning}")
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
    