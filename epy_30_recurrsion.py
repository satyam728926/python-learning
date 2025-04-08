def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))
# 5*factorial(4)
# 5*4*factorial(3)
# 5*4*3*factorial(2)
# 5*4*3*2*factorial(1)
# 5*4*3*2*1

def fibonaci(n):
    if(n==0):
        return 0
    elif(n==1):
        return(1)
    else:
        return fibonaci(n-1)+fibonaci(n-2)
    
print(fibonaci(5))
