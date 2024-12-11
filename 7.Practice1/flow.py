# Game start
import random
import csv
import os
from datetime import datetime

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
                    GameOver(word, meaning, score, player_name)
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
                print("\n" + "="*50 + "\n")  # Add a separator line
                print("New Round Starting!")
                break  # Break the inner loop to start a new round

            if lives <= 0:
                GameOver(word, meaning, score, player_name)
                return

# Game over (record score)
def GameOver(word: str, meaning: str, score: int, player_name: str) -> None:
    """Handle game over logic"""
    print(f"You died! The correct word was: {word}")
    print(f"The meaning of the word is: {meaning}")
    print(f"Game Over! Your final score is: {score}")
    
    # Add rank functionality
    update_rank(player_name, score)
    show_rank = input("\nWould you like to check the rank? (y/n): ").lower()
    if show_rank == 'y':
        display_rank()

def update_rank(player_name: str, score: int) -> None:
    """Update the rank with new score"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    rank_path = os.path.join(current_dir, 'source', 'rank.csv')
    
    # Read existing rank
    rank_data = {}
    if os.path.exists(rank_path):
        with open(rank_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['player_name']
                if name not in rank_data or int(row['score']) < int(score):
                    rank_data[name] = {
                        'score': int(row['score']),
                        'datetime': row['datetime']
                    }
    
    # Update current player's score if it's higher
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if player_name not in rank_data or rank_data[player_name]['score'] < score:
        rank_data[player_name] = {
            'score': score,
            'datetime': current_time
        }
    
    # Write updated rank
    with open(rank_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['player_name', 'score', 'datetime'])
        for name, data in sorted(rank_data.items(), key=lambda x: (-x[1]['score'], x[0])):
            writer.writerow([name, data['score'], data['datetime']])

def display_rank() -> None:
    """Display the current rank"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    rank_path = os.path.join(current_dir, 'source', 'rank.csv')
    
    if not os.path.exists(rank_path):
        print("\nNo rank data available yet!")
        return
        
    print("\n" + "="*50)
    print("\nRANK")
    print("="*50)
    print(f"{'Rank':<6}{'Player':<15}{'Score':<8}{'Date/Time':<20}")
    print("-"*50)
    
    with open(rank_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader, 1):
            print(f"{i:<6}{row['player_name']:<15}{row['score']:<8}{row['datetime']:<20}")
    print("="*50 + "\n")

# Main game loop
if __name__ == "__main__":
    while True:
        print("Welcome to the Hangman Game!")
        name = player_name()
        word, meaning = ReadQuestion()  # Get the first word and its meaning
        if word is None or meaning is None:
            print("Error: Could not load vocabulary.")
            break
        StartGuessing(word, meaning, name)
        
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            break
    print("\nThanks for playing!")