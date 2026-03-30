# Task 1: Employee Management System

employees = []

def add_employee():
    name = input("Name: ")
    age = int(input("Age: "))
    role = input("Role: ")
    salary = float(input("Salary: "))
    employees.append({
        "name": name,
        "age": age,
        "role": role,
        "salary": salary
    })
    print("Employee added.")

def update_employee():
    name = input("Enter employee name to update: ")
    for emp in employees:
        if emp["name"] == name:
            emp["age"] = int(input("New Age: "))
            emp["role"] = input("New Role: ")
            emp["salary"] = float(input("New Salary: "))
            print("Employee updated.")
            return
    print("Employee not found.")

def delete_employee():
    name = input("Enter employee name to delete: ")
    for emp in employees:
        if emp["name"] == name:
            employees.remove(emp)
            print("Employee deleted.")
            return
    print("Employee not found.")

def display_employees():
    if not employees:
        print("No employees.")
    for emp in employees:
        print(emp)

while True:
    print("\n1.Add 2.Update 3.Delete 4.Display 5.Exit")
    ch = input("Choice: ")
    if ch == "1": add_employee()
    elif ch == "2": update_employee()
    elif ch == "3": delete_employee()
    elif ch == "4": display_employees()
    elif ch == "5": break

# Task 2: Student Report Card

def report_card():
    name = input("Student Name: ")
    m1 = float(input("Mark 1: "))
    m2 = float(input("Mark 2: "))
    m3 = float(input("Mark 3: "))

    total = m1 + m2 + m3
    avg = total / 3

    if avg >= 90: grade = "A"
    elif avg >= 75: grade = "B"
    elif avg >= 60: grade = "C"
    else: grade = "Fail"

    print("\n--- REPORT CARD ---")
    print(f"Name: {name}")
    print(f"Total: {total}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")

report_card()

#Task 3: Shopping Cart System

cart = {}

def add_item():
    name = input("Product: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    cart[name] = {"price": price, "qty": qty}

def remove_item():
    name = input("Remove product: ")
    cart.pop(name, "Item not found")

def display_cart():
    total = 0
    print("\nItem Price Qty Total")
    for item in cart:
        p = cart[item]["price"]
        q = cart[item]["qty"]
        t = p*q
        total += t
        print(item, p, q, t)
    print("Grand Total:", total)

while True:
    print("\n1.Add 2.Remove 3.View 4.Exit")
    c = input("Choice: ")
    if c=="1": add_item()
    elif c=="2": remove_item()
    elif c=="3": display_cart()
    elif c=="4": break

# Task 4: Login & User Validation

users = {
    "admin": "1234",
    "user": "abcd"
}

uname = input("Username: ")
pwd = input("Password: ")

if uname in users and users[uname] == pwd:
    print("Login Successful")
else:
    print("Invalid Credentials")

# Task 5: Unique Visitor Counter

visitors = set()

while True:
    name = input("Enter visitor name (or exit): ")
    if name.lower() == "exit":
        break
    visitors.add(name)

print("Total unique visitors:", len(visitors))


#Task 6: String Formatter Tool

name = input("Name: ")
product = input("Product: ")

print(f"Hello {name}, thanks for buying {product}")
print(name.ljust(20, "*"))
print(name.rjust(20, "*"))
print(name.center(20, "*"))

#Task 7: Bank Account System

account = {}

def create():
    account["name"] = input("Name: ")
    account["balance"] = float(input("Initial Balance: "))

def deposit():
    amt = float(input("Deposit amount: "))
    account["balance"] += amt

def withdraw():
    amt = float(input("Withdraw amount: "))
    if amt <= account["balance"]:
        account["balance"] -= amt
    else:
        print("Insufficient balance")

def check():
    print("Balance:", account["balance"])

create()

while True:
    print("\n1.Deposit 2.Withdraw 3.Balance 4.Exit")
    c = input("Choice: ")
    if c=="1": deposit()
    elif c=="2": withdraw()
    elif c=="3": check()
    elif c=="4": break

# Task 8: Voting System

votes = {}

while True:
    name = input("Vote for (or exit): ")
    if name == "exit":
        break
    votes[name] = votes.get(name, 0) + 1

winner = max(votes, key=votes.get)
print("Winner:", winner)

# Task 9: Course Enrollment System

students = {}

def add_student():
    name = input("Student Name: ")
    courses = input("Courses (comma separated): ").split(",")
    students[name] = courses

def update_courses():
    name = input("Student Name: ")
    if name in students:
        students[name] = input("New courses: ").split(",")

def display():
    for s in students:
        print(s, "->", students[s])

while True:
    print("\n1.Add 2.Update 3.Display 4.Exit")
    c = input("Choice: ")
    if c=="1": add_student()
    elif c=="2": update_courses()
    elif c=="3": display()
    elif c=="4": break

# Task 10: Number Utility Tool

num = int(input("Enter number: "))

print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hexadecimal:", hex(num))

big = 1234567890
print("With commas:", f"{big:,}")
print("Scientific:", f"{num:.2e}")