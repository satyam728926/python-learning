# def double(x):
#     return x*2

def appl(fx,value):
    return 6+fx(value)
double=lambda x:x*2
cube=lambda x:x*x*x
avg=lambda x,y,z:(x+y+z)/2
print(avg(5,5,5))

print(appl(lambda x:x+x,7))