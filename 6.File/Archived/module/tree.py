def pattern_tree(level, wide=False):
    # 树冠部分
    for i in range(1, level + 1):
        spaces = " " * (level - i)
        numbers = str(i) * (2 * i - 1)
        print(spaces + numbers)
    
    # 树干部分
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
