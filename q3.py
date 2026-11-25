class rectangle:
  def __init__ (self , length , width ):
    self.length = length 
    self.width = width 
  def area(length , width ):
    print(f" Area of the rectangle is : {length * width }")
  def perimeter ( length , width ):
    print(f" Perimeter of the rectangle is : { 2 * (length + width )}")

obj1 = rectangle(10,4)
obj1.area()
obj1.perimeter()        