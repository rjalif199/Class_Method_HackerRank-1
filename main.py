import math as m
class Rectangle:
  def __init__(self,base,height):
    self.base=base
    self.height=height
  def area(self):
    return self.base*self.height
  pass
class Circle:
  
  def __init__(self,radius):
    self.radius=radius
  def area(self):
    return m.pi*self.radius**2
  pass  
# carea=Circle()
# print(carea.area(4)) 
message=input("Enter 'Cir' to calculate area of circle or 'Rec' to calculate area of rectangle\n")
if message.lower=="cir":
  rad=float(input("Enter the radius >_"))
  carea=Circle(rad)
  print(f"Area of the circle {carea.area()}")  
if message.lower()=="rec":
  b=float(input("Enter base of the rectangle >_"))
  print("\n")
  h=float(input("Enetr Height of the rectangle >_"))
  recarea=Rectangle(b,h)
  print(f"Area of the rectange = {recarea.area()}")


