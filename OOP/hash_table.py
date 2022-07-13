#set
#data ={}
#create the set
#colours={"red"}
#colours=set()
#print(type(data))
#print(type(colours))


#order dictionary
#from collections import OrderedDict
#od=OrderedDict()
#od.

#hash table is unordered
#no duplicated keys
#duplicated value is okay
from cgi import test
from types import NoneType


data ={"colin":"c@gmail.com","john":"j@gmail.com","allen":"a@gmail.com","colin":"cbsdf@gmail.com","colin00":"c@gmail.com"}
print(data)
#passing the key
print(data['colin'])

##how python built in dictionaries  implemented at stackflow
#key has been hashed 
print(hash("colin"))
#SOMETHING CANNOT BE HASHED SUCH AS LIST ARRAY
#print(hash([]))

#eg: unhashable
class Test:
    pass
    ___hash__ =None

#print(hash(Test()))

data0={"red","blue","black","purple","green"}
data1={"blue","orange","purple","green"}

# data0+data1 is a list ,here it's difference

#union
all_data=data0 |data1
print(all_data)

#intersection (elements shared between both)
shared_data= data0 & data1
print(shared_data)


#method versions
all_data=data0.union(data1)
print(all_data)

shared_data=data0.intersection(data1)
print(shared_data)


##difference and symmetric difference
data0={}