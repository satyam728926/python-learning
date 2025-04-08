s={2,2,2,24,43,131}
print(s)
##unordered not sure about the order
#duplicate value no accept
satyam={}
print(type(satyam))
satyam1=set()
print(type(satyam1))

##sets methods

s1={1,2,3,4,5}
s2={3,5,1,3}
# print(s1.union(s2))
s1.update(s2)
print(s1)

##same goes with intrsecitpn
s1.symmetric_difference(s1)
print(s1)
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s2.issuperset(s1))
##remove does give error but no discard
del s1
print(s1)
s1={1,2,3,4,5}
s1.clear
print(s1)