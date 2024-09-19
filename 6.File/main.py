import os
from module.ladder import pattern_ladder
from module.tree import pattern_tree
from module.letterv import pattern_V

def read_orders(orders_dir):
    orders = []
    for root, dirs, files in os.walk(orders_dir):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(root, file), 'r') as f:
                    orders.append(f.read().strip())
    return orders

def process_order(order): #需要重新寫 因為會友wide pattern 出現
    parts = order.split()
    level = int(parts[-2])
    pattern_type = parts[-1].lower().rstrip('.')
    return pattern_type, level

def create_pattern(pattern_type, level): #重新考量一下
    if pattern_type == "ladder":
        return pattern_ladder(level)
    elif pattern_type == "tree":
        return pattern_tree(level)
    elif pattern_type == "v":
        return pattern_V(level)
    else:
        return "We don't support this pattern."

def save_results(results, products_dir): 
    for pattern_type, patterns in results.items():
        filename = f"{pattern_type.capitalize()}.txt"
        with open(os.path.join(products_dir, filename), 'w') as f:
            for pattern in patterns:
                f.write(pattern + "\n\n")

def main():
    orders_dir = './orders'
    products_dir = './products'
    
    if not os.path.exists(products_dir):
        os.makedirs(products_dir)
    
    orders = read_orders(orders_dir)
    results = {"ladder": [], "tree": [], "v": []}
    
    for order in orders:
        pattern_type, level = process_order(order)
        pattern = create_pattern(pattern_type, level)
        results[pattern_type].append(pattern)
    
    save_results(results, products_dir)
    print("All orders have been processed and saved in the products folder.")

if __name__ == "__main__":
    main()
