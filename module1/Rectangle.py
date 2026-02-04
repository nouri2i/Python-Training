'''
Instructions
Create a class called Rectangle that has attributes width and height.
Add a init method to initialize the attributes.
Add a str method so that printing a Rectangle object displays "Rectangle(width=, height=)".
Add a add method so that adding two Rectangle objects returns a new Rectangle with width and height being the sum of the two rectangles’ widths and heights.
Create two rectangles: rect1 with width 3 and height 4, and rect2 with width 5 and height 6.

'''
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.heigth=height

    def __str__(self):
        return(f"Rectangle (width={self.width}, height={self.heigth})")

    def __add__(self,other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return (self.width + other.width,self.heigth +other.heigth)
    

rect1=Rectangle(10,20)
rect2 =Rectangle(15,25)
print(rect1)
print(rect2)
print(rect1 + rect2)


        