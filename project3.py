import numpy as np
#python data handling
class Student_info:
    def __init__(self,name,age,Class):
        self.name=name
        self.age=age
        self.Class=Class
students={
    "user1":{
        "name":"anuj",
        "age":17,
        "class":18
    }
}
print(students)
n=int(input("enter the number of student:"))
for i in range(n):
    name=input(f"enter the name for std {i+1}:")
    age=input(f"enter the age of std {name}:")
    Class=input(f"enter the Class of std {name}:")
    s=Student_info(name,age,Class)
    
print(students)
