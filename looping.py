## for loop

# colors=["red","yellow","green","blue","voilet"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)
        
# range
# for k in range(5):
#     print(k)
    
# for k in range(1,5):
#     print(k)
    
# for i in range(1,10,2):
#     print(i)

## while loop

# i=0
# while(i<=60):
#     i=int(input("enter the value of i : "))
#     print(i)
#     # i=i+1
# else:
#     print("inside else")

## do while
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break

## break and continue

# for i in range(1,12):
#     print("5 * ",i,"=",5*i)
#     if(i==10):
#         break
# print("i is greater then 10")

# for i in range(1,12):
#     if(i==10):
#         print("continue start")
#         continue
#     print("5 * ",i,"=",5*i)