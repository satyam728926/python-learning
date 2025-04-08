import time;

Crnt_hr=int(time.strftime('%H'))
crnt_zone=time.strftime('%p')
print(crnt_zone)

# print(Crnt_hr)
if(Crnt_hr>12):
    Crnt_hr_in=int(Crnt_hr-12)

if(Crnt_hr_in<12):
    if(crnt_zone=="AM"):
        print("good morning")
    elif(Crnt_hr_in>12 and Crnt_hr_in <4):
        print("good evening")        
    else:
        print("good night time is",Crnt_hr_in ,crnt_zone)