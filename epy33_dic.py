dic1={
    "name":"Satyam",
    "age":24
}
# print(dic1["age"])
# print(dic1)
# for i in dic1.keys():
#     print (f" the value of key {i} is {dic1[i]}")
# print(dic1.items())

###dic methods

ep={1:12,2:23,3:34,4:34}
ep1={5:12,6:23,7:34,8:34}
ep.update(ep1)
# ep.clear()
# ep.pop(3)
del ep[2]
print(ep)