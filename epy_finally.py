# a=input("enter the number : ")
# print(f"multiplication table of {a} is :")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} * {i} = {int(a)*i}")
# # except Exception as e:
# except:
#     print("invalid input!")

# print("some line of code")
# print("en of the program")
#different type of error
def func1():
    try:
        a=[2,3,4,5,5,6,78]
        i=int(input("enter the index "))
        print(a[i])
        return 1
    except :
        print("entered index is out of scope")
        return 0
    finally:#if you want to clean something or remve conneciton
        print("i am always executed")

x=func1()
print(x)
