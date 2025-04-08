x=int(input("type a number : "))
match x:
    case 0:
        print("value of x is zero")
    case 4:
        print("value of x is four") 
    case _ if x!=5:
        print(x," is not equal to 5")    