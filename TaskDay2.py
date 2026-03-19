#Bitwise Operator 
a=10
b=6
print(a&b)
 
x=12
y=5
print(x|y)

num=8
print(~num)

a=15
b=9
print(a^b)

num=7
print(num<<2)

num=20 
print(num>>1)

a=int(input("Enter the value of a :- "))
b=int(input("Enter the value of b :- "))
print(a&b)

c=int(input("Enter the value of c :- "))
d=int(input("Enter the value of d :- "))
print(c^d)  

#String Tasks
a="hi"
print(a * 4)

b="python"
print(b * 3)

a="super"
b="man"
print(a+b)

a="hello"
b=" "
c="world"
print(a+b+c)

name=input("Enter the name:-")
print(name*5)

a=input("Enter the Name:-")
b=input("Enter the Name:-")
print(a+b)

#Input & Type Casting
name=input("Enter the Name:-")
print(type(name))

age=int(input("Enter the Age:-"))
print(type(age))

a=int(input("Enter the value of a:-"))
b=int(input("Enter the value of b:-"))
print(a+b)

a=int(input("Enter the mark 1:-"))
b=int(input("Enter the mark 2:-"))
print((a+b)/2)

a=int(input("Enter the value of a:-"))
b=int(input("Enter the value of b:-"))
print(3*a*2+b-2)

num=input("Enter the value of num:-")
print(type(num))
num=int(num)
print(type(num))

#Unit Digit Task
num=input("Enter the value of num:-")
print(num[len(num)-1])

num=1231
print(num%10)

num=1720
print(num//10)

num="1767"
print(num[len(num)-2])

num=54367
print(num%10)

#If Statement Task
if(10>=5):
    print("Condition is True")

num=int(input("enter the value of num:-"))
if(num>50):
    print("condition valid")

age=int(input("enter the age:-"))
if(age>=18):
    print("Condition is valid")

num=int(input("enter the value of num:-"))
if(num>100):
    print("condition valid")

num=17
if(num>=0):
    print("The Given no is positive")

#If-Else Statement
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

marks = int(input("Enter marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")

num = int(input("Enter the value of number: "))
if num >= 0:
    print("Positive number")
else:
    print("Negative number")

num = int(input("Enter the value of number: "))
if num > 10:
    print("Number is greater than 10")
else:
    print("Number is not greater than 10")

#Nested If Task

 #job eligibility
name=input("Enter name :")
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))
if(age>=18):
    if(height>=160):
        if(weight>=60):
            print(name,"Congrats you havw been selected")
        else:
            print(name,"Your weight is not eligible")
    else:
        print(name,"Your height is not eligible")   
else:
    print(name,"Your age is not eligible")  

#college admission           
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if (marks >= 60):
    if(age >= 17):
       print("Admission Granted")
    else:
       print("Admission Rejected ,because your age is not eligible")
else:
   print("Admission Rejected ,because your mark is not eligible") 

#sports selection
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if(age >= 16):
    if(height >= 150): 
        if(weight >= 50):
           print("Selected")
        else:
           print("Not Selected, your weight is not eligible")
    else:
        print("Not Selected, your height is not eligible")
else:
    print("Not Selected, your age is not eligible")

#Match Statement
day = int(input("Enter a number (1-7): "))
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid number")


num = int(input("Enter a number (1-3): "))
match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")
    case _:
        print("Invalid number")



fruit = int(input("Enter a number (1-4): "))
match fruit:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")
    case _:
        print("Invalid number")


