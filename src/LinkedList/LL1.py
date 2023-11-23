class LL:

  class Node:
    def __init__(self,value,next):
      self.next = next
      self.value = value
      
  def __init__(self,head=None,tail=None,size=0):
    self.head = head
    self.tail = tail
    self.size = size
  
  def display(self):
    temp = self.head
    while(temp):
      print(temp.value)
      temp = temp.next
  
  def insert(self,value):
    temp = self.Node(value,None)
    if(self.size == 0):
      self.head = self.tail = temp
      print("size 0")
    else:
      self.tail.next = temp
      self.tail = temp
      print("size > 0")
    self.size = self.size + 1
  
    
#main

L1 = LL()
L1.insert(1)
L1.insert(2)
L1.insert(5)
L1.display()
