def f(x):
    global y
    y=1
    x=y+x
    return x
x=3
y=4
z=f(x)
print('x is',x)
print("y is", y)
print('z is ',z)
