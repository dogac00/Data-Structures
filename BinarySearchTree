from Defining-a-Binary-Tree import Node

class BinarySearchTree(object):
  
  def __init__(self):
    self.root = None
  
  def insert(self,data):
    if not self.root:
      self.root = Node(data)
    else:
      self.root.insert(data)
  
  def remove(self, dataToRemove):
    if self.root:
      if(self.root.dat == dataToRemove):
        temp = Node(None)
        temp.left = self.root
        self.root.remove(dataToRemove, temp)
      else:
        self.root.remove(dataToRemove, None):
  
  def getMax(self):
    if self.root:
      return self.root.getMax()
  
  def getMin(self):
    if self.root:
      return self.root.getMix()
      
  def traverseInOrder(self):
    if self.root:
      self.root.traverseInOrder()
  
