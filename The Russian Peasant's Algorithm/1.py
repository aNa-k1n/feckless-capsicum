##:* args and **kargs

def F(*args,**kwargs):
    pass
    for arg in args:
        print arg
    for kwarg in kwargs:
        print kwarg
    print kwargs



fruit = "apple"
F(fruit)

print "------------"

F(fruit,color = 'red',shape = "sphere")