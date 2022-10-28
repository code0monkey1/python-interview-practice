# fraction class 
import math

class Fraction:
  
  def __init__(self,top,bottom):
    self.top = top
    self.bottom = bottom
    
    
  def __str__(self):
     return str(self.top) + "/" + str(self.bottom)
   
  def __add__(self,other):
      new_top=self.top*other.bottom+self.bottom*other.top
      new_bottom=self.bottom*other.bottom
      the_gcd= math.gcd(new_top,new_bottom)
      
      return Fraction(new_top//the_gcd,new_bottom//the_gcd)
    
  def __eq__(self,other):
    
       return self.top*other.bottom==self.bottom*other.top
     
  def __sub__(self,other):
     new_top=self.top*other.bottom-other.top*self.bottom
     new_bottom=self.bottom*other.bottom
     new_gcd=math.gcd(new_top,new_bottom)
     
     return Fraction(new_top//new_gcd,new_bottom//new_gcd)
   
  def __lt__(self, other):
     return self.top*other.bottom<other.top*self.bottom
   
  def __mul__(self, other):
    new_num=self.top*other.top
    new_bottom=self.bottom*other.bottom
    the_gcd=math.gcd(new_num,new_bottom)
    return Fraction(new_num//the_gcd,new_bottom//the_gcd)
  
  def __truediv__(self, other):
    new_num=self.top*other.bottom 
    new_bottom=self.bottom*other.top
    
    the_gcd=math.gcd(new_num,new_bottom)
    
    return Fraction(new_num//the_gcd,new_bottom//the_gcd)
    
fraction1 = Fraction(3,17)

print("Fraction",fraction1)

fraction2= Fraction(234,5)

addition  = fraction1+fraction2

print(addition)

subtraction = fraction1-fraction2

print(subtraction)

print(fraction1/fraction2)

print(15/ (7*234))