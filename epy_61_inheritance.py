class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show_Details(self):
        print(f"name of the  employee is {self.name} and id is {self.id}")

class Programmer(Employee):
        def showlanguage(self):
            print("the default language is python")

e1=Employee("satyam",623)
e1.show_Details()
e2=Programmer("Raj",6122)
e2.show_Details()
e2.showlanguage()