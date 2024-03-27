# 3.11.7 'base':conda
import turtle
t = turtle.Turtle()

# Octagon
def DrawOctagon():
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
def DrawTriangle():
  t.forward(100)
  t.right(120)
  t.forward(100)
  t.right(120)
  t.forward(100)
def DrawCloudLogo():
  t.circle(30)
  t.forward(50)
  t.circle(50)
  t.forward(60)
  t.circle(70)
  t.forward(60)
  t.circle(50)
def DrawOnionRings():
  t.circle(5)
  t.circle(15)
  t.circle(35)
  t.circle(65)
  t.circle(105)

DrawOnionRings()

turtle.done()