class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def RemoveNode(self, removekey):
       HeadVal= self.headval

       if HeadVal is not None:
           if HeadVal.dataval == removekey:
               self.headval = HeadVal.nextval
               HeadVal = None
               return
       while HeadVal is not None:
           if HeadVal.dataval == removekey:
               break
           prev = HeadVal.nextval
           HeadVal = HeadVal.nextval
           if HeadVal == None :
               return
           prev.next = HeadVal.nextval
           HeadVal = None




   def Inbetween(self, middle_node, newnode):
       if middle_node is None:
           print("The mentioned node is None")
           return
       NewNode = Node(newnode)
       NewNode.nextval = middle_node.nextval
       middle_node.nextval = NewNode


# Function to add newnode
   def AtEnd(self, newdata):
      NewNode = Node(newdata)
      if self.headval is None:
         self.headval = NewNode
         return
      laste = self.headval
      while(laste.nextval):
         laste = laste.nextval
      laste.nextval=NewNode
# Print the linked list
   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

# list.AtEnd("Thu")
# list.Inbetween(list.headval.nextval, "Fri")
list.RemoveNode("Tue")
list.listprint()