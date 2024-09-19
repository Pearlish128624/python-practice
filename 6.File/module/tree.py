def pattern_tree(level):
    if level % 2 == 0:
        print("The level of the tree must be odd.")
    else:
        for i in range (1,level+1): # 樹
            spaces = " " * (level - i)  # 前面的空格，使數字居中
            numbers = str(i) * (i*2-1)  # 生成該行的數字，數量是2*i-1
            print(spaces + numbers)  

        for i in range(level, 0, -1):  # 迴圈從 level 到 1, -1是步長，這樣數列才會倒序。
            spaces = " " * (level - 1)  # 每行需要的前置空格數量固定
            print(spaces + str(i))  # 樹幹
        