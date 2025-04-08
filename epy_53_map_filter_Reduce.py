# map function
cube=lambda x:x*x*x
l1=[1,2,3,4,5,6,20,40,11]
# l2=[]
# for i in range(len(l1)):
#     l2.append(cube(i))
# l2=list(map(cube,l1))
# print(l2)

# filter
# def filter_function(a):
#   return a>10

# l2=list(filter(filter_function,l1))
# print(l2)
from functools import reduce

sum=reduce(lambda x,y:x+y,l1)
print(sum)