def isValidExpression(expression):
  
  ops =[]
  values=[]
  
  operators=["*","+","-","/"]
  
  for element in expression.split():
    
    if element == ")":
      operation=ops.pop()
      
      num1,num2=ops.pop(),ops.pop()
      
      result = evaluateExpression(num1,num2,operation)
      
      values.append(result)
      
    if element in operators:
       ops.append(element)
    
    
       
       
def evaluateExpression(num1,num2,operation):
  
  if operation=="*":
    result =int(num1) * int(num2)
  elif operation=="-":
    result =int(num1) - int(num2)
  elif operation=="+":
    result =int(num1) + int(num2)
  else :
    result =int(num1) // int(num2)
  
  return result
  
    
