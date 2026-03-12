import numpy as np
#OOPS with data structure
class Student_info:
    def __init__(self,name,age,Class):
        self.name=name
        self.age=age
        self.Class=Class
# students={
#     "user1":{
#         "name":"anuj",
#         "age":17,
#         "class":18
#     }
# }
# print(students)



students={}
def load_students():
    try:
        students={}
        with open("student.txt","r") as f:
         for line in f:
            parts=line.strip().split(",")
            students[parts[0]] =  {
                "name":parts[1],
                 "age" :parts[2],
                 "class":parts[3]
            }
    except:
        students={}
    return students
students=load_students()    
start=len(students)+1
n=int(input("enter the number of student:"))
for i in range(start,start+n):
    name=input(f"enter the name for std {i}:")
    age=input(f"enter the age of std {name}:")
    Class=input(f"enter the Class of std {name}:")
    s=Student_info(name,age,Class)
    students[f"user{i}"]={
        "name":s.name,
        "age":s.age,
        "class":s.Class,
    }
def save_students(students):
    with open("student.txt","w") as f:
        for key,value in students.items():
            f.write(f"{key},{value['name']},{value['age']},{value['class']}\n")
save_students(students)
print(students)





#later i will updat ethis with file handling concepts Stay with me
