																
user_input = input(" ") #e.g Give me level 5 snake with 4 corners.																
																
def matchlevel():																
    input_list = user_input.split()																
    level = int(input_list[3])																
    return level																
																
def matchcorners():																
    input_list = user_input.split()																
    corners = int(input_list[6])																
    return corners																
																
level = matchlevel()																
corners = matchcorners()																
width = (level*corners)+1
jcorners= int(corners//2)																
																
# 先建立一個足夠大的 matrix																
matrix = [[" " for _ in range(width)] for _ in range(level)]																

for i in range(level):# 往下的															
	for j in range (jcorners+1):					
		col = i + j * (level-1)*2 				
		matrix[i][col] = str(level - i) 																			

for i in range(level): # 0 1 2 3 4	#往上的															
    for j in [(level-1)*2, (level-1)*jcorners*2]: 																
        col = j - i																
        if j-i < width :																
            matrix[i][col]= str(level-i)																
        else:																
            break		
        
for row in matrix:																
    print(''.join(row))																
																
    