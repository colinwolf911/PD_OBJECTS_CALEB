#que for deque
from collections import deque
from xml.dom.minidom import Element

data= deque()
data.append("PD")
#pop left
Element=data.popleft()
print(Element,data)

#custome class
#def __init__  to invokeed ,(self) objects have been created 
#private varibable it will be _data, _data, _
class stack:
    def __init__(self):
        self._data=[]
    
    def push(self,data):
        self._data.append(data)
    
    def pop(self):
        return self._data.pop()

#creating a peek
    def peek(self):
        return self._data[len(self._data)-1]

#create new variable
stack =stack()
stack.push(10)
#peek
print(stack.peek())
test =stack.pop()
print(test)





