import random

def test_read_question():
    file_path = r"C:\Users\sunni\OneDrive1\OneDrive\Python\240701\python-practice\7.Practice1\source\1000.txt"
    
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.readlines()
    
    # Print 5 random lines to check the format
    print("Testing 5 random words from the file:")
    for _ in range(5):
        chosen_line = random.choice(words).strip()
        parts = chosen_line.split()
        
        # Extract word and meaning
        first_part = parts[0].split('.')  # Split the "487.flu" into ["487", "flu"]
        word = first_part[1]  # Get the word after the number
        meaning = ' '.join(parts[1:])  # Get everything after the word
        
        print("\n------------------------")
        print(f"Original line: {chosen_line}")
        print(f"Word to guess: {word}")
        print(f"Word length: {len(word)}")
        print(f"Display format: {'_ ' * len(word)}")
        print(f"Meaning: {meaning}")

# Run the test
if __name__ == "__main__":
    test_read_question() 