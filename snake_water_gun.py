#    s   w   g
# s  d   1  -1
# w -1   d   1
# g  1  -1   d

import numpy as np
import random
option=["snake","water","gun"]
dic_option={"snake":0,"water":1,"gun":2}
matrix=np.array([["Draw","win","loose"],["loose","Draw","win"],["win","loose","Draw"]])
# print(matrix[0,0])f
comp_choice=random.choice(option)
user_choice=input(f"enter the value of {option}\n")
result=matrix[dic_option[user_choice],dic_option[comp_choice]]
if result=="win":
    print(f"Hurray you win since machine choosed {comp_choice}")
elif result=="loose":
    print(f"Oooopsie you lost since machine choosed {comp_choice}")
else:
    print("Its draw")


    



