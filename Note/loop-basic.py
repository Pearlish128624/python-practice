# while loop -> please note that it might become endless result
# 1+2+3+...+10
"""
n=0
sum=0 #record sum
while n<=10:
    if n==5:
        break
    sum=sum+n
    n+=1
print(sum) #only print 1+2+3+4=10(n==5 stop the loop and print sum)
# for loop
#sum=0
#for x in range(1,11):
    #sum=sum+x
#print(sum)
"""
'''
n=0
for x in [0,1,2,3]:
    if x%2==0: #X是偶數
        continue #0,2 就不會print 也不會加, 因此n只會+1 +1 共兩次
    print(x)
    n+=1
print("final n:",n)
'''
'''
sum=0
for n in range(11):
    sum+=n
else:
    print(sum) 
'''

#找出整數平方根
# input 9 output 3
# input 11 output can't get valid number 
n=input("please input a number: ")
n=int(n)
for i in range(n): # from n to n-1
    if i*i==n:
        print("整數平方根: ",i)
        break #用 break 結束loop不會跑 else
else:
    print("沒有整數平方根")

