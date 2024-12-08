import csv
import os

def transform_to_csv(input_file: str, output_file: str) -> None:
    """Transform text file to CSV format"""
    try:
        # Get all lines from the text file
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Create CSV with all data
        with open(output_file, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['word', 'meaning'])
            
            for line in lines:
                # Skip empty lines
                if not line.strip():
                    continue
                    
                # Split by tab first
                parts = line.strip().split('\t')
                if len(parts) >= 2:
                    # Process the first part (id and word)
                    id_word = parts[0].split('.')
                    if len(id_word) >= 2:
                        word = id_word[1].strip()
                        # Process the meaning part
                        meaning = parts[1].strip()
                        writer.writerow([word, meaning])

        print(f"Successfully created CSV file: {output_file}")
        print(f"Processed {sum(1 for line in open(output_file, encoding='utf-8')) - 1} words")  # -1 for header
        
    except Exception as e:
        print(f"Error during transformation: {str(e)}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "source", "1000.txt")
    output_file = os.path.join(current_dir, "source", "vocabulary.csv")
    
    transform_to_csv(input_file, output_file)
