# x=4
# print(x)
# def hello():
#     x=5
#     print(f"local variable of x is {x}")

# print(f"global variable of x is {x}")

# hello()
# print(f"again global variableof x is {x}")

x=4
print(x)
def hello():
    global x
    x=5
    y=10
    print(f"local variable of x is {x}")

print(f"global variable of x is {x}")

hello()
print(f"again global variable changed x is {x}")
