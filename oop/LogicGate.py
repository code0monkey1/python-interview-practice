

class LogicGate:
  
 def __init__(self,n):
   self.label = n
   self.output=None
   
 def getLabel(self):
   return self.label
 
 def getOutput(self):
    self.output=self.performGateLogic()
    return self.output
  
class UnaryGate(LogicGate):
   
   def __init__(self,n):
     super(UnaryGate,self).__init__(n)
     self.pin=None
     
   def getPin(self):
     return int(input("Enter the pin for the gate: "+self.getLabel()+"-->"))
    
class BinaryGate(LogicGate):
  
    def __init__(self,n):
      super(BinaryGate, self).__init__(n)
      
      self.pinA=None
      self.pinB=None
      
    def getPinA(self):
       return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))
     
    def getPinB(self):
       return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
     
class AndGate(BinaryGate):
  
  def __init__(self,n):
    super(AndGate,self).__init__(n)
    
  def performGateLogic(self):
    
    a=self.getPinA()
    b=self.getPinB()
    
    if a==1 and b==1:
      return 1
    
    return 0
      
class OrGate(BinaryGate):
  
  def __init__(self,n):
    super(OrGate,self).__init__(n)
    
  def performGateLogic(self):
    
    a=self.getPinA()
    b=self.getPinB()
    
    if a==1 or b==1:
      return 1
    return 0
  
class NotGate(UnaryGate):
  
  def __init__(self,n):
    super(NotGate,self).__init__(n)
    
  def performGateLogic(self):
    
    a= self.getPin()
    
    if a==1:
      return 0
    return 1
  
g2 = OrGate("G2")
print(g2.getOutput())


g3 = NotGate("G3")
print(g3.getOutput())