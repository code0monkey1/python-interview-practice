class Node:
  
  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next


class LinkedList:
 
  def __init__(self,head=None):
    self.head=head
  
  def getHead(self):
    return self.head
  
  def insert(self,target_index,node):
    
    if self.head is None:
      self.head=node
      return
    
    currentIndex=0
    currentNode=self.head
    

    while currentNode.next!=None and currentIndex+1<target_index:
      currentNode=currentNode.next
      currentIndex+=1
   
    node.next=currentNode.next
    currentNode.next=node
      
    
  def append(self,node):
    
    if self.head==None:
      self.head=node
      return
    
    currentNode= self.head
     
    while currentNode.next!=None:
      currentNode=currentNode.next
    
    currentNode.next=node
    
  def reverse_print(self,node=None):
     
     if node==None :
       return
    
     self.reverse_print(node.next)
     print(node.data)
     
    
  def insert_at_start(self,node):
     if self.head==None:
       self.head=node
       return
     
     headNode=self.head
     self.head=node
     self.head.next=headNode
     
  def print_list(self):
    
    currentNode=self.head
    
    while currentNode!=None:
      print(currentNode.data,end=',')  
      currentNode=currentNode.next
    print()
     
    
if __name__ == "__main__":
  linked_list= LinkedList()
  head = Node(4)
  linked_list.append(head)
  linked_list.append(Node(10))
  linked_list.print_list()
  
  linked_list.insert(1,Node(100))
  linked_list.print_list()
  
  linked_list.reverse_print(head)

  