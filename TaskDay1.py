#Task1 - Print Formatting
print("Hello World",end=" ")
print("Welcome Python")

print("Laptop","Mouse","Keyboard",sep=" | ")

#Task2 - Variables
name="Ravi"
age=22
city="Chennai"

print(name,age,city,sep="-")

#Task3 - Multiple Assignment
name="Meena"
age=20
student=True

print("Multiple Assignment:-", name,age,student)

#Task4 - Indexing
word="Python"
print(word[0])
print(word[2])
print(word[5])

#Task5 - Arithmetic operators
print(25+10)
print(50-20)
print(8*5)
print(100/10)
print(10%3)
print(2**4)
print(20//3)

#Task6 - BODMAS Expression
print(3+2*5**2)
#ans-53

#Task7 - Assignment Operator
num=50
num+=25
print(num)

num=100
num/=10
print(num)

#Task8 - Comparison Operators
print(10>5)
print(20<15)
print(5==5)
print(10!=8)
print(7>=7)
print(6<=2)

#Task9 - String Comparison
a="apple"
b="Apple"
print(a==b)
#in python String is case sensitive, it has different ASCII values

#Task10 - Logical operator
print(10>5 and 5==5)
print(5>10 or 10==10)
print(not(5>2))

#Task11 - Membership operator
numbers=[10,20,30,40,50]
print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)

#Task12 - Swap Variables
a=10
b=20
a,b=b,a
print(a,b)

#Task13 -  Bitwise XOR
a=6 
b=3
print(a^b)