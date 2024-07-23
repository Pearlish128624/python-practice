# 集合的運算
#s1={3,4,5}
#print(3 in s1)#有就會出現 True
#s1={3,4,5}
#s2={4,5,6,7}
#s3=s1&s2 #交集:使用& 取兩個集合中相同的資料
#s3=s1|s2  #聯集: 把所有人放進來、但不重複資料
#s3=s1-s2 #差集: 從s1中減去和s2重疊的部分
#s3=s1^s2 #反交集: 取兩個集合中不重疊的部分
#print(s3)

#s=set("Hello") #set(字串) 會自動拆解字串中的文字變成集合
#print(s)

##字典
#dic={"apple":"蘋果","bug":"蟲"}
#dic["apple"]="小蘋果" 更改字典
#print(dic["apple"])
#print("apple" in dic) #判斷key是否存在
#print(dic)
#del dic["apple"] #刪除字典中整個鍵值對
#print (dic)

dic={x:x*2 for x in [3,4,5]} #從列表的資料產生字典
print(dic)