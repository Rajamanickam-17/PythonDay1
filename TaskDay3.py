#Section 1 - Loop Basics

'''for i in range(1,51):
    print(i)

for i in range(1, 101):
    if i % 2 == 0:
        print(i)

for i in range(1, 101):
    if i % 2 != 0:
        print(i)

for i in range(1, 13):
    print("7 x", i, "=", 7 * i)

total = 0
for i in range(1, 101):
    total += i
print("Sum of numbers from 1 to 100 =", total)

for i in range(50, 0, -1):
    print(i)

count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print("Count =", count)

for i in range(1, 11):
    print(i, "square is", i * i)

for i in range(1, 11):
    print(i,"cube is", i ** 3)

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)'''

#Section 2- While Loop

'''i = 1
while i <= 20:
    print(i)
    i += 1

n = int(input("Enter a number: "))
fact = 1
while n > 0:
    fact = fact * n
    n -= 1
print("Factorial of entered number :", fact)

n = int(input("Enter a number: "))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print("Reversed number:", reverse)

n = int(input("Enter a number: "))
count = 0
while n > 0:
    count += 1
    n = n // 10
print("Number of digits:", count)

while True:
    user_input = input("Enter something: ")
    if user_input == "stop":
        break
    print("You entered:", user_input)
print("Program stopped.")'''

# Section 3: Nested Loop

'''for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()

for i in range(3):
    for j in ['A', 'B', 'C']:
        print(j, end=" ")
    print()

num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()'''

#Section 4: String Basics

'''val = input("Enter a string: ")
count = 0
for char in val:
    count += 1
print("Total characters:", count)


val = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in val:
    if char in vowels:
        vowel_count += 1
print("Total vowels:", vowel_count)


val = input("Enter a string: ")
vowels = "aeiouAEIOU"
consonant_count = 0
for char in val:
    if char.isalpha() and char not in vowels:
        consonant_count += 1
print("Total consonants:", consonant_count)


val = input("Enter a string: ")
reversed_val = ""
for i in range(len(val) - 1, -1, -1):
    reversed_val += val[i]
print("Reversed string:", reversed_val)



text = input("Enter a string: ")
reversed_text = ""
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]
if text == reversed_text:
    print("It is a palindrome")
else:
    print("It is NOT a palindrome")'''

#Section 5: String Slicing 

'''a = "PythonSlicing"
print(a[:5])

a = "PythonSlicing"
print(a[-3:])

a = "PythonSlicing"
print(a[::-1])

a = "PythonSlicing"
print(a[1::2])

a = "PythonSlicing"
print(a[1:-1])'''

# Section 6: List Basics

'''numbers = [10, 17, 18, 33, 45]

total = sum(numbers)
print("Sum of elements:", total)

maximum = max(numbers)
print("Maximum value:", maximum)

minimum = min(numbers)
print("Minimum value:", minimum)

count = len(numbers)
print("Total elements:", count)

element = 20
if element in numbers:
    print(element, "exists in the list")
else:
    print(element, "does not exist in the list")'''

#Section 7: List Operations 

my_list = [10, 17]

my_list.append(18)
my_list.append(33)
my_list.append(45)
print(my_list)


my_list = [10, 18, 33]

my_list.insert(1, 17)
print(my_list)


my_list = [10, 17, 18, 33, 45]

my_list.remove( 17)
print(my_list)


my_list = [10, 17, 18, 33, 45]

reversed_list = my_list[::-1]
print(reversed_list)


my_list = [ 45, 17, 10, 33, 18]

my_list.sort()
print(my_list)





