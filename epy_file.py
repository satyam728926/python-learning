# f=open("myfile.txt",'r')
# # print(f)
# text=f.read()
# print(text)
# f.close(f)
# f=open("myfile.txt",'w')
# text=f.write("hello world")
# f.close()
# r=open("myfile.txt",'r')
# print(r.read())
# r.close()

# with open("myfile.txt","a") as f:
#     f.write("hey i am in")
# f=open("myfile.txt",'r')
# for i in range(0,3):
#     line=f.readline()
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     # print(m1)
    
#     print(f"mark of student {i} in maths is :{m1}")
#     print(f"mark of student {i} in english is :{m2}")
#     print(f"mark of student {i} in sst is :{m3}")
#     print(line)

# with open("myfile.txt",'r') as f:
#     print(type(f))
# # move the cursor to specific file
#     see=f.seek(10)
#     # tell return the curnt pos in file
#     print(f.tell())
#     data=f.read(5)
#     print(data)
with open('myfile.txt','w') as f:
    f.write("hello world")
    f.truncate(5)
    



