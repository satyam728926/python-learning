class Person:
    def __init__(self,a,b):#constructor
        # print("Constructor called")
        self.name1=a
        self.occ=b

    def info(self):#method
        print(f"{self.name1} is a {self.occ}")

a=Person("satyam","developer")
b=Person("Divya","HR")
# a.info()
# a.name="Divya"
# a.occ="HR"
# a.info()
a.info()
b.info()