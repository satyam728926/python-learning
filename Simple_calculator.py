a=int(input("enter the value of a :"))
b=int(input("enter the value of b :"))
oper=str(input("choos any of the below option\n1-add\n2-subs\n3-divis\n4-multip\n"))
if(oper=="1"):
    print("result = ",a+b)
elif(oper=="2"):
    print("result = ",a-b)
elif(oper=="3"):
    print("result = ",a/b)
elif(oper=="4"):
    print("result = ",a*b)    
else:
    print("no such operation")
    
