class Node():
  def __init__(self,val):
    self.left = None
    self.right = None
    self.val = val

class BinarySearchTree():
  def __init__(self):
    self.root = None

  def insert(self,val):
    newNode = Node(val)
    if self.root == None:
      self.root = newNode
      return
    else:
      curr_node = self.root
      while True:
        if val < curr_node.val:
          if curr_node.left == None:
            curr_node.left = newNode
            return
          else:
            curr_node = curr_node.left
        elif val > curr_node.val:
          if curr_node.right == None:
            curr_node.right = newNode
            return
          else:
            curr_node = curr_node.right

  def lookup(self,val):
    curr_node = self.root
    while True:
      if curr_node == None:
        return False
      if curr_node.val == val:
        return curr_node.val
      elif val < curr_node.val:
        curr_node = curr_node.left
      else:
        curr_node = curr_node.right

