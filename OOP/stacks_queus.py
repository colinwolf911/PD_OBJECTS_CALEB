data=[]
#push append
#pop
data.append(6)
#peek the element of data
print (data[len(data)-1])
#we didn't threw out the any data with peek
element=data.pop()
#invoke the pop
print(element)
print(data)
#using the list few function such as pop and push to keeping the intergty of stacks

#eg: stack  first in last out 
data=[]
data.append(5)
data.append(10)
data.append(15)
data.append(20)
data.pop()
data.pop()
print(data)


#que left it will be infornt of que
data=[]
#enqueue
data.append(5)
data.append(10)
data.append(15)
data.append(20)
#dequeue
data.pop(0)
element =data.pop(0)
#peek it doesn't remove the element  but each time we removed the element the data scoop down which is time consumption which is o(n)to avovid it import deque
print(data[0])
print(element)
print(data)
