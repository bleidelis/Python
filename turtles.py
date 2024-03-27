# 3.11.7 'base':conda
#The canvas has a default size (700x650)

import turtle
t = turtle.Turtle()


# Octagon
def Octagon():
  t.forward(100)
  t.right(45)
  t.forward(100)
  t.right(45)
  t.forward(100)
  t.right(45)
  t.forward(100)
  t.right(45)
  t.forward(100)
  t.right(45)
  t.forward(100)
  t.right(45)
  t.forward(100)
  t.right(45)
  t.forward(100)
def Cloud():
  t.begin_fill()
  t.circle(30)
  t.penup()
  t.forward(50)
  t.pendown()
  t.circle(50)
  t.penup()
  t.forward(60)
  t.pendown()
  t.circle(70)
  t.penup()
  t.forward(60)
  t.pendown()
  t.circle(50)
  t.end_fill()  
def Onion():
  t.screen.bgcolor("#023e8a")
  t.color("#0077b6")
  t.begin_fill()
  t.circle(150)
  t.end_fill()
  t.color("#0096c7")
  t.begin_fill()
  t.circle(105)
  t.end_fill()
  t.color("#00b4d8")
  t.begin_fill()
  t.circle(65)
  t.end_fill()
  t.color("#48cae4")
  t.begin_fill()
  t.circle(35)
  t.end_fill()
  t.color("#ade8f4")
  t.begin_fill()
  t.circle(15)
  t.end_fill()
  t.color("#caf0f8")
  t.begin_fill()
  t.circle(5)
  t.end_fill()
  t.penup()
def TriForce():
  t.screen.bgcolor("#4aba91")
  t.color("#F8D74F")
  t.begin_fill()
  t.forward(150)
  t.left(120)
  t.forward(150)
  t.left(120)
  t.forward(150)
  t.end_fill()
  t.screen.bgcolor("#0d9263")
  t.begin_fill()
  t.forward(150)
  t.left(120)
  t.forward(150)
  t.left(120)
  t.forward(150)
  t.end_fill()
  t.penup()
  t.left(240)
  t.forward(150)
  t.pendown()
  t.screen.bgcolor("#0e5135")
  t.begin_fill()
  t.right(120)
  t.forward(150)
  t.left(120)
  t.forward(150)
  t.left(120)
  t.forward(150)
  t.screen.bgcolor("#494b4b")
  t.end_fill()

def SolarSystem():
  t.screen.bgcolor("#494b4b")
  t.speed(10)
  #Sun - (radius = 696,000 km - 10900%) | #F23D00
  # t.color("#F23D00")
  # t.begin_fill()
  # t.circle(1090)
  # t.end_fill()


  #go to the left side
  t.left(180)
  t.penup()
  t.forward(550)
  t.left(180)
  #Mercury - (radius = 2,440 km / 1,516 miles) – 38% | #A8A8A8
  t.pendown()
  t.color("#A8A8A8")
  t.begin_fill()
  t.circle(38)
  t.end_fill()

  t.penup()
  t.forward(150)
  t.pendown()

  #Venus - (6,052 km / 3,761 miles) – 95% | #E9BB5D
  t.color("#E9BB5D")
  t.begin_fill()
  t.circle(95)
  t.end_fill()

  t.penup()
  
  t.forward(150)
  t.pendown()

  #Earth - (6,371 km / 3,959 miles) | #426F2F
  t.color("#426F2F")
  t.begin_fill()
  t.circle(100)
  t.end_fill()

  t.penup()
  t.forward(150)
  t.pendown()
  #Mars - (3,390 km / 2,460 miles) – 53% | #C1440F
  t.color("#C1440F")
  t.begin_fill()
  t.circle(53)
  t.end_fill()

  t.penup()
  t.forward(150)
  t.pendown()

  #Jupiter - (69,911 km / 43,441 miles) – 1,120% | #ECCCAE
  t.color("#ECCCAE")
  t.begin_fill()
  t.circle(1120)
  t.end_fill()

  t.penup()
  t.forward(150)
  t.pendown()
  #Saturn - (58,232 km / 36,184 miles) – 945% | #ECCCAE

  #Uranus - (25,362 km / 15,759 miles) – 400% | #C9ECF0

  #Neptune - (24,622 km / 15,299 miles) – 388% | #4474F3

  #Pluto - (1,188.3 km) - 19% | #A78670

SolarSystem()
turtle.done()