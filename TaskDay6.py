
#Task 1: Encapsulation (User Class)


class User:
    def __init__(self):
        self.__user_name = None
        self.__pwd = None

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")

# Example usage
user = User()   
user.set_user("raja", "xyz123")
user.register()  # O/P: Registering user: raja
user.login()     # O/P: Logging in: raja


#Task 2: Inheritance 

# Parent Class: User
class User:
    def register(self):
        print("Registering user...")

    def login(self):
        print("Logging in...")

# Child Class: Student
class Student(User):
    def student_greet(self):
        print("Hello Student")

# Child Class: Faculty
class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")

# Multilevel Inheritance: TempFaculty inherits from Faculty
class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")

# Student object
s1 = Student()
s1.register()        # -->Access parent method
s1.login()           # -->Access parent method
s1.student_greet()   # -->Access child method


# Faculty object
f1 = Faculty()
f1.register()        # -->Access parent method
f1.login()           # -->Access parent method
f1.faculty_greet()   # -->Access child method


# TempFaculty object
t1 = TempFaculty()
t1.register()            # -->Access parent method
t1.login()               # -->Access parent method
t1.faculty_greet()       # -->Access Faculty method
t1.tempFaculty_greet()   # -->Access TempFaculty method


# Parent object 
u1 = User()
u1.register()
u1.login()
# u1.student_greet()   # -->Error: Parent cannot access child methods
# u1.faculty_greet()  


# Task 3: Method Overriding

# Parent Class
class User: 
    def greet(self):
        print("Welcome User")

# Child Class: Student
class Student(User):
    def greet(self):
        print("Welcome Student")    

# Child Class: Faculty
class Faculty(User):
    def greet(self):
        print("Welcome Faculty")

# Example 
student = Student()             
faculty = Faculty()
student.greet()  # -->O/P: Welcome Student
faculty.greet()  # -->O/P: Welcome Faculty

#Task 4: Method Chaining

class User:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self
    
# Example
user = User()   
user.login().greet().register()


#Task 5: Combined Task (Real-Time)


class User:
    users_count = 0  # Class variable to count users

    def __init__(self):
        self.__user_name = None
        self.__pwd = None
        User.users_count += 1  

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print(f"Registering user: {self.__user_name}")
        return self

    def login(self):
        print(f"Logging in: {self.__user_name}")
        return self

    def greet(self):
        print("Welcome User")
        return self

# Child Class: Student
class Student(User):
    def greet(self):
        print("Welcome Student")
        return self

# Child Class: Faculty
class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self

# Example 
student = Student()
student.set_user("bruce", "pwd123")
student.login().greet().register()  
faculty = Faculty()
faculty.set_user("prof_lee", "lee142")
faculty.login().greet().register()  
print(f"Total users created: {User.users_count}")  



    