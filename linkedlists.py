#Create SLL

class Node:
  def __init__(self, val):
    self.next = None
    self.val = val

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def append(self, val):
    new_node = Node(val)
    if self.head == None: 
      self.head = new_node
      self.tail = new_node
      self.length = 1
    else:
      self.tail.next = new_node
      self.tail = new_node
      self.length += 1
  
  def prepend(self, val):
    new_node = Node(val)
    if self.head == None:
      self.head = new_node
      self.length = 1
    else:
      temp = self.head
      self.head = new_node
      new_node.next = temp
      self.length += 1
  
  def insert(self, idx, val):
    new_node = Node(val)
    count = 0
    temp = self.head
    #edge cases
    if idx >= self.length:
      self.append(val)
    if idx == 0:
      self.prepend(val)
    #main 
    while count < self.length:
      if count == idx-1:
        temp.next, new_node.next = new_node, temp.next
        self.length += 1
      else:
        temp = temp.next
        count += 1

  def remove(self, idx):
    temp = self.head
    count = 0
    if idx > self.length:
      return "This index doesn't exist"
    while count < self.length:
      if idx == 0:
        self.head = temp.next
        self.length -= 1
      if count == self.length - 1:
        temp.next = None
        self.tail = temp
        self.length -= 1
      if count == idx - 1:
        temp.next = temp.next.next
        self.length -= 1
      else:
        count += 1
        temp = temp.next

  def printList(self):
    temp = self.head
    while temp != None:
      print(temp.data)
      temp = temp.next
    print()
    print(str(self.length)+ "Length")

  def reverse(self):
    prev = None
    self.tail = self.head
    while self.head != None:
      temp = self.head
      self.head = self.head.next
      temp.next = prev
      prev = temp
    self.head = temp 







    

