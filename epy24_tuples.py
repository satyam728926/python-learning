# tup=(1,4,6,"green",True)
# print(type(tup),tup)
#else everything is same as list only it is not mutable
# if "green" in tup:
#     print("yes green is in tup")
# else:
#     print("no it is not in")

# tup2=tup[1:4]
# print(tup2)
contries=("india","south africa","england","australia")
print(contries)
l=list(contries)
l.append("indonasia")   #add
l.pop(2)   #remove
l[0]="indian"
country=tuple(l)
print(country)
tup3=(1,2,3,4)
tup4=country+tup3
print(tup4)