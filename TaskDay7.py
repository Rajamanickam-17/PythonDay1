
#Task 1: Use super() properly
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

# Example 
student = Student("Raj", 1, "IT", 12000)
faculty = Faculty("Dr.Vasu", 2, 50000)
temp_faculty = TempFaculty("Crown", 3, 40000, "6 months")
print(student.name, student.id, student.dept, student.fees)
print(faculty.name, faculty.id, faculty.salary)
print(temp_faculty.name, temp_faculty.id, temp_faculty.salary, temp_faculty.duration)


#Task 2: Apply Abstraction

from abc import ABC, abstractmethod
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees
    def get_details(self):
        return f"{super().get_details()}, Dept: {self.dept}, Fees: {self.fees}"
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
    def get_details(self):
        return f"{super().get_details()}, Salary: {self.salary}"
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration
    def get_details(self):
        return f"{super().get_details()}, Duration: {self.duration}"
    
# Example
student = Student("Raj", 1, "IT", 12000)    
faculty = Faculty("Dr.Vasu", 2, 50000)
temp_faculty = TempFaculty("Crown", 3, 40000, "6 months")
print(student.get_details())
print(faculty.get_details())
print(temp_faculty.get_details())

#Task 3: Sorting using key

students = [
    Student("Raj", 1, "IT", 12000),
    Student("Bobin", 2, "Mathematics",11000),
    Student("Charan", 3, "Physics", 9000)
]

faculty = [
    Faculty("Dr.Vasu", 1, 50000), 
    Faculty("Dr.John", 2, 60000),
    Faculty("Crown", 3, 40000)
]

students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)
print("Sorted Students by Fees:")
for student in students:
    print(student.get_details())
print("\nSorted Faculty by Salary:")
for member in faculty:
    print(member.get_details())

#Task 4: Use map()

students = [
    Student("Raj", 1, "IT", 12000),
    Student("Bobin", 2, "Mathematics",11000),
    Student("Charan", 3, "Physics", 9000)
]

names = list(map(lambda s: s.name, students))
print("Student Names:", names)

#Task 5: Use filter()

students = [
    Student("Raj", 1, "IT", 12000),
    Student("Bobin", 2, "Mathematics",11000),
    Student("Charan", 3, "Physics", 9000)
]

faculty = [
    Faculty("Dr.Vasu", 1, 50000), 
    Faculty("Dr.John", 2, 60000),
    Faculty("Crown", 3, 40000)
]

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))
print("Students with Fees > 50000:")
for student in high_fee_students:
    print(student.get_details())
print("\nFaculty with Salary > 30000:")
for member in high_salary_faculty:
    print(member.get_details())

#Task 6: Use reduce()

from functools import reduce

students = [    
    Student("Raj", 1, "IT", 12000),
    Student("Bobin", 2, "Mathematics",11000),
    Student("Charan", 3, "Physics", 9000)
]

faculty = [
    Faculty("Dr.Vasu", 1, 50000), 
    Faculty("Dr.John", 2, 60000),
    Faculty("Crown", 3, 40000)
]
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)
print("Total Fees Collected:", total_fees)
print("Total Salary of Faculty:", total_salary)

#Task 7: Higher Order Function

def process_users(users, func):
    return list(map(func, users))

students = [
    Student("Raj", 1, "IT", 12000),
    Student("Bobin", 2, "Mathematics",11000),
    Student("Charan", 3, "Physics", 9000)
]
# Example:
student_names = process_users(students, lambda s: s.name)
print("Student Names:", student_names)


#Final Challenge - Build a mini system:

from abc import ABC, abstractmethod
from functools import reduce

# -------------------------------
# Abstract Base Class
# -------------------------------

class AbstractUser(ABC):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @abstractmethod
    def get_details(self):
        pass


# -------------------------------
# Child Classes
# -------------------------------

class Student(AbstractUser):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty(AbstractUser):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"


# -------------------------------
# Higher Order Function
# -------------------------------

def process_users(users, func):
    return list(func(users))


# -------------------------------
# Data
# -------------------------------

students = [
    Student("Raj", 101, "IT", 52000),
    Student("Bobin", 102, "Math", 60000),
    Student("Charan", 103, "Physics", 45000),
    Student("Daniel", 104, "Bio-zoology", 70000)
]

faculty = [
    Faculty("Dr. Vasu", 201, 25000),
    Faculty("Dr. Ram", 202, 40000),
    Faculty("Dr. Crown", 203, 35000),
    Faculty("Dr. Prasath", 204, 60000)
]

# -------------------------------
# 1. Print All Details
# -------------------------------

print("=== All Students ===")
for s in students:
    print(s.get_details())

print("\n=== All Faculty ===")
for f in faculty:
    print(f.get_details())


# -------------------------------
# 2. Sorted Data
# -------------------------------

students.sort(key=lambda s: s.fees)
faculty.sort(key=lambda f: f.salary)

print("\n=== Students Sorted by Fees ===")
for s in students:
    print(s.get_details())

print("\n=== Faculty Sorted by Salary ===")
for f in faculty:
    print(f.get_details())


# -------------------------------
# 3. Filtered Data
# -------------------------------

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("\n=== Students with Fees > 50000 ===")
for s in high_fee_students:
    print(s.get_details())

print("\n=== Faculty with Salary > 30000 ===")
for f in high_salary_faculty:
    print(f.get_details())


# -------------------------------
# 4. Aggregated Data (reduce)
# -------------------------------

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("\n=== Totals ===")
print("Total Fees Collected:", total_fees)
print("Total Faculty Salary:", total_salary)


# -------------------------------
# 5. Higher Order Function Usage
# -------------------------------

names = process_users(students, lambda users: map(lambda s: s.name, users))
print("\n=== Student Names (via process_users + map) ===")
print(names)



