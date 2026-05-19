# Variable Assignment and Value Change Example
name = "Naveen Kumar"
age1 = 25
age2 = 24
print("Actual value", age2)
favSubject = "Python Programming"
age2 = age1
print("changed value", age2)
print("Favorite Subject", favSubject)

#Program to take input from user and print it
print("A program to take input from user and print it")
name = input("Enter your name : ")
age = input("Enter your age : ")
print("Your name is : ", name)
print("Your age is : ", age)

# Take Diameter as input and calculate area of circle
d = int(input("Enter diameter of circle : "))
r = d/2
area = 3.14 * r * r
print("Area of circle is : ", area)


# calculate the area of rectangel
l = int(input("Enter length of rectangle : "))
b = int(input("Enter breadth of rectangle : "))
area = l * b
print("Area of rectangle is : ", area)

# calculate the area of triangle
h = int(input("Enter height of triangle : "))
b = int(input("Enter breadth of triangle : "))
area = 1 / 2 * b * h
print("Area of triangle is : ", area)
