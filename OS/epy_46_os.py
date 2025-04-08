import os
# if(not os.path.exists("rename")):
#     os.dir("rename")

# for i in range(1,100):
#     os.rename(f"data/tutorial{i}",f"data/tutorial {i}")

folders=os.listdir("data")
print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))