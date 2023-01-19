a = 7
def b():
    a = 12
    print(a)

b()
print(a)


def c():
    global a
    a = 18
    print(a)

c()
print(a)