
a = 10
b = 20
c = 30

def print_globals():
    global c
    print(a, b, c)
    globals()["c"] = 100 #same as c = 100
    print(c)
    
print_globals()
