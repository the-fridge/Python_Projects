#Simple HashSet
#@author Prohunt
import sys
class HashSet:
  cap = sys.maxint/20
  list = sys.maxint/20*[None]
  size = 0
  def hash(self, element):
    index = hash(element)
    if index < 0:
      index = index * -1
    while index > self.cap:
      index = index / 10
    return index
  def contains(self, element):
    index = self.hash(element)
    print " "
    print index
    if self.list[index] is element :
      return True
    else :
      while self.list[index] is not element:
        if self.list[index] is None:
          return False
        index = index + 1
    return True
  def add(self, element):
    if self.contains(element):
      return False
    index = self.hash(element)
      
    while self.list[index] is not None:
      index = index + 1
    self.list[index] = element
    self.size = self.size + 1
    return True
  def getSize(self):
    return self.size
  def init(self):
    self.size = 0
    
  
def main():
  string1 = "hello"
  string2 = "world"
  stringSet = HashSet()
  stringSet.add(string1)
  stringSet.add(string2)
  
  if stringSet.contains("hello") and stringSet.contains("world"):
    print "set contains both hello and world"
  if not stringSet.contains("Hello") and  not stringSet.contains("World"):
    print "set does not contain Hello and World"
  
  print "Size of the list: "
  print stringSet.getSize()
if __name__ == "__main__" :main()