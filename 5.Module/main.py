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