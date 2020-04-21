#Implement Stack using a Linked List
#LIFO
class Node:
  def __init__(self,val):
    self.val = val
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0
  
  def peek(self):
    return self.top.val

  def push(self,val):
    new_node = Node(val)
    if self.bottom == None:
      self.bottom = new_node
      self.top = self.bottom 
      self.length = 1
    else:
      self.top.next = new_node
      self.top = new_node
      self.length += 1

  def pop(self):
    count = 1
    curr = self.bottom
    size = self.length - 1
    while count != size:
      curr = curr.next
      count += 1
    pop_val = curr.next
    curr.next = None
    self.top = curr
    self.length -= 1
    return pop_val.val

  def printStack(self):
    temp = self.bottom
    while temp != None:
      print(temp.val)
      temp = temp.next
    print()

newstack = Stack()
newstack.push(10)
newstack.push(20)
newstack.push(30)
newstack.pop()
newstack.pop()
newstack.printStack()
    
#Implement Stack using arrays
class Stack:
  def __init__(self):
    self.arr = []
    self.length = 0
  
  #Making the stack readable
  def __str__(self):
    return str(self.__dict__)
  
  def peek(self):
    return self.arr[self.length-1]

  def push(self, val):
    self.arr.append(val)
    self.length += 1
  
  def pop(self):
    popped_item = self.arr[self.length - 1]
    del self.arr[self.length - 1]
    self.length -= 1
    return popped_item

  

