a=input("enter any value between 5 and 9")
if a=="quit":
    print("valid")
    
else:
    b=int(a)
    if b<5 or b>9:

        raise ValueError("value in between 5 and 9")

#custom error
