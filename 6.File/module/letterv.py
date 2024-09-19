def pattern_V(level):
#level= int(input("Please input the level of the V: ")) 分開運行時寫的
    for i in range(level, 0, -1):
        spacein= " "*(i*2-3) #中間的空格
        spaceout=" "*(level-i) #前面的空格
        print(spaceout+str(i)+spacein+str(i))
        if i==2: #因為1只需要一個如果不停止會出現兩個1
            break
    spacefinal=" "*(level-1) #1前面的空
    print(spacefinal+str(1)) 