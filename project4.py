# basic data structure using file handling and funtion
def save_name(something):
    with open("username.txt","w") as f:
        f.write(something)
def load_name():
    try:
        with open("username.txt","r") as f:
         return f.read()
        
    except:
       return ""
name=load_name()
print(name)

# name=input("enter the name:") first to store name
# save_name(name) calling the function
