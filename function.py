# ##user defind function
# ## build in function

# a=2
# b=3
# gmean=(a*b)/(a+b)
# print(gmean)
# #funciton
# def calculategmean(a,b):
#     mean=(a*b)/(a+b)
#     print(mean)
# def isgreater(a,b):
#     if(a>b):
#         print("a>b")
#     else:
#         print("b>a")    
# calculategmean(2,3)
# isgreater(2,3)
# calculategmean(4,5)
# isgreater(4,5)

##a arguments
#default argue
# def average(a=9,b=1):
#     print("average is = ",(a+b/2))

# average() #assumed that the value of a nd is given by default
# ##keyword argument
# average(a=12,b=34)

# def average(*numbers):
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("average of numbers is ",sum/len(numbers))

# average(12,12,3,13,13)

def name(**name):
    print("fname is ", name["fname"],"middle name is ",name["mname"],"lname is ",name["lname"])

name(fname="Satyam",mname="abhay",lname="pandey")