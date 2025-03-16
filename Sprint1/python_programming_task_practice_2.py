

# 1. Declare variables using camelCase and snake_case
userName = "Kiran"
user_age = 20
print(userName)
print(user_age)

#2.Declare a constant variable using Python’s convention (uppercase) and use it in a calculation.
#● Defi ne a constant PI = 3.14159.
#● Calculate and print the circumference of a circle (2 * PI * radius).

PI= 3.14159
Radius = int(input("Enter the radius"))
print("Circumfrence Of Circle",2*PI*Radius)

#3.Declare a list, access elements, and perform basic list operations.
#● Create a list with five different items.
#● Print the fi rst and last elements.
#● Modify an element and add a new item to the list.

List = ['Dinesh','Phani','Manogna','Shalini','Meghana']
List.append('Ram')
print(List)
List[1] = 'Kiran'
print(List)
print(List[3])
List.remove('Meghana')
print(List)

#4.Sum of Two Numbers
#● Declare two variables with numeric values.
#● Add them together and print the result.
A=int(input("Enter the First Number:"))
B=int(input("Enter the Second Number:"))
print("Sum of Two Numbers:",A+B)

#5.Program to Find the Area of a Circle
#Write a Python program to calculate and display the area of a circle using the formula πr².
PI=3.14159
Radius = int(input("Enter the radius:"))
print("Area Of Circle:",PI*Radius*Radius)

#6.Program to Find the Area of a Rectangle
#Write a program that takes length and width as inputs and calculates the area using length × width.
Length = int(input("Enter the Length:"))
Width = int(input("Enter the Width:"))
print("Area Of Rectangle:",Length*Width)

#7.Program to Find the Area of a Triangle
#Write a program that calculates the area of a triangle using (base × height) / 2.
Base = int(input("Enter the Base:"))
Height = int(input("Enter the Height:"))
print("Area Of Triangle:",(Base*Height)/2)

#8.Simple Calculator
#Create a Python program that asks the user for two numbers and performs addition, subtraction, multiplication, and division. Display the results.
X = int(input("Enter 1st Number:"))
Y = int(input("Enter 2nd Number:"))
print(f"Addition: {X + Y}")
print(f"Subraction:{X-Y}")
print(f"Multiplication:{X*Y}")
print(f"Division:{X/Y}")

#9.Use assignment operators (=, +=, -=, *=, /=) to modify and print variable values.
#● Assign an initial value to a variable.
#● Use different assignment operators to update and print the variable’s value.
x = int(input("Enter a number:"))
x += 5
x -= 2
x *= 3
x /= 2
print("Final value of x:", x)

#10. Declare a variable and use increment (+=) and decrement (-=) operators to modify its value.
#● Start with an integer variable.
#● Increase its value using += and decrease it using -=.
num = int(input("Enter a number:"))
num += 7
print("Incremented:", num)
num -= 7
print("Decremented:", num)

#11.Use comparison operators (==, !=, >, <, >=, <=) to compare two variables and print the results.
#● Declare two numeric variables.
#● Use comparison operators and print the outcome of each comparison.
# 11. Comparison operators
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#12.Use logical operators (and, or, not) on boolean variables and print the results.
#● Declare two boolean variables (True or False).
#● Apply logical operators and print the results of each operation.
# 12. Logical operators
is_sunny = True
is_warm = False
print(is_sunny and is_warm)
print(is_sunny or is_warm)
print(not is_sunny)

#13 .Program to Swap Two Variables
#● Swap values of two variables using a third variable.
#● Swap values again without using a third variable.
a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
temp = a
a = b
b = temp
print("Swapped using third variable:", a, b)
a, b = b, a
print("Swapped without third variable:", a, b)

#14.Program to Find the Average of Given Numbers
#Write a program to take three numbers as input and calculate their average
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("Average:", average)

#15.Perform a compound arithmetic operation on four variables.
#Given a = 10, b = 30, c = 12, d = 3, perform (a + b) * c / d and print the result.
a, b, c, d = 10, 30, 12, 3
result = (a + b) * c / d
print("Result:", result)

#16.Program to Store 10th Grade Marks, Calculate Total and Average.
#● Declare variables for marks in subjects (e.g., Tamil, English, Maths, Science, Social).
#● Calculate and print the total marks and average.
tamil = int(input("Enter Tamil Marks:"))
english = int(input("Enter English Marks:"))
maths = int(input("Enter Maths Marks:"))
science = int(input("Enter Science Marks:"))
social = int(input("Enter Social Marks:"))
total = tamil + english + maths + science + social
average = total / 5
print("Total Marks:", total)
print("Average Marks:", average)

