# Game start
import random
import csv
import os

def get_project_root():
    """Get the project root directory"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    return project_root

def ReadQuestion():
    """Read vocabulary from CSV file and return a random word and its meaning"""
    try:
        # Get the current script's directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        vocabulary_path = os.path.join(current_dir, 'source', 'vocabulary.csv')
        
        with open(vocabulary_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            vocabulary_list = list(reader)
            
            if not vocabulary_list:
                print("Error: Vocabulary file is empty")
                return None, None
                
            selected = random.choice(vocabulary_list)
            return selected['word'], selected['meaning']
            
    except FileNotFoundError:
        print(f"Error: Could not find vocabulary file at: {vocabulary_path}")
        return None, None
    except Exception as e:
        print(f"Error reading vocabulary file: {str(e)}")
        return None, None

# Initialize 
  # You can guess 10 times
  # Enter player's name
def player_name() -> str:
    player_name = input("Enter your name: ")
    return player_name

# Start guessing
def StartGuessing(word: str, meaning: str, player_name: str) -> None:
    """Main game logic"""
    lives = 10
    score = 0
    
    while True:  # Main game loop
        guessed_letters = []
        wrong_letters = []
        word_length = len(word)
        display_format = "_ " * word_length

        print(f"The word you are guessing is: {display_format.strip()}")
        print(f"This word contains {word_length} letters.")

        while lives > 0:  # Round loop
            print("\n" + "-" * 40)  # Divider line
            if wrong_letters:
                print(f"Wrong letters guessed: {', '.join(wrong_letters)}")
            
            # Input validation
            guess = ""
            while len(guess) != 1:
                guess = input("Enter a letter: ").lower()
                if guess == "exit":
                    GameOver(score)
                    return
            
            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue
            guessed_letters.append(guess)

            if guess in word:
                print("Correct guess!")
            else:
                lives -= 1
                wrong_letters.append(guess)
                print(f"Wrong guess! Lives left: {lives}")

            current_display = ''.join(letter if letter in guessed_letters else '_' for letter in word)
            print(f"Current word: {current_display}")

            if '_' not in current_display:
                print(f"You finished the word: {word}")
                print(f"The meaning of the word is: {meaning}")
                score += 1
                lives = 10
                print(f"Score: {score}")
                word, meaning = ReadQuestion()
                print(f"\nScore: {score}")
                print("\n" + "="*50 + "\n")  # Add a separator line
                print("New Round Starting!")
                print(f"The word you are guessing is: {display_format.strip()}")
                print(f"This word contains {word_length} letters.")
                break  # Break the inner loop to start a new round

            if lives <= 0:
                print(f"You died! The correct word was: {word}")
                print(f"The meaning of the word is: {meaning}")
                Died(score)
                return

# Died 
def Died(score: int) -> None:
    GameOver(score)  # Just call GameOver directly

# Game over (record score)
def GameOver(score: int) -> None:
    print(f"Game Over! Your final score is: {score}")
    # Here you can add logic to record the highest score for each player, rank players, etc.

# Main game loop
if __name__ == "__main__":
    print("Welcome to the Hangman Game!")
    player_name = player_name()
    word, meaning = ReadQuestion()  # Get the first word and its meaning
    StartGuessing(word, meaning, player_name)