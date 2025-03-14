import turtle
import random

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("dark blue")


t = turtle.Turtle()
#menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("white")
t.write("Background Color",font=("airial",30,"normal"), align = "center")

t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor("tan")
t.write("1. Tan",font=("airial",20,"normal"), align = "left")

t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor("azure")
t.write("2. Azure",font=("airial",20,"normal"), align = "left")

t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor("cornsilk")
t.write("3. Cornsilk",font=("airial",20,"normal"), align = "left")

t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor("red")
t.write("4. Khaki",font=("airial",20,"normal"), align = "left")

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor("white")
t.write("Choose one ",font=("airial",30,"normal"), align = "center")

name = input("Enter your name: ")
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
num1 = random.randint(-100,100)
num2 = random.randint(-100,100)

sum = num1 + num2

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor("red")
t.write(name,font=("airial",30,"normal"), align = "center")


t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor("blue")
t.write(num1,font=("airial",30,"normal"), align = "center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor("purple")
t.write("+",font=("airial",30,"normal"), align = "center")

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("green")
t.write(num2,font=("airial",30,"normal"), align = "center")

t.penup()
t.goto(100,0)
t.pendown()
t.pencolor("purple")
t.write("=",font=("airial",30,"normal"), align = "center")

answer = int(input("What is the answer: "))

t.penup()
t.goto(200,0)
t.pendown()
t.pencolor("black")
t.write(sum,font=("airial",30,"normal"), align = "center")

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor("black")
t.write("Your answer is: "+str(answer),font=("airial",30,"normal"), align = "center")

t.penup()
t.goto(0,-200)
t.pendown()
t.pencolor("black")
t.write("The correct answer is: "+str(sum),font=("airial",30,"normal"), align = "center")

if answer == sum:
   screen.bgcolor("dodgerblue")
   t.penup()
   t.goto(0, 200)
   t.pendown()
   t.pencolor("black")
   t.write("correct", font=("airial", 30, "normal"), align="center")

else:
    screen.bgcolor("darkorange")
    t.penup()
    t.goto(0, 200)
    t.pendown()
    t.pencolor("black")
    t.write("incorrect", font=("airial", 30, "normal"), align="center")


turtle.done()