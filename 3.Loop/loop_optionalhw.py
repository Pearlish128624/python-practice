def snake_with_corners(level):
    for i in range (level,0,-1): #因為從5開始，跟V一樣是倒著開始
        if i==level: #5的那行
            spacefirst=" "*(level-i)# 最前面的空
            spacemid= " "*(i*2-2) #中間1的空?
            print(spacefirst+str(i)+(spacemid+str(i))*2)
        elif i>1 and i<level: #從4-2的那幾行
            spacefirst2=" "*(level-i)
            spacemid2= " "*(i*2-3)
            spacethr2=" " * (2 * (level - i))
            print(spacefirst2 + str(i) + (spacemid2 + str(i) + spacethr2 + str(i))*2)
        else:#1那行
            space3=" "*(level-1)
            spacemid3=" "*((level-1)*2) #?
            print(space3+str(i)+(spacemid3+str(i))*2)
snake_with_corners(5)

#但是雖然似乎沒對齊..... 空格的計算有問題(不符合我一開始的公式，採用了以結果為主的公式)