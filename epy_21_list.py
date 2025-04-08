l=[1,2,3,4,5,"satyam",True]
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])
# print(l[5])
# print(l[6])
# print(type(l))
# print(l[-3])
# if "satyam" in l:
#     print("Yes")
# else:
#     print("no")    
    ## same thing applies for string as well
# print(l)
# print(l[1:-1])
# print(l[1:5:2])
#list comprehesnion
# lst=[i for i in range(5)]
# print(lst)
# lst1=[i+i for i in range(10)]
# print(lst1)
# lst2=[i+i for i  in range(10) if i%2==0]
# print(lst2)

#list function
l=[1,2,3,4,5]
l.append(29)
# # print(l)
# l.sort()
# # print(l)
# l.reverse()
# print(l)
# print(l.index(4))
# m=l
# m[0]=0
# print(l)
#in above case m is reference of l but no copied on m for that you need to copy l into m
# m=l.copy()
# m[0]=0
# print(l)

l.insert(3,199)
print(l)
m=[12,12,13]
l.extend(m)
print(l)
k=[13,13,41,41]
l=m+k
print(l )