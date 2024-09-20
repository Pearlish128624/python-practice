def pattern_ladder(level, wide=False):
    for i in range(1, level + 1):
        if wide:
            print(f"{i}-{str(i) * i}")
        else:
            print(str(i) * i)