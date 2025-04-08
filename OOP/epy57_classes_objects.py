class Person:
    name="satyam"
    occupation="Developer"
    networth="10"
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person()
b=Person()
c=Person()
# print(a.name,a.occupation)
a.name="Shubham"
a.occupation="ETL Developer"
b.name="Gaurav"
b.occupation="Dalal"
# print(a.name,a.occupation)
a.info()
b.info()
c.info()