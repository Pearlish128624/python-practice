
def pattern_ladder(level):
    #level = int(input("Please input the level of ladder you want: ")) 這是我分開寫寫的
    for i in range(1, level + 1):
        print(str(i) * i)

def pattern_tree(level):
    if level % 2 == 0:
        print("The level of the tree must be odd.")
    else:
        for i in range (1,level+1): # 樹
            spaces = " " * (level - i)  # 前置空格，使數字居中
            numbers = str(i) * (i*2-1)  # 生成該行的數字，數量是2*i-1
            print(spaces + numbers)  # 拼接空格和數字並打印

        for i in range(level, 0, -1):  # 迴圈從 level 到 1, -1是步長，使數列倒序。
            spaces = " " * (level - 1)  # 每行需要的前置空格數量固定
            print(spaces + str(i))  # 樹幹
        
def pattern_V(level):
#level= int(input("Please input the level of the V: ")) 分開運行時寫的
    for i in range(level, 0, -1):
        spacein= " "*(i*2-3)
        spaceout=" "*(level-i)
        print(spaceout+str(i)+spacein+str(i))
        if i==2:
            break
    spacefinal=" "*(level-1)
    print(spacefinal+str(1))

def main():
    pattern_type = input("Please input the pattern（ladder, tree, V）: ").lower() #確保變成小寫==才有作用
    level = int(input("please input the level: "))
    if level>9 or level<=0:
        print("The level need to between 1-9")
    else:
        if pattern_type=="ladder":
            pattern_ladder(level)
        elif pattern_type=="tree":
            pattern_tree(level)
        elif pattern_type=="v":
            pattern_V(level)
        else:
            print("We don't support this pattern.")

main()