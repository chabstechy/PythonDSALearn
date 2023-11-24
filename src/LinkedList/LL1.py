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
    print("-----------------")
    if(self.size == 0):
      print("LL is empty")
    else: 
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

  def insertFirst(self,value):
    temp = self.Node(value,self.head)
    self.head = temp
    self.size = self.size + 1
    if(self.tail==None):
      self.tail = self.head
        
  def insertAtIndex(self,value, index):
    if(index < 1 or index > self.size + 1):
      print("Invalid index")
      return
      
    if(index == self.size + 1):
      self.insert(value)
    elif (index == 1):
      self.insertFirst(value)
    else:
      print("here it comes")
      i = 1
      temp1 = self.head
      while(temp1):
        if(i==index):
          temp = self.Node(value, temp1.next)
          temp1.next = temp
          self.size = self.size + 1
          break
        i = i + 1
        temp1 = temp1.next

#main

L1 = LL()
L1.insert(1)
L1.insert(2)
L1.insert(5)
L1.display()
