class Node:
  def __init__(self, data):
    self.data = data
    self.children = []
  
  def addChild(self, data):
    temp = Node(data)
    self.children.append(temp)
    
  def searchChildren(self, val):
    for child in self.children:
      if(child.data == val):
        return True
    for child in self.children:
      if(child.children):
        return child.searchChildren(val)
    return False
    
  def searchNode(self, val):
    if(self.data == val):
      return True
    
    return self.searchChildren(val)
  
  def printChildren(self):
    print([node.data for node in self.children])
    
  def addChildtoChild(self, childData, data):
    temp = Node(data)
    if(self.data == childData):
      self.children.append(temp)
    for node in self.children:
      if node.data == childData:
        node.children.append(temp)
    for node in self.children:
      if node.children:
        for n in node.children:
          n.addChildtoChild(childData, data)
  
dogac = Node(1)
dogac.addChild(2)
dogac.addChild(3)
dogac.addChild(4)
dogac.addChildtoChild(2,5)
dogac.addChildtoChild(2,6)
dogac.addChildtoChild(2,7)
dogac.addChildtoChild(6,8)

print(dogac.searchNode(1)) # True
print(dogac.searchNode(3)) # True
print(dogac.searchNode(2)) # True
print(dogac.searchNode(5)) # True
print(dogac.searchNode(6)) # True
print(dogac.searchNode(8)) # True
