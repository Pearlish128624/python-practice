#四則運算
n1=int(input("please input number1: "))
n2=int(input("please input number2: "))
op=input("please input +,-,*,/ : ")

#how to prevent that n1 and n2 is also number but not random text?


if op=="+": #== please note that it is double= 
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("This calculation is not suppoted")
