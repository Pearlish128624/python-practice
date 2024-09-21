import os
import sys
from io import StringIO

def pattern_V(level, wide=False):
    for i in range(level, 0, -1):
        spaceout = " " * (level - i)  # 前面的空格
        
        if i == 1:
            if wide:
                print(f"{spaceout}{i}{i}")  # 最后一行只打印一个 11
            else:
                print(f"{spaceout}{i}")  # 非 wide 模式最后一行只打印一个 1
        else:
            spacein = " " * (2 * i - 3)  # 中間的空格
            if wide:
                print(f"{spaceout}{i}{i}{spacein}{i}{i}")
            else:
                print(f"{spaceout}{i}{spacein}{i}")

def pattern_ladder(level, wide=False):
    for i in range(1, level + 1):
        if wide:
            print(f"{i}-{str(i) * i}")
        else:
            print(str(i) * i)

def pattern_tree(level, wide=False):
    # 樹葉部分
    for i in range(1, level + 1):
        spaces = " " * (level - i)
        numbers = str(i) * (2 * i - 1)
        print(spaces + numbers)
    
    # 樹幹部分
    if wide:
        trunk_width = len(str(level))
        for i in range(level, 0, -1):
            spaces = " " * (level - trunk_width // 2 - 1)
            trunk = str(i).center(trunk_width)
            print(spaces + trunk)
    else:
        for i in range(level, 0, -1):
            spaces = " " * (level - 1)
            print(spaces + str(i))

def read_orders(orders_dir):
    orders = []
    for root, dirs, files in os.walk(orders_dir):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(root, file), 'r') as f:
                    orders.extend(f.read().splitlines())
    return orders

def process_order(order):
    words = order.lower().split()
    level = None
    pattern_type = None
    wide = False

    for word in words:
        if word.isdigit():
            level = int(word)
        elif word in ["tree", "v", "ladder", "tree.", "v.", "ladder."]:
            pattern_type = word.rstrip('.')
        elif word == "wide":
            wide = True

    if level is None or pattern_type is None:
        raise ValueError(f"Invalid order format: '{order}'. Missing level or pattern type")

    return pattern_type, level, wide

def create_pattern(pattern_type, level, wide):
    # 捕获打印输出
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    if pattern_type == "tree":
        pattern_tree(level, wide)
    elif pattern_type == "v":
        pattern_V(level, wide)
    elif pattern_type == "ladder":
        pattern_ladder(level, wide)
    else:
        raise ValueError(f"Unknown pattern type: {pattern_type}")

    pattern = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return pattern

def save_pattern(pattern, filename):
    with open(filename, 'w') as f:
        f.write(pattern)

def main():
    # 使用绝对路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    orders_dir = os.path.join(base_dir, 'orders')
    products_dir = os.path.join(base_dir, 'products')
    
    if not os.path.exists(orders_dir):
        raise FileNotFoundError(f"Orders directory not found: {orders_dir}")
    
    if not os.path.exists(products_dir):
        os.makedirs(products_dir)
    
    orders = read_orders(orders_dir)
    if not orders:
        print(f"No order files found in {orders_dir}")
        return

    results = {"ladder": [], "tree": [], "v": []}
    
    for order in orders:
        try:
            pattern_type, level, wide = process_order(order)
            pattern = create_pattern(pattern_type, level, wide)
            if pattern is not None:
                results[pattern_type].append(pattern)
                print(f"Processed order: '{order}'")
                print(f"Type: {pattern_type}, Level: {level}, Wide: {wide}")
                print("Pattern:")
                print(pattern)
                print("-" * 40)
            else:
                print(f"Failed to create pattern for order: '{order}'")
        except ValueError as e:
            print(f"Error processing order: {e}")

    # 保存结果到文件
    for pattern_type, patterns in results.items():
        filename = os.path.join(products_dir, f"{pattern_type.capitalize()}.txt")
        with open(filename, 'w') as f:
            for pattern in patterns:
                f.write(pattern + "\n\n")
        print(f"Saved {pattern_type} patterns to {filename}")

if __name__ == "__main__":
    main()
