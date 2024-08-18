level=5 #level= int(input("")) 嗯哼
matrix = [[0] * level for _ in range(level)] #先建立一個全部都是0的矩陣
for i in range(level):
    matrix[i][i] = i + 1
for i in range(level - 2, -1, -1): #由下往上填充，從倒數第二行(5-2=3行)，填到0行停止
    for j in range(i+1, level):  #從對角線旁邊的位置開始 (上行顯示i=3開始，i+1=則代表從第4個開始)
        matrix[i][j] = matrix[i][j - 1] + matrix[i + 1][j] #比如(1,2)位置的[5]+(2,3)位置[7]字會得到(2,3)數字的[12]
for row in matrix: #逐行列印矩陣不然會全部一行
        print(row) 
        #沒想到怎麼把 matrix 對齊的方法 -> 設定每個數字採用2位數的寬度呈現?
        #使用f-string 好像可以做到