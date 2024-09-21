def pattern_V(level, wide=False):
    for i in range(level, 0, -1):
        spaceout = " " * (level - i)  # 前面的空格
        
        if wide:
            spacein = " " * (i * 2 - 1)  # 宽版中間的空格
            print(spaceout + str(i) * 2 + spacein + str(i) * 2)
        else:
            spacein = " " * (i * 2 - 3)  # 普通版中間的空格
            print(spaceout + str(i) + spacein + str(i))
            if i == 2:  # 普通版在 i=2 时停止循环
                break
    
    spacefinal = " " * (level - 1)  # 最后一行前面的空格
    if wide:
        print(spacefinal + str(1) * 2)  # 宽版最后一行打印两个1
    else:
        print(spacefinal + str(1))  # 普通版最后一行打印一个1