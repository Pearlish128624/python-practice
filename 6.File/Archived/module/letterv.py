def pattern_V(level, wide=False):
    for i in range(level, 0, -1):
        spaceout = " " * (level - i)  # 前面的空格
        
        if wide:
            if i == 1:
                print(f"{spaceout}{i}{i}")  # 最后一行只打印一个 11
            else:
                spacein = " " * (2 * i - 1)  # 修正：宽版中間的空格
                print(f"{spaceout}{i}{i}{spacein}{i}{i}")
        else:
            spacein = " " * ((level - i) * 4 + 1)  # 普通版中間的空格
            print(f"{spaceout}{i}{spacein}{i}")

pattern_V(8, False)
