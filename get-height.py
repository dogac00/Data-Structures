def getHeight(self):
  if(self.left and self.right):
    return 1 + max(self.left.getHeight(), self.right.getHeight())
  elif(self.left):
    return 1 self.left.getHeight()
  else:
    return 1
    
// The code above is in the Tree class

def getHeight(self):
  if self.root:
    return self.root.getHeight()
  else:
    return 0
