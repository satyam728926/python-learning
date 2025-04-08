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
try:
    num=int(input("enter a number "))
    a=[2,3]
    print(a[num])
except ValueError:
    print("entered number is not a integar")
except IndexError:
    print("entered index is out of scope")