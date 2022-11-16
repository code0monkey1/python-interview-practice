# Practice Problem : https://www.codechef.com/problems/RNT011

class Stack:
  def __init__(self):
    self.list=[]
    self.count=0
  
  def push(self,value):
    self.list.append(value)
    self.count+=1 
    return value
    
  def pop(self):
    if self.list!=[]:
      value= self.list.pop()
      self.count-=1
      return value
    
  def size(self):
    return self.count
  
  def isEmpty(self):
    return self.list==[]
  
  def peek(self):
    return self.list[len(self.list)-1]
  

# s=Stack()

# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())

# #balanced parenthesis

# stack= Stack()

# parenthesis1='(()(()(()))()(()()))'



def isBalanced(parenthesis):
  opener="[({"
  closer="])}"
  
  for ch in parenthesis:
     
      if ch in opener:
        stack.push(ch)
      elif ch in closer:
          if stack.isEmpty():
            return 'NO'
          else:
            top=stack.peek()
            if not matches(top,ch):
              return 'NO'
            stack.pop()    
        
  if stack.isEmpty():
    return 'YES'
  
  return 'NO'

def matches(opening, closing):
 
  opener="[({"
  closer="])}"

  return opener.index(opening) == closer.index(closing)

        
if __name__ == "__main__":
  num = int(input())
  
  for i in range(num):
    stack = Stack()
    parenthesis = input()
    print(isBalanced(parenthesis))
   
