class Math:
    def __init__(self,num):
        self.num=num
    def addtonum(self,n):
        self.num=self.num+n

    @staticmethod
    def add(a,b):
        return a+b
    
a=Math(5)
sum=a.add(5,2)
sum2=a.addtonum(5)
print(a.num)