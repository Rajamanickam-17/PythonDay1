# Task 1: User Info Manager
def create_user(name, age, role):
    
    return {
        "name": name.title(),
        "age": age,
        "role": role.title()
    }

users = []
users.append(create_user("Raja", 23, "Cloud Engineer"))
users.append(create_user("Sundari", 24, "IT"))

for user in users:
    print(user)

# Task 2: Dynamic Calculator (*args)    

def calculate_total(*numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

t, a = calculate_total(17, 18, 33)
print("Total:", t, "Average:", a)

# Task 3: Keyword Config System (**kwargs)

def system_config(**settings):
    for key, value in settings.items():
        print(key, ":", value)

system_config(mode="debug", version="1.0")

# Task 4: Factorial Service (Recursion)

def factorial(n):
    if n < 0:
        return "Error: Negative number"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("\nFactorial:")
print("Factorial of 7:", factorial(5))
print("Factorial of -2:", factorial(-1))

# Task 5: Memory Optimization (Generator)

def square_generator(n):
    for i in range(1, n+1):
        yield i*i

gen = square_generator(5)
lst = [i*i for i in range(1, 6)]

print(type(gen))
print(type(lst))

for i in gen:
    print(i)

# Task 6: Exception Handling Module

try:
     numerator = float(input("Enter the numerator (top number): "))
     denominator = float(input("Enter the denominator (bottom number): "))

     result = numerator / denominator
     print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide a number by zero.")

except ValueError:
     print("Error: Invalid input. Please enter numbers only.")

finally:
     print("Program Completed")

# Task 7: File Handling

with open("team_data.txt", "w") as f:
    f.write("Rocky, Developer\n Geetha, Manager")

with open("team_data.txt", "r") as f:
    data = f.read()
    print(data)

print("File closed:", f.closed)