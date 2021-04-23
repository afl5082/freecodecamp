class Rectangle:
  def __init__(self,w,h):
    self.h = h
    self.w = w

  def __str__(self):
    return str("Rectangle(width=" + str(self.w) +", height=" + str(self.h) +")") 

  def set_width(self,w):
    self.w = w
  
  def set_height(self,h):
    self.h = h

  def get_perimeter(self):
    perimeter = 2 * self.w + 2 * self.h 
    return perimeter

  def get_area(self):
    area = self.w * self.h
    return area

  def get_diagonal(self):
    diagonal = ((self.w ** 2 + self.h ** 2) ** .5)
    return diagonal

  def get_picture(self):
    if self.h > 50:
      return "Too big for picture."
    elif self.w > 50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(self.h):
        for i in range(self.w):
          picture+="*"
        picture+=('\n')
      return picture

  def get_amount_inside(self,Rectangle):
    area = self.get_area()
    area_rect = Rectangle.get_area()

    return int(area / area_rect)


class Square(Rectangle):
  def __init__(self,side):
    self.h = side
    self.w = side
    super(Rectangle, self)
  
  def set_side(self,side):
    self.h = side
    self.w = side

  def set_height(self,h):
    self.h = h
    self.w = h

  def set_width(self,w):
    self.h = w
    self.w = w

  def __str__(self):
    return str("Square(side=" + str(self.h) +")")
