

#1. Hello World
#Write a Python program to print "Hello, World!" to the console.

print("Hello,World!")

#2.Print Your Name
#Write a program that prints your name to the print()

a=input("your name:")
print(a)

#2.Print Your Name
#Write a program that prints your name to the print()


print("Sreeram Venkata Phani Kiranmai")

#3.Print Name and Age on Separate Lines
#Write a program to print your name and age on separate lines.Practice handling multiple pieces of information using the print() function.

a=input("your name:")
b=input("your age:")
print(a)
print(b)

#4.Declare and Use Different Data Types
#Declare variables of different data types (string, integer, float, boolean) and perform basic operations on them.

a=("Sreeram")
b=20
c=7.7
d=True
print(a)
print(b)
print(c)
print(d)

#5.String Concatenation
#Modify the program to print a message that combines your name and age in a single line using string concatenation. Use +, .format(), or f-strings (f"Hello, my name is{name} and I am {age} years old.").

Name=input("your name:")
Age=(input("your age:"))
print("This is "+Name+" and I am  " +Age+" years old.")

#6. Declare and Print Variables
#Declare variables for your name and age, then print them

Name=input("your name:")
Age=(input("your age:"))
print(Name)
print(Age)

#7.Perform Mathematical Operations
#Write a program that calculates and prints the result of all basic mathematicaloperations. Declare variables for the operands and perform addition, subtraction,multiplication, and division. Understand how Python handles numbers and mathematical expressions.

a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#8.Declare and Print a List
#Declare a list of strings and print each element.

x=["Orange","Apple","Banana","Mango","Kiwi","Muskmelon","Dragonfruit"]
print(x[0])
print(x[2])
print(x[1])
print(x[3])
print(x[5])
print(x[4])
print(x[6])
print(x)

#9.Write a program to print a simple pattern using asterisks:
#Use loops and structured output formatting to generate the pattern.

for i in range(1, 5):
    print("*" * i)

#10. Declare and Modify Variables
#● Declare a variable name and assign it a string value.
#● Declare a variable age and assign it an integer value.
#● Declare a variable is_student and assign it a boolean value (True or False).

Name="Sreeram"
Age=20
is_student=True
print(Name)
print(Age)
print(is_student)

#Print and Modify Variable Values
#● Print the value of each variable to the console.
#● Change the value of the name variable to another string.
#● Increment the value of the age variable by 1.
#● Toggle the value of is_student from True to False or vice versa.
#Practice updating and modifying stored values dynamically.


name = "kiran"
age = 20
is_student = False

print(name, age,  is_student)

name = "Charlie"
age += 1
is_student = not is_student
print(name, age, is_student)

#12. Store and Print Personal Details
#Write a program to store and print the following details using separate variables:
#● name (String)
#● age (Integer)
#● dob (Date of Birth - String or Date format)
#● height (Float)
#● weight (Float)
#● degree (String)
#● gender (String)

name = "Dinesh Adapa"
age = 19
dob = "2005-04-09"
height = 5.8
weight = 70.5
degree = "B.Tech in Computer Science & engineering"
gender = "Male"

print(f"Name: {name}\nAge: {age}\nDOB: {dob}\nHeight: {height}\nWeight: {weight}\nDegree: {degree}\nGender: {gender}")
