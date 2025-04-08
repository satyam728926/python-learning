def greet(fx):
    def mfx(*args,**kwargs):
        print("function started")
        fx(*args,**kwargs)
        print("function ended")
    return mfx
@greet
def hello():
    print("hello")

# greet(hello)()
hello()
@greet
def add(a,b):
    print(a+b)

add(2,4)