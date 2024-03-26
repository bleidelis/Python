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
  t.forward(40)
  t.circle(50)
  t.forward(60)
  t.circle(70)
  t.forward(60)
  t.circle(55)

DrawCloudLogo()
#DrawTriangle()
turtle.done()