x=10
print("Memory Address of X = ",id(x))
y=x
print("Memory Address of Y = ",id(y))

if id(x)== id(y):
    print("X and Y have same memory location")

x=11
print("After x=11 , Memory Address of X = ",id(x))

if id(x)==id(y):
    pass
else:
    print("X and Y have Different memory Location")

z=10
print("Memory Address of Z = ",id(z))

if id(z)==id(y):
    print("Python is Dynamically Typed Language")
