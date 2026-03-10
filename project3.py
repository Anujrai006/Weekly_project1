import numpy as np
#OOPS with data structure
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
for i in range(2,n+2):
    name=input(f"enter the name for std {i}:")
    age=input(f"enter the age of std {name}:")
    Class=input(f"enter the Class of std {name}:")
    s=Student_info(name,age,Class)
    students[f"user{i}"]={
        "name":s.name,
        "age":s.age,
        "class":s.Class,
    }
    
print(students)
#later i will updat ethis with file handling concepts Stay with me
