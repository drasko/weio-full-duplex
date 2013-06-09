
class WeioShvar(object):
    pass


"""
class WeioShvar(object):
    def __init__ (self, s):
        __slots__=[s]

    def get(self) :
        return self.var

    def set(self, val) :
        self.var = val
"""

"""
class WeioShvar():

    def get(self) :
        return self.var

    def set(self, val) :
        self.var = val



class SharedVars() :
    def __init__ (self, s) :
        for o in s :
            self.o = WeioShvar()

"""

s = ["i",  "j",  "k"]



shv = WeioShvar()
shv.i = 10
shv.j = [10, 20, 30]
shv.k = {"a" : "b", "c" : "d"}

print shv.i
print shv.j
print shv.k


"""
i = WeioShvar()
j = WeioShvar()
k = WeioShvar()

i.set(10)
j.set([10, 20, 30])
k.set({"a" : "b", "c" : "d"})

print i.get()
print j.get()
print k.get()

print j.get()[1]
print k.get()['c']
"""
