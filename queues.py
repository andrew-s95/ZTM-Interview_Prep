#Implement a Queue with Linked-List
class Node:
  def __init__(self,val):
    self.val = val
    self.next = None
  
class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0
  
  def peek(self):
    if self.length == 0:
      return None
    else:
      return self.first.val
  
  def enqueue(self,val):
    newNode = Node(val)
    if self.length == 0:
      self.first = newNode
      self.length += 1
    else:
      self.last.next = newNode
      self.last = newNode
      self.length += 1

  def dequeue(self):
    temp = self.first.next
    dequeuedNode = self.first
    if temp == None:
      self.first = None
      self.length -= 1
      return dequeuedNode
    else:
      self.first.next = None
      self.first = temp
      self.length -= 1
    return dequeuedNode