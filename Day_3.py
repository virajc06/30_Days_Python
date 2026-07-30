# Excercise - Day 3

import string


age=20
height=6
com=1+2j

base=int(input("Enter base of triangle: "))
height=int(input("Enter height of triangle: "))
print("Area of triangle is: ", 0.5*base*height)

a=int(input("A : "))
b=int(input("B : "))
c=int(input("C : "))
print("Perimeter of triangle is: ", a+b+c)

lenght=int(input("Enter length of rectangle: "))
width=int(input("Enter width of rectangle: "))
print("Perimeter of rectangle is: ", 2*(lenght+width))

rad=int(input("Enter radius of circle: "))
print("Area of circle is: ", 3.14*rad**2)

# Question Doudt 8, 9, 10 , 11 , 23

print(len('python')>len('dragon'))

if 'on' in 'python' and 'on' in 'dragon':
    print("True")

i="I hope this course is not full of jargon"
jargon="jargon"

if jargon in i:
    print("True")

print(not 'on' in 'python' and not 'on' in 'dragon')

p=len('python')
print(float(p))
print(str(p))

if int(input("Enter number: "))%2==0:
    print("Even")
else:
    print("Odd")

print(7.0//3.0==2.7)

print(type('10')==type(10))

print(int(9.8)==10)

hours=int(input("Enter hours: "))
rate=int(input("Enter rate per hour: "))
print("Your weekly earning is: ", hours*rate)

years=int(input("Enter number of years you have lived: "))
print("You have lived for ", years*365*24*60*60, " seconds")

for i in range(5):
    print(i, " x ", i, " = ", i*i)


Their are questions i left that i will be completing after i get a bbreak






