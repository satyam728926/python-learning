class Myclass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"Value of a is {self._value}")

    @property
    def tentimesb(self):
        return 10*self._value
    
    @tentimesb.setter
    def tentimesb(self,new_value):
        self._value=new_value

a=Myclass(10)
a.show()
a.tentimesb=100
print(a.tentimesb)
a.show()