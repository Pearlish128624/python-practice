from collections import Counter

def process_records(input_file, output_file):
    input_file = 'record.txt'  # 使用相對路徑
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                name, items = line.strip().split(': ')
                count = Counter(items)
                sorted_items = ''.join(f"{count[char]}{char}" for char in sorted(count))
                outfile.write(f"{name}: {sorted_items}\n")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

process_records('record.txt', 'record_1.txt')